from threading import Thread
from Cracker import Cracker
from PasswordsWorker import PasswordWorker
from ThreadStatic import ThreadStatic

class Threads(Thread):

    def __init__(self,proxy,login,passwords,passwordsids,name):
        Thread.__init__(self)
        self.proxy = proxy
        self.login = login
        self.passwords = passwords
        self.passwordsids = passwordsids
        self.name = name

    def run(self):
        print('Thread #' + str(self.name) + ' is up and running.')
        cracker = Cracker(self.proxy,self.login,self.passwords,self.passwordsids,str(self.name))
        print('Thread #' + str(self.name) + ' completed.')

passwords_len = None

def ThreadsCreator(proxy,login,passwords,count):
    global passwords_len
    if passwords_len == None:
        passwords_len = PasswordWorker.GetLen(passwords)
    for i in range(1,count+1):
        tempmas = []
        for j in range(i-1,passwords_len,count):
            tempmas.append(j)
        Thread = Threads(proxy, login, passwords,tempmas, i)
        Thread.start()