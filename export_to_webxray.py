'''
    This script copies all required files from a built version of the
    jQuery repository to the given webxray repository.
'''

import os
import sys
import json
from distutils.dir_util import mkpath
from distutils.file_util import copy_file

ROOT = os.path.dirname(os.path.abspath(__file__))
path = lambda *a: os.path.join(ROOT, *a)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "usage: %s <path-to-webxray-repository>"
        sys.exit(1)

    def webxray_path(*parts):
        base = os.path.abspath(sys.argv[1])
        return os.path.join(base, *parts)
    
    config = json.load(open(webxray_path('config.json')))
    
    for filename in config['compiledFileParts']:
        if filename.startswith('jquery'):
            src = os.path.normpath(path('..', filename))
            dest = webxray_path(filename)            
            print '%s -> %s' % (src, dest)
            dest_dir = os.path.dirname(dest)
            mkpath(dest_dir)
            copy_file(src, dest)

    extras = {
        "dist/jquery.min.js": "static-files/jquery.min.js",
        "test/qunit/qunit/qunit.js": "test/qunit.js",
        "test/qunit/qunit/qunit.css": "test/qunit.css"
    }
    
    for src, dest in extras.items():
        src = path(src)
        dest = webxray_path(dest)
        print "%s -> %s" % (src, dest)
        copy_file(src, dest)
