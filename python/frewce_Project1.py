#Calculates total disk space, and available disk space of the current selected disk. This will default to the main hard drive of whereever the file is saved.
import shutil

total, used, free = shutil.disk_usage("/")

#states the amount of bytes to take total bytes to gigabytes
byteAmount = 2**30

#gives to total amount of GB
print("You have %d GB Total." % (float(total) // (byteAmount)))
print("You have %d GB Used." % (float(used) // (byteAmount)))
print("You have %d GB Free." % (float(free) // (byteAmount)))

#This is just to have a bit of space from the error message
print() 

if free // (byteAmount) < 100:
    print("You should clear up some space!")
else:
    print("You have lots of free space on your hard drive!")
