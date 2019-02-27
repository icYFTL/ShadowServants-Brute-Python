# Version 1.0 alpha
'''
How to use:
    Example:
        type_of_proxy = 1 # 1 - http, 2 - https, 3 - socks4, 4 - socks5
        proxycount = 5000 # Up to 10000 besides socks5(socks 5 up to 200)

        a = BadParser(type_of_proxy,proxycount)
        data = a.Grab()

        # data = [1.1.1.1:8000, ...]
'''
import requests

class BadParser:
    def __init__(self, kind, count):
        print('[BadParser v.1.0 alpha]\n')
        if kind == 1:
            self.kind = 'http'
        elif kind == 2:
            self.kind = 'https'
        elif kind == 3:
            self.kind = 'socks4'
        elif kind == 4:
            self.kind = 'socks5'

        self.count = count
        self.handled = 0
        self.proxy_list = []

    def Grab(self):
        print('Work initiated. Getting data from server.')
        r = requests.get('https://www.proxy-list.download/api/v1/get?type={}&anon=elite'.format(self.kind))
        print('Getting done. Parsing started.')
        r = r.text.split('\r\n')
        for i in r:
            if int(self.handled) < int(self.count):
                if i != '':
                    self.proxy_list.append(i)
                    self.handled += 1
            else:
                break
        print('Work done.\n')
        return self.proxy_list

