import threading
import time
import random

buffer = []
MAX_SIZE = 5

empty = threading.Semaphore(MAX_SIZE)

full = threading.Semaphore(0)

mutex = threading.Lock()

def producer():
    while True:
        item = random.randint(1, 100) 
        
        empty.acquire() 
        mutex.acquire() 
        
        buffer.append(item)
        print(f"Produced: {item} | Buffer: {buffer}")
        
        mutex.release() 
        full.release()  
        
        time.sleep(random.random()) 

def consumer():
    while True:
        full.acquire()  
        mutex.acquire() 
        
        item = buffer.pop(0)
        print(f"Consumed: {item} | Buffer: {buffer}")
        
        mutex.release() 
        empty.release() 
        
        time.sleep(random.random()) 


t1 = threading.Thread(target=producer, daemon=True)
t2 = threading.Thread(target=consumer, daemon=True)

t1.start()
t2.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nStopping...")

