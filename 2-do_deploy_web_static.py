#!/usr/bin/python3
'''Fabric task 2 Module'''

from fabric.api import *
from datetime import datetime

env.hosts = ['35.229.44.12']
env.user = 'ubuntu'


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

def do_deploy(archive_path):
    '''Deploy the tgz file in the server'''
    if (not archive_path):
        return (False)
    else:
        try:
            put(archive_path, "/tmp")
            file_name = archive_path[9:]
            release_name = file_name[:-4]
            release_folder = "/data/web_static/releases/" + release_name
            run("mkdir -p " + release_folder)
            run("tar zxvf /tmp/" + file_name + " -C " + release_folder)
            run("mv " + release_folder + "/web_static/* " + release_folder)
            run("rm -rf " + release_folder + "/web_static/")
            run("rm -rf /tmp/" + file_name)
            run("rm /data/web_static/current")
            run("ln -sf " + release_folder + " /data/web_static/current")
            return (True)
        except:
            return (False)
