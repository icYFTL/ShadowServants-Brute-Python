import cfscrape
from bs4 import BeautifulSoup
import re

r = cfscrape.create_scraper()


print('[Bad parser v0.1 beta]\n')
print('Really works bad because I was writing this at 04:00 am. Don\'t hit me, pls. I\'ll re-write it. May be. 50/50 =)\nYou can stop parse by CTRL+C.\n\n\n')


print('Wait for data from proxy server.')

data = r.get("https://hidemyna.me/ru/proxy-list/").text

print('Got data. Parsing initializated.\n')

soup = BeautifulSoup(data, 'html.parser')

true_set = []

parsed = soup.findAll('td')
proxy = re.findall(r'[0-9]+.[0-9]+.[0-9]+.[0-9]+',str(parsed))
for i in proxy:
    if (len(i) > 0):
        true_set.append(i)

    for i in range(len(parsed)):
        try:
            for j in true_set:
                if j in parsed[i]:
                   parsed[i] = None
        except TypeError:
            continue
count = 0
for i in range(len(str(parsed))):
    try:
        if str.isdecimal(str(parsed)[i]):
            if str(parsed)[i-1] == '>' and str(parsed)[i-2] == 'd':
                true_set[count] += ":"
                while(str.isdecimal(str(parsed)[i])):
                    true_set[count]+=str(parsed)[i]
                    i += 1
                print("Proxies handled: " + str(count))
                count+=1
    except TypeError:
        continue
    except KeyboardInterrupt:
        print('\n\nOk. Parsing done.\nHandled: ' + str(count-1))
        break

