import sys
import time


class preview(object):
    def do():
        print('[SSBrute]')
        corp = 'by icYFTL\n\n'

        for i in range(len(corp)):
            if (corp[i].isalpha() or corp[i - 1].isalpha() and i != 0):
                sys.stdout.write(corp[i])
                sys.stdout.flush()
                time.sleep(0.2)
            else:
                sys.stdout.write(corp[i])
                sys.stdout.flush()
        print('Available modes: \n1 - BruteMode')
