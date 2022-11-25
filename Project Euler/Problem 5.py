import time
a = 2520
b = False 
start_time = time.time()
r =(3,4,5,6,7,11,13,16,17,18,19)

while b is False:
    str(a)
    for i in r:
        if a % i==0:
            b = True
            continue
        else:
            b = False
            break
    a += 40



print("--- %s seconds ---" % (time.time() - start_time))
print(a-40)


