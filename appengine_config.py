import pkg_resources
from google.appengine.ext import vendor
# add all lib directories
vendor.add('lib')

pkg_resources.working_set.add_entry('lib')
