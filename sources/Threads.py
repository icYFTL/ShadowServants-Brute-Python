from threading import Thread
from Cracker import Cracker
from PasswordsWorker import PasswordWorker

class Threads(Thread):

    def __init__(self,proxy,login,passwords,startpoint,endpoint):
        Thread.__init__(self)
        self.proxy = proxy
        self.login = login
        self.passwords = passwords
        self.startpoint = startpoint
        self.endpoint = endpoint

    def run(self):
        cracker = Cracker()
        cracker.session_get(self.proxy,self.login,self.passwords,self.startpoint,self.endpoint)

plues = None

def ThreadsCreator(proxy,login,passwords,count):
    global plues
    if plues == None:
        plues = PasswordWorker.GetLen(passwords)
    for i in range(1,count+1):
            Thread = Threads(proxy, login, passwords, plues//count+i,plues//count-i)
            Thread.start()