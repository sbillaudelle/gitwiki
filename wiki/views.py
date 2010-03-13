from django.shortcuts import render_to_response
from django.http import Http404

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

    content = ':author: none\n\n' + sourcefile.data

    history = git.Commit.find_all(REPO, 'HEAD', path)[:5]
    for i in history: i.date = datetime.datetime.fromtimestamp(time.mktime(i.committed_date))

    return render_to_response('view.html', {'content': content, 'path': path, 'history': history})
