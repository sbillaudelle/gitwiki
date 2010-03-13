from django.http import HttpResponseRedirect, HttpResponse
from django.template import Template, Context
from django.templatetags.markup import restructuredtext
from django.utils.safestring import mark_safe

from wiki.models import Page, PageType

import time
import datetime
import git

import re

REGEXP = re.compile('^%%(?P<type>.*)')

def get_file(tree, path):
    for f in path.split('/'):
        if type(tree.get(f)) == git.Tree:
            tree = tree.get(f)
        else:
            return tree.get(f)
    return None

def view(request, path, revision=None):

    repo = git.Repo('/home/stein/Labs/GitWiki/repo')
    if revision:
        head = repo.commit(revision)
    else:
        head = repo.commit('HEAD')
    tree = head.tree

    content = get_file(tree, path).data

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

    history = git.Commit.find_all(repo, 'HEAD', path)[:5]
    for i in history: i.date = datetime.datetime.fromtimestamp(time.mktime(i.committed_date))

    return HttpResponse(t.render(Context({'content': content, 'path': path, 'history': history})))
