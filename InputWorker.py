from ProxyWorker import ProxyWorker
from PasswordsWorker import PasswordWorker
import os


class InputWorker(object):
    def initializator():
        selected_proxy = ''
        pages = ''
        if os.path.exists('./proxies/last_proxies.txt'):
            selected_proxy = input('Looks like i have already parsed proxy. Use them? y/n: ')
            print('\n')
            selected_proxy.lower()
            while True:
                if (selected_proxy != 'y' and selected_proxy != 'n'):
                    print('[Error]' + 'Bad answers. y/n\n')
                    selected_proxy = input('Looks like i have already parsed proxy. Use them? y/n: ')
                    print('\n')
                    selected_proxy.lower()
                else:
                    break
        if selected_proxy == '' or selected_proxy == 'n':
            try:
                os.remove('./proxies/last_proxies.txt')
            except:
                pass

            selected_proxy = input('Use auto-proxy? y/n: ')
            selected_proxy.lower()
            while (True):
                if (selected_proxy != 'y' and selected_proxy != 'n'):
                    print('[Error]' + 'Bad answers. y/n\n')
                    selected_proxy = input('Use auto-proxy? y/n: ')
                    selected_proxy.lower()
                else:
                    if (selected_proxy == 'y'):
                        selected_proxy = True
                        pages = input('How many proxies do you neeed? (50-70 recommended and 10 < x < 200): ')
                        while True:
                            try:
                                pages = int(pages)
                                if pages < 10 or pages > 200:
                                    raise Exception
                                else:
                                    break
                            except:
                                pages = input('\n\n[ERROR] How many proxies do you neeed? (50-70 recommended and 10 < x < 200): ')

                    else:
                        selected_proxy = False
                    break
            if (selected_proxy == False):
                selected_proxy = input('\nOk. Give me path to the file with proxies.\nOnly .txt allowed.\n\nPath: ')
                while (True):
                    beta = ProxyWorker.handler(selected_proxy)
                    if (beta == False):
                        selected_proxy = input('[Error]' + ' Bad proxies or path.' + '\n\nPath: ')
                    else:
                        selected_proxy = beta
                        break
        if selected_proxy == 'y':
            selected_proxy = './proxies/last_proxies.txt'
            selected_proxy = ProxyWorker.handler(selected_proxy)


        return [selected_proxy,str(pages)]
    def content_getter():
        login = ''
        passwords = ''
        login = input('Give the login: ')
        passwords = input(
            '\nUse rockyou? (I\'ll download it right now.)\nOr you can use your password list.\n\ny-rockyou, n-custom dictionary: ')
        passwords.lower()
        while (True):
            if (passwords != 'y' and passwords != 'n'):
                print('[Error]' + 'Bad answers. y/n\n')
                passwords = input('y-rockyou, n-custom dictionary: ')
                passwords.lower()
            else:
                break
        if passwords == 'y':
            PasswordWorker.GetRockYou()
            passwords = './dictionaries/rockyou.txt'
        if passwords == 'n':
            passwords = input('\nOk. Give me path to the file with passwords.\nOnly .txt allowed.\n\nPath: ')
            while (True):
                if os.path.exists(passwords) == False:
                    passwords = input('[Error]' + ' Bad path.' + '\n\nPath: ')
                else:
                    break

        return [login, passwords]