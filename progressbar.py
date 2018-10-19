"""
EXEMPLE D'UTILISATION
=====================
import time

from progressbar import progress

total = 10
i = 0
while i < total:
    i += 1
    progress(i, total, status="test")
    time.sleep(0.5)
print('')
"""
import sys


def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s | %s\r' % (bar, percents, '%', status))
    sys.stdout.flush()


def main():
    import time
    import os

    from progressbar import progress

    os.system("title progressbar.py")

    print("Progress Bar Demo :")

    total = 10
    i = 0
    while i < total:
        i += 1
        progress(i, total, status="test")
        time.sleep(0.5)
    print('')
    print('Finish')
    os.system("pause")


if __name__ == '__main__':
    main()
