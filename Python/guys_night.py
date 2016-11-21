import random
import sys
num1 = 0
num2 = 0
count = 0
lst = {'qadir': 0, 'brandon': 0, 'phil': 0, 'dan': 0, 'cam': 0, 'aaron': 0}
lst_name = ['qadir', 'brandon', 'phil', 'dan', 'cam', 'aaron']
num1 = random.randint(0, 5)
num2 = random.randint(0, 5)
print(lst_name[num1], lst_name[num2])
lst[lst_name[num1]] += 1
lst[lst_name[num2]] += 1
while True:
    try:
        min_val = 99
        name = ""
        last = input("Who won?: ")
        lst[last] += 1
        if count % 3 == 0:
            for x in lst_name:
                if lst[x] < min_val:
                    min_val = lst[x]
                    name = x
        else:
            while True:
                num1 = random.randint(0, 5)
                if last != lst_name[num1]:
                    name = lst_name[num1]
                    break
        print("Up next: %s " % name)
        lst[name] += 1
        count += 1
    except KeyboardInterrupt:
        sys.exit()
