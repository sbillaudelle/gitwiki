from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.template import Template, Context
from django.templatetags.markup import restructuredtext
from django.utils.safestring import mark_safe

from wiki.models import Page, PageType

import time
import datetime
import git
import repo

import re

REGEXP = re.compile('^%%(?P<type>.*)')

REPO = repo.get_repository()

def view(request, path, revision=None):
    revision = REPO.commit(revision or 'HEAD')
    try:
        sourcefile = repo.get_file_from_tree(revision.tree, path)
    except git.NoSuchPathError:
        raise Http404("Page '%s' not found." % path)

    content = sourcefile.data

    first_line = content.split('\n')[0]
    if first_line.startswith('%%'):
        m = REGEXP.match(first_line)
        if m:
            type = PageType.objects.get(id=m.group('type').strip())
            content = '\n'.join(content.split('\n')[1:])
            if type.markup == 'restructuredtext':
                content = restructuredtext(':author: none\n\n' + content)
            elif type.markup == 'html':
                content = mark_safe(content)

            layout = type.layout
            t = Template(layout)

    history = git.Commit.find_all(REPO, 'HEAD', path)[:5]
    for i in history: i.date = datetime.datetime.fromtimestamp(time.mktime(i.committed_date))

    return HttpResponse(t.render(Context({'content': content, 'path': path, 'history': history})))
