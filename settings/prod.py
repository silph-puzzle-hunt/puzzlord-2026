from settings.base import *
from settings.base import SECRET_KEY
from settings.base import SITE_PASSWORD

DEBUG = False

ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# security checks
assert SECRET_KEY != "FIXME_SECRET_KEY_GOES_HERE"
assert SITE_PASSWORD != "FIXME_PASSWORD_GOES_HERE"
