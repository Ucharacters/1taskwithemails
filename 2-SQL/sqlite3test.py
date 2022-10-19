import sqlite3
import time
conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.executescript("""CREATE TABLE IF NOT EXISTS user(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   name TEXT,
   email TEXT);
   """)
conn.commit()

start_time = time.time()
for i in range(10000): 
    cur.executescript("""INSERT INTO user(name, email) VALUES
        ('Иван', '1@1.com');
    """)
    conn.commit()


cur.executescript("""CREATE TABLE IF NOT EXISTS user2(
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   name TEXT,
   email TEXT);
   """)
conn.commit()

cur.executescript("""INSERT INTO user2(id,name, email) SELECT * FROM user;
   """)
conn.commit()
print (time.time()-start_time)

import threading
import time

def myfunc(a, b):
    time.sleep(2.5)
    print('сумма :', a + b)
thr1 = threading.Thread(target = myfunc, args = (1, 2), daemon=True)
thr1.start()
thr1.join(0.125)
if thr1.is_alive():
    print('поток не успел завершиться')
else:
    print('вычисления завершены')



##import asyncio
##async def hello_world():
##    print("Hello World!")
##
##loop = asyncio.get_event_loop()
### Blocking call which returns when the hello_world() coroutine is done
##loop.run_until_complete(hello_world())
##loop.close()

import asyncio

async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)
    from queue import Queue
    queue1 = Queue()
    start_time = time.time()
    for i in range(10000): 
        queue1.put('Python 3')
    for i in range(10000): 
        value = queue1.get()
    print (time.time()-start_time)
    
    return x + y

async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))

loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(1, 2))
loop.close()
