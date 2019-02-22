from ProxyWorker import ProxyWorker

class InputWorker(object):
    def initializator():
        selected_mode = input('\n\nSelect mode: ')

        while (True):
            if (selected_mode != '1'):
                print('[Error]' + 'Bad mode selected\n')
                selected_mode = input('Select mode: ')
            else:
                break

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
                    print('By the way. Default count of grubbing proxies is about 100. You can\'t change it. Now.')
                else:
                    selected_proxy = False
                break
        if (selected_proxy == False):
            selected_proxy = input('\nOk. Give me path to the file with proxies.\nOnly .txt allowed.\n\nPath: ')
            temp = ProxyWorker()
            while (True):
                beta = temp.handler(path=selected_proxy)
                if (beta == False):
                    selected_proxy = input('[Error]' + ' Bad proxies or path.' + '\n\nPath: ')
                else:
                    selected_proxy = beta
                    break
        return [selected_mode, selected_proxy]
