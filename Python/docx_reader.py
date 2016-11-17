"""
    Program to convert a word document to a mp3 file
    @author: Doshmajhan
"""
from gtts import gTTS
import docx
import os
import sys

# Convert word document to mp3
def convert_doc(f):
    print("[*] Converting...")
    path = os.path.join(sys.path[0], '%s.mp3' % str(f))
    doc = docx.Document(f)
    text = []
    for p in doc.paragraphs:
        text.append(p.text)
    text = '.'.join(x for x in text)
    text = text.encode('utf-8').decode('ascii', "ignore")
    tts = gTTS(text=text, lang='en')
    tts.save(path)
    print("[*] Done")
    return path

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: docx_reader [file]")
    path = convert_doc(sys.argv[1])
    print("[*] The MP4 is located in %s" % path)
    sys.exit(0)
