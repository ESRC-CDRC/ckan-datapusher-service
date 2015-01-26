import os
import sys
import hashlib

activate_this = os.path.join(os.environ['CKAN_HOME'], 'bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

import ckanserviceprovider.web as web
import datapusher.jobs as jobs
os.environ['JOB_CONFIG'] = os.path.join(os.environ['CKAN_CONFIG'], 'datapusher_settings.py')

web.init()
application = web.app