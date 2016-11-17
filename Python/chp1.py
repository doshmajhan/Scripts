
text = "xultpaajcxitltlxaarpjhtiwtgxktghidhipxciwtvgtpilpitghlxiwiwtxgqadds"
base = 'abcdefghijklmnopqrstuvwxyz'

for x in range(1, 27):
    temp = ""
    for i in text:
        temp += base[base.index(i) - x]
    print temp
