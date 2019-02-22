import os
from BadParser import BadParser

proxies = set()

class ProxyWorker (object):
    def handler(path):
        if (os.path.isfile(path=path) != True):
            return False
        if (os.path.splitext(path)[1] != '.txt'):
            return False
        f = open(path, 'r')
        line = f.readline()
        while(line):
            proxies.add(line)
            line = f.readline()
        f.close()
        return proxies
    
    def AutoGrabber():
        return BadParser.Grab(5)
