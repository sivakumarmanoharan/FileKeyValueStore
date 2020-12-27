import threading
from threading import *
import time
dict={}
def create(key,value,timeout=0):
    if key in dict:
        print("Key already exists!!")
    else:
        if key.isalpha():
            if len(dict)<(1024*1020*1024) and value<=(16*1024*1024): # To specify the max file size limit of 1GB
                    if timeout==0:
                        l=[value,timeout]
                    else:
                        l=[value,time.time()+timeout]
                    if len(key)<32:# To cap the string at 32 chars
                        dict[key]=l
            else:
                print("Memory limit exceeded!!")
        else:
            print("Key must contain alphabets only!!")
def read(key):
    if key not in dict:
        print("Key not present!")
    else:
        b=dict[key]
        if b[1]!=0:
            if time.time()<b[1]:
                stri=str(key)+":"+str(b[0])
                return stri
            else:
                print("Time to live for the key expired!!")
        else:
            stri=str(key)+":"+str(b[0])
            return stri
def delete(key):
    if key not in dict:
        print("Key not present!")
    else:
        b=dict[key]
        if b[1]!=0:
            if time.time()<b[1]:
                del dict[key]
                print("Key is successfully deleted")
            else:
                print("Time to live for the key expired!!")
        else:
            del dict[key]
            print("Key is successfully deleted")
