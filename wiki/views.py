from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse

from wiki.models import Page

import time
import datetime
import git

def get_file(tree, path):
    for f in path.split('/'):
        if type(tree.get(f)) == git.Tree:
            tree = tree.get(f)
        else:
            return tree.get(f)
    return None

def view(request, path, revision=None):

    print path
    print revision

    repo = git.Repo('/home/stein/Labs/GitWiki/repo')
    if revision:
        head = repo.commit(revision)
    else:
        head = repo.commit('HEAD')
    tree = head.tree

    content = ':author: none\n\n' + get_file(tree, path).data

    history = git.Commit.find_all(repo, 'HEAD', path)[:5]
    for i in history: i.date = datetime.datetime.fromtimestamp(time.mktime(i.committed_date))

    return render_to_response('wiki/view.html', {'content': content, 'path': path, 'history': history})
