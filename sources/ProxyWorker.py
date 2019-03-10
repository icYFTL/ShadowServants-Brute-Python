import os
from BadParser import BadParser

proxies = []


class ProxyWorker(object):
    def handler(path):
        if os.path.isfile(path=path) != True:
            return False
        if os.path.splitext(path)[1] != '.txt':
            return False
        f = open(path, 'r', encoding='utf-8')
        line = f.readline().replace('\\n', '')
        line = line.strip()
        while line:
            proxies.append(line)
            line = f.readline().replace('\\n', '')
            line = line.strip()
        f.close()
        return proxies

    def AutoGrabber(pages):
        print('\n')
        prox = BadParser(3, pages)
        data = prox.Grab()
        if ProxyWorker.FileCreating(data) is False:
            print('Can\'t save proxies.\n')
        return data

    def DirectoryChecker():
        try:
            if not os.path.exists('./proxies/'):
                os.mkdir('./proxies/')
                return True
        except:
            print('Can\'t save proxies.\n')
            return False

    def FileCreating(data):
        if ProxyWorker.DirectoryChecker() is False:
            return False
        f = open('./proxies/last_proxies.txt', 'w', encoding='utf-8')
        for i in data:
            f.write(i + '\n')
        f.close()
