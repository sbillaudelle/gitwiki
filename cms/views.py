from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.template import Template, Context
from django.templatetags.markup import restructuredtext
from django.utils.safestring import mark_safe

from cms.models import PageType

from cms import register_template

import time
import datetime
import git
import repo

REPO = repo.get_repository()

def view(request, path, revision=None):
    revision = REPO.commit(revision or 'HEAD')
    try:
        sourcefile = repo.get_file_from_tree(revision.tree, path)
    except git.NoSuchPathError:
        raise Http404("Page '%s' not found." % path)

    content = sourcefile.data

    first_line = content[:content.find('\n')]
    if first_line.startswith('%%'):
        content_type = first_line[2:]
        if content_type:
            page_type = PageType.objects.get(id=content_type.strip())

            layout = page_type.layout
            template = Template(layout, name='main_template')

            content = content[content.find('\n')+1:]
            if page_type.markup == 'restructuredtext':
                content = restructuredtext(':author: none\n\n' + content)
            elif page_type.markup == 'html':
                content = mark_safe(content)
            elif page_type.markup == 'template':
                register_template('main_template', layout)
                template = Template('{% extends "main_template" %}\n' + content)

    else:
        layout = """{{ content }}"""

    

    history = git.Commit.find_all(REPO, 'HEAD', path)[:5]
    for i in history: i.date = datetime.datetime.fromtimestamp(time.mktime(i.committed_date))

    return HttpResponse(template.render(Context({'content': content, 'path': path, 'history': history})))
