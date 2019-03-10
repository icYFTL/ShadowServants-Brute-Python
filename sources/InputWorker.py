from ProxyWorker import ProxyWorker
from PasswordsWorker import PasswordWorker
import os


class InputWorker(object):
    def initializator():
        try:
            selected_proxy = None
            pages = None

            if os.path.exists('./proxies/last_proxies.txt'):
                selected_proxy = input('Looks like i have already parsed proxy. Use them? y/n: ')
                selected_proxy.lower()
                while True:
                    if selected_proxy != 'y' and selected_proxy != 'n':
                        print('[Error]' + 'Bad answers. y/n\n')
                        selected_proxy = input('Looks like i have already parsed proxy. Use them? y/n: ')
                        selected_proxy.lower()
                    else:
                        break
            if selected_proxy is None or selected_proxy is 'n':
                try:
                    os.remove('./proxies/last_proxies.txt')
                except:
                    pass

                selected_proxy = input('Use auto-proxy? y/n: ')
                selected_proxy.lower()
                while True:
                    if selected_proxy != 'y' and selected_proxy != 'n':
                        print('[Error]' + 'Bad answers. y/n\n')
                        selected_proxy = input('Use auto-proxy? y/n: ')
                        selected_proxy.lower()
                    else:
                        if selected_proxy is 'y':
                            selected_proxy = True
                            pages = input('How many proxies do you need? (600-700 recommended and 10 < x < 10000): ')
                            while True:
                                try:
                                    pages = int(pages)
                                    if pages < 10 or pages > 10000:
                                        raise Exception
                                    else:
                                        break
                                except:
                                    pages = input(
                                        '\n\n[ERROR] How many proxies do you need? (600-700 recommended and 10 < x < 10000): ')
                        else:
                            selected_proxy = False
                        break

                if selected_proxy is False:
                    selected_proxy = input('\nOk. Give me path to the file with proxies.\nOnly .txt allowed.\n\nPath: ')
                    while True:
                        beta = ProxyWorker.handler(selected_proxy)
                        if beta is False:
                            selected_proxy = input('[Error]' + ' Bad proxies or path.' + '\n\nPath: ')
                        else:
                            selected_proxy = beta
                            break

            if selected_proxy is 'y':
                selected_proxy = './proxies/last_proxies.txt'
                selected_proxy = ProxyWorker.handler(selected_proxy)

            login = input('\nGive me the login, which will be bruted: ')
            while True:
                if len(login) < 1:
                    print('[Error] Bad login len.')
                    login = input('\nGive me the login, which will be bruted: ')
                else:
                    break
            passwords = input(
                '\nUse rockyou? (I\'ll download it right now.)\nOr you can use your password list.\n\ny-rockyou, n-custom dictionary: ')
            passwords.lower()
            while True:
                if passwords != 'y' and passwords != 'n':
                    print('[Error]' + 'Bad answers. y/n\n')
                    passwords = input('y - [rockyou], n - [custom dictionary]: ')
                    passwords.lower()
                else:
                    break
            if passwords is 'y':
                PasswordWorker.GetRockYou()
                passwords = './dictionaries/rockyou.txt'
            if passwords is 'n':
                passwords = input('\nOk. Give me path to the file with passwords.\nOnly .txt allowed.\n\nPath: ')
                while True:
                    if os.path.exists(passwords) is False:
                        passwords = input('[Error]' + ' Bad path.' + '\n\nPath: ')
                    else:
                        break

            threadcount = input('\nHow many threads do you want? (1 < x < 50): ')
            while True:
                try:
                    threadcount = int(threadcount)
                    if threadcount > 50 or threadcount < 1:
                        threadcount = input(
                            '[Error] Invalid threads count. (1 < x < 50)\n\nHow many threads do you want?: ')
                    else:
                        break
                except:
                    threadcount = input('[Error] Invalid threads count. (1 < x < 50)\n\nHow many threads do you want?: ')
            return [selected_proxy, pages, login, passwords, threadcount]

        except KeyboardInterrupt:
            print('\nShutting down...')
            exit(-9)
