import code as x
import threading
x.create("Siva",21)# Creates the key value pair
x.create("Kumar",22,120)
x.read("Siva")# Returns the key- value pair in the format of JSON object
x.delete("Siva")# Deletes the key value pair
t1=threading.Thread(target=(create or read or delete),args=(key_name,value,timeout))
t1.start()
t1.sleep()
t2=threading.Thread(target=(create or read or delete),args=(key_name,value,timeout))
t2.start()
t2.sleep()
