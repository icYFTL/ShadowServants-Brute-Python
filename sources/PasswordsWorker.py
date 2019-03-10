import requests
import os


class PasswordWorker(object):
    def GetRockYou():
        if os.path.exists('./dictionaries/rockyou.txt'):
            print('\nNice! You already have rockyou.txt. Let\'s continue.')
            return
        print('\nGetting rockyou.\nPlease stand by...')
        try:
            os.mkdir('./dictionaries/')
        except OSError:
            pass
        try:
            f = open('./dictionaries/rockyou.txt', 'w', encoding='utf-8')
            f.write(requests.get('https://www.scrapmaker.com/data/wordlists/dictionaries/rockyou.txt').text)
            f.close()
            print('\nDownloaded and saved into "./dictionaries/rockyou.txt".')
        except Exception as e:
            print('I can\'t write it.')
            print(str(e))
            exit()

    def GetLen(path):
        if os.path.exists(path):
            f = open(path, 'r', encoding='utf-8')
            data = f.readline()
            counter = 0
            while data:
                if data != '' and data != '\n':
                    counter += 1
                data = f.readline()
            f.close()

            return counter
        else:
            return False
