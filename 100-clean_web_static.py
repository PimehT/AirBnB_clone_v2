#!/usr/bin/python3
"""Fabric script that deletes out-of-date archives"""
from fabric.api import run, env, local
from datetime import datetime
import os


env.hosts = ['54.152.129.50', '54.236.43.35']


def do_clean(number=0):
    if int(number) < 2:
        number = 1
    else:
        number = int(number)

    local("ls -ltr versions | tail -n +{} | awk '{{print $9}}' \
| xargs -I {{}} rm versions/{{}}".format(number + 1))

    run("ls -ltr /data/web_static/releases | tail -n +{} | awk '{{print $9}}' \
| xargs -I {{}} rm -rf /data/web_static/releases/{{}}".format(number + 1))
