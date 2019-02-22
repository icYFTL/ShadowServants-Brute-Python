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
selected_mode = inputs[0]
selected_proxy = inputs[1]

###### WorkOut ######

if selected_proxy == True:
    proxies = ProxyWorker.AutoGrabber()

    cracker = Cracker()
    cracker.session_get(proxies)
