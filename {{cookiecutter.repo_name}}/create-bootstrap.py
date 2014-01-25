#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from virtualenv import create_bootstrap_script

INSTALL_SCRIPT = 'install-and-run-app.py'


def main(argv):
    with open('bootstrap.py') as f:
        output = create_bootstrap_script(f.read())
    with open(INSTALL_SCRIPT, 'w') as f:
        f.write(output)
    os.chmod(INSTALL_SCRIPT, 0755)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
