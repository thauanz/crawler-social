from fabric.api import *

env.hosts = ['192.168.99.103']
env.user = "deployer"
env.git_clone = "https://github.com/thauanz/crawler-social.git"
env.password = "123456789"
env.shell = "/bin/sh -c"
env.key_filename = 'local'

def deploy():
    with settings(warn_only=True):
        with cd("/app"):
            run("cd /app && git clone %(git_clone)s" % { 'git_clone':env.git_clone })