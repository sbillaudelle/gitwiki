import os
from django.conf import settings
from django.http import HttpResponse

def update(request):
    # Commit information is in request.POST.get('payload')

    print "Updating git repository..."

    # manual pulling here because apparently GitPython does not offer a
    # .pull() method.
    os.system('cd %s; git pull' % settings.REPOSITORY_PATH)

    return HttpResponse("Done.", mimetype='text/plain')
