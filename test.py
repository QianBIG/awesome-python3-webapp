from fabric.api import local, lcd

def lsfab():
    with lcd('.'):
        local('ls')