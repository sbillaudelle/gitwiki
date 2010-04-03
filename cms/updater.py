import os
import subprocess
from django.conf import settings
from django.http import HttpResponse

def update(request):
    # Commit information is in request.POST.get('payload')

    print "Updating git repository..."

    # manual pulling here because apparently GitPython does not offer a
    # .pull() method.
    home = os.environ.get('HOME', None)
    os.environ['HOME'] = '/home/cream/'
    proc = subprocess.Popen(['git', 'pull'], cwd='/home/cream/www/main/cream/source/', stdout=subprocess.PIPE)
    proc.wait()
    with open('/home/cream/gitpulllog', 'w') as f:
        f.write(proc.stdout.read())
    return HttpResponse("Done.", mimetype='text/plain')
