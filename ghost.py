#! /usr/bin/python
# Doshmajhan
# Scrape ghostbin
import requests, threading, itertools
import socket, time
ghost="https://ghostbin.com/paste/"

def worker(ext):
    tmp = ghost+ext
    r = requests.get(tmp)
    print "Trying - %s" % ext
    if r.status_code == 200:
        print "FOUND => %s" % ext
        r = requests.get(tmp + "/raw")
        f = open("loot/"+ext, 'w')
        f.write(r.text)
        f.close()


if __name__ == '__main__':
    
    MAX_THREAD = 10
    exts = [''.join(i) for i in itertools.product("abcdefghijklmnopqrstuvwxyz0123456789", repeat=5)]
    i = 0
    for x in exts:
        worker(x)
        """t = threading.Thread(target=worker, args=(x))
        while(i > MAX_THREAD):
            time.sleep(4)
        i+=1
        t.start()"""
