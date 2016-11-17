# Script to monitor integrity of files in a folder
# @author: Cameron Clark
import os
import sys
import sqlite3
import hashlib

# Generate a md5 hash for a given file
def md5(fname):
    hash_md5 = hashlib.md5()
    try:
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
    
        return hash_md5.hexdigest()
    
    except IOError:
        return None

# Scan through the given file path and compare each files md5 hash to the one in the database
def scan(f):
    c = db.cursor()
    file_array = []
    # Need absolute paths
    if os.path.isfile(f):
        file_array = [f]

    elif os.path.isdir(f):
        for root, dirs, files in os.walk(f):
            #print(root)
            file_array += [root + '\\' + fil for fil in files]

    elif f == 'all':
        file_array = ['C:']

    else:
        raise TypeError("File doesn't exists")

    update_array = []
    changed_array = []
    for x in file_array:
        c.execute('SELECT md5 FROM files WHERE file=?', (x,))
        file_hash = c.fetchone()
        if not file_hash:
            update_array += [x]
        else:
            new_hash = md5(x)
            if not new_hash:
                continue
            if new_hash != file_hash[0]:
                c.execute('UPDATE files SET md5=? WHERE file=?', (new_hash, x))
                changed_array += [(x, new_hash)]

    db.commit()
    update_db(update_array, db)
    return changed_array

# Update the database with the new hashes for the changed files
def update_db(f_array, db):
    c = db.cursor()
    file_array = []

    for x in f_array:
        print("Adding %s" % x)
        file_hash = md5(x)
        c.execute('INSERT INTO files VALUES (?, ?)', (x, file_hash))

    db.commit()

# Create our database to store our file names and hashes
def create_db():
    db = sqlite3.connect('files.db')
    c = db.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS files (file text, md5 text, UNIQUE(file))')
    db.commit()
    return db


if __name__ == '__main__':
    if len(sys.argv) > 2:
        print("Usage: integrity.py [file||filepath]")
        sys.exit()

    if len(sys.argv) == 1:
        f = 'all'
    else:
        f = sys.argv[1]

    db = create_db()
    changed = scan(f)
    print("=============")
    print("Changed Files")
    print("=============")
    for x in changed:
        print(x)
