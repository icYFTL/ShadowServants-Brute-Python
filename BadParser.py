# Version 0.1

import re
import requests
import Stopwatch

true_set = []
handled = 0

class BadParser(object):
    def Grab(page):
        print('[Bad parser v0.3 beta]\n')
        global true_set
        global handled
        while page != 0:
            print('Wait for data from proxy server.\n')
            timer = Stopwatch.create_thread()
            data = requests.get("https://proxylist.me/?protocol=1&filtrar=Filtrar&page="+str(page)).text
            print('Got data. Parsing initializated.\nTime spent: '+str(timer.secs) + ' secs.\n')
            timer.kill_thread()
            data = data.replace(' ','')
            proxy = re.findall(r'<tdclass=\"ip\"><ahref=\"[A-Za-z\/0-9-]+\">[0-9]+.[0-9]+.[0-9]+.[0-9]+</a></td>\n\n<tdclass=\"port\">[0-9]+', data)
            for i in proxy:
                prox = ''
                i = str(i)
                i = i.replace('</a></td>\n\n<tdclass="port">',':')
                found = False
                for j in range(len(i)):
                    if (str.isdecimal(i[j]) and i[j-1] == '>') or (found):
                        found = True
                        prox += i[j]
                true_set.append(prox)
                handled += 1
            page -= 1
        print('\nOk. Work done.\nTotal handled: ' + str(handled))
        return true_set