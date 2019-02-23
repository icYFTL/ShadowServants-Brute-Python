import requests
import os

class PasswordWorker(object):
    def GetRockYou():
        if os.path.exists('./dictionaries/rockyou.txt'):
            print('\n\nHm, nice! You already have rockyou.txt. Let\'s continue.')
            return
        print('\nGetting rockyou.\nPlease stand by...')
        dict = requests.get('https://www.scrapmaker.com/data/wordlists/dictionaries/rockyou.txt')
        print('\nGot it. Wait, I\'ll write it in the file.')
        try:
            os.mkdir('./dictionaries/')
        except OSError:
            pass
        try:
            f = open('./dictionaries/rockyou.txt','w')
            f.write(dict.text)
            f.close()
            print('\nDone it.')
        except:
            print('I can\'t write it.')
            exit()
