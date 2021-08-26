#!/usr/bin/python3
'''Fabric task 1 Module'''

from fabric.api import *
from datetime import datetime


def do_pack():
    '''Make de tgz file'''
    try:
        local('mkdir -p versions')
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        name = "web_static_" + timestamp + ".tgz"
        tar = local("tar -cvzf versions/" + name + " web_static")
        return ("versions/" + name)
    except:
        return (None)
