import sys
sys.path.append("./sources/")

from Preview import Preview
from InputWorker import InputWorker
from ProxyWorker import ProxyWorker
import Threads



###### PREVIEW ######

Preview.do()


###### DATA INPUT ######

inputs = InputWorker.initializator()
selected_proxy = inputs[0]
pages = inputs[1]
login = inputs[2]
passwords = inputs[3]
threadcount = inputs[4]

###### WORKOUT ######

if selected_proxy == True:
    proxies = ProxyWorker.AutoGrabber(pages)
    Threads.ThreadsCreator(proxies,login,passwords,threadcount)


elif selected_proxy == False:
    print('[Error] Something went wrong with proxies.\n\nShutting down...')
    exit(-9)
else:
    proxies = selected_proxy
    Threads.ThreadsCreator(proxies, login, passwords, threadcount)
