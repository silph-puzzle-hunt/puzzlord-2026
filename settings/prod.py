from settings.base import *
from settings.base import SECRET_KEY
from settings.base import SITE_PASSWORD

DEBUG = False

ALLOWED_HOSTS = ['puzzlord-2026.onrender.com']

# security checks
assert SECRET_KEY != "FIXME_SECRET_KEY_GOES_HERE"
assert SITE_PASSWORD != "FIXME_PASSWORD_GOES_HERE"
