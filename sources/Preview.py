import sys
import time
from ConsoleWorker import ConsoleWorker


class Preview(object):
    def do():
        CLSWork = ConsoleWorker()
        CLSWork.ClearConsole()
        print('[SSBrute] v.1.3.1')
        corp = 'by icYFTL\n\n'

        for i in range(len(corp)):
            if corp[i].isalpha() or corp[i - 1].isalpha() and i != 0:
                sys.stdout.write(corp[i])
                sys.stdout.flush()
                time.sleep(0.2)
            else:
                sys.stdout.write(corp[i])
                sys.stdout.flush()
