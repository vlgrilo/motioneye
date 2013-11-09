
import logging
import os.path
import sys

# you normally don't have to change these 
PROJECT_PATH = os.path.dirname(sys.argv[0])
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')
STATIC_PATH = os.path.join(PROJECT_PATH, 'static')

# static files (.css, .js etc) are served at this root url
STATIC_URL = '/static/'

# path to the config directory; must be writable
CONF_PATH = os.path.abspath(os.path.join(PROJECT_PATH, 'conf'))

# logs, pid files and other output files go here
RUN_PATH = os.path.abspath(os.path.join(PROJECT_PATH, 'run'))

# repository details for software updating
REPO = ('ccrisan', 'motioneye')

# set to logging.DEBUG for verbose output
LOG_LEVEL = logging.INFO

# set to 127.0.0.1 to restrict access to localhost
LISTEN = '0.0.0.0'

# change the port according to your requirements/restrictions
PORT = 8765

# interval in seconds at which motionEye checks if motion is running
MOTION_CHECK_INTERVAL = 10

# interval in seconds at which the janitor is called to remove old images and movies
CLEANUP_INTERVAL = 43200

# timeout in seconds to wait for responses when contacting a remote server
REMOTE_REQUEST_TIMEOUT = 10