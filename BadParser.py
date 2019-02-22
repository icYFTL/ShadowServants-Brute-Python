# Version 0.2

import cfscrape
import re
import Stopwatch

class BadParser(object):
    def Grab():
        r = cfscrape.create_scraper()
        handled = 0
        true_set = []

        print('[Bad parser v0.2 beta]\n')

        print('Wait for data from proxy server.\n')
        timer = Stopwatch.create_thread()
        data = r.get("https://hidemyna.me/ru/proxy-list/").text
        print('Got data. Parsing initializated.\nTime spent: '+str(timer.secs) + ' secs.\n')
        timer.kill_thread()

        try:

            proxy = re.findall(r'<td class=tdl>[0-9]+.[0-9]+.[0-9]+.[0-9]+<\/td><td>[0-9]{1,5}', data)

            for i in proxy:
                i = str(i)
                i = i.replace('<td class=tdl>','')
                i = i.replace('</td><td>',':')
                true_set.append(i)
                handled += 1
                print('Proxy handled: ' + str(handled))
            raise KeyboardInterrupt
        except KeyboardInterrupt:
            print('\nOk. Work done.')
            return true_set
