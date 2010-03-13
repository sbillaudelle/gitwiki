import os
from django.conf import settings
from django.http import HttpResponse

def on_github_commit(request):
    # Commit information is in request.POST.get('payload')

    print "Got github Post-Receive-Hook, updating git repository..."

    # manual pulling here because apparently GitPython does not offer a
    # .pull() method.
    os.system('cd %s; git pull' % settings.REPOSITORY_PATH)

    return HttpResponse("Alles gut", mimetype='text/plain')
