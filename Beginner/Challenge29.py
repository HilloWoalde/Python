import time
bottles = 99
for i in range(bottles,0,-1):
    if(i > 1):
        #time.sleep(1)
        print(str(i) + " bottles of milk on the wall, " + str(i) + " bottles of milk.")
        #time.sleep(2)
        print("Take one down and pass it along, " + str(i) + " bottles of milk on the wall.")
        #time.sleep(1)
    else:
        i = 99
        #time.sleep(1)
        print("1 bottle of milk on the wall, 1 bottle of milk.")
        #time.sleep(1)
        print("Take one down and pass it around, no more bottles of milk on the wall.")
        #time.sleep(1)
        print("No more bottles of milk on the wall, no more bottles of milk.")
        #time.sleep(1)
        print("Go to the store and buy some more, 99 bottles of milk on the wall.")
        time.sleep(3)
