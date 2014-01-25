# -*- coding: utf-8 -*-

import os
from subprocess import call
import sys

THIS_DIR = os.path.dirname(__file__)


def bin_dir(home_dir):
    if sys.platform == 'win32':
        bdir = 'Scripts'
    else:
        bdir = 'bin'
    return os.path.join(home_dir, bdir)


def pip(home_dir, *args):
    pip_path = os.path.join(bin_dir(home_dir), 'pip')
    call([pip_path] + list(args))


def after_install(options, home_dir):
    requirements_txt = os.path.join(THIS_DIR, 'requirements.txt')
    pip(home_dir, 'install', '-r', requirements_txt)
    manage_py = os.path.join(THIS_DIR, 'manage.py')

    print
    print 'Make sure Sass is installed.'
    print
    print 'Now run the following:'
    print
    if sys.platform == 'win32':
        print os.path.join(bin_dir(home_dir), 'activate.bat')
    else:
        print 'source {}'.format(os.path.join(bin_dir(home_dir), 'activate'))
    print '{} syncdb'.format(manage_py)
    print '{} migrate'.format(manage_py)
    print '{} runserver'.format(manage_py)
