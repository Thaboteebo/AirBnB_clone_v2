#!/usr/bin/python3
"""
Deletes out-of-date archives
fab -f 100-clean_web_static.py do_clean:number=2
    -i ssh-key -u ubuntu > /dev/null 2>&1
"""

import os
from fabric.api import *

env.hosts = ['34.224.95.34', '100.25.149.113']


def do_clean(number=0):
    """Delete out-of-date archives.
    Args:
        number (init): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent archuve. If
    number is 2, keeps the most and second-most recent archives,
    ect.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        run("rm -rf ./{}".format(a)) for a in archives]
