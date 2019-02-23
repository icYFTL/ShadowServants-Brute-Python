import requests
import time
from preview import preview
from InputWorker import InputWorker
from ProxyWorker import ProxyWorker
from Cracker import Cracker
import sys


selected_mode = ''
selected_proxy = ''



###### PREVIEW ######

preview.do()

###### Data Input ######

inputs = InputWorker.initializator()
selected_proxy = inputs[0]
pages = inputs[1]

inputs = InputWorker.content_getter()
login = inputs[0]
passwords = inputs[1]

###### WorkOut ######

if selected_proxy == True:
    proxies = ProxyWorker.AutoGrabber(pages)
    cracker = Cracker()
    cracker.session_get(proxies,login,passwords)

elif selected_proxy == False:
    print('Smth went wrong with proxies.\nShutting down.')
    exit()
else:
    proxies = selected_proxy
    cracker = Cracker()
    cracker.session_get(proxies,login,passwords)