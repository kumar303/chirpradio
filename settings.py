# Copyright 2008 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Django settings for chirpradio project.

import os
import sys
from common import in_dev

IN_DEV = in_dev()
DEBUG = IN_DEV
# DEBUG = False
TEMPLATE_DEBUG = DEBUG

ROOT_PATH = os.path.dirname(__file__)
ROOT_ABSPATH = os.path.abspath(ROOT_PATH)

ADMINS = (
    # fixme: make this a CHIRP distribution list maybe?
    ('Kumar McMillan', 'kumar.mcmillan@gmail.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'appengine'  # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = ''             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# The full site URL, used for external redirects.
SITE_URL = (IN_DEV and 'http://localhost:8000'
            or 'https://chirpradio.appspot.com')

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT =  os.path.join(ROOT_ABSPATH, 'media')

# URL to access the media directory:
MEDIA_URL = '/media/'

# The following URLs will not require user login.  See auth/middleware.py.
# These are *path prefixes*.  That is, anything underneath these URLs are
# also public.
#
# Auth is handled in app.yaml or not applicable for these URLs.  For tasks,
# this is necessary so they are executed by Admin user
# (internal Task Queue user)
PUBLIC_TOP_LEVEL_URLS = ['/playlists/task',
                         '/auth/task',
                         '/auth/cron',
                         '/_ah/warmup',
                         '/fbapp',  # facebook app
                         '/m'  # go_mobile()
                         ]

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'auth.middleware.AuthenticationMiddleware',
    'playlists.middleware.FromStudioMiddleware'
]

if not DEBUG:
    # when in production, install this error handler
    # (otherwise, let the debug middleware handle the request)
    MIDDLEWARE_CLASSES.append(
        # from:
        # http://github.com/wtanaka/google-app-engine-django-errors
        'errors.middleware.GoogleAppEngineErrorMiddleware'
    )

TEMPLATE_CONTEXT_PROCESSORS = (
    'common.context_processors.base',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, 'templates'),
)

INSTALLED_APPS = (
     'appengine_django',
     'auth',
     'common',
     'djdb',
     'landing_page',
     'playlists',
     'traffic_log',
     'errors',
     'jobs'
)

# Hmm, maybe there is a better way to detect that we're running tests.
RUNNING_TESTS = 'test' in sys.argv

if RUNNING_TESTS:
    INSTALLED_APPS += (
        'django_nose',
    )

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = ['--logging-clear-handlers', '--with-nicedots']

NOSE_PLUGINS = [
    'nosenicedots.plugin.NiceDots',
]


# Each module here defines job workers so they must be imported
# by the job runner.
JOB_WORKER_MODULES = [
    'playlists.reports',
    'traffic_log.views',
]
