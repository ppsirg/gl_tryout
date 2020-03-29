"""
Functionality:
What is the problem in the following code?
- answer: total variable is not thread-safe, so its value is not totally realiable
How do you solve it?
- answer: using asyncio to make total be updated in a safe way, or if is not possible, 
at least dont modify total variable outside the main thread or use primitive syncronization
such a Lock
Will it happen the same problem using processes instead of threads. Why?
- answer: with processes there is a different problem, new process with current total value
will be created, at return, its modifications will not be available
"""

import ​ threading
import ​ time
import ​ random

total = 0

def ​ update_total(amount, delay):
    global total
    total0 = total
    time.sleep(delay)
    total = total0 + amount

threads = []

transactions = [2, 100, 20, 300, 400, 250, 15, 89]

for ​ amount ​ in ​ transactions:
    mythread = ​ threading.Thread​ (target=update_total,
        args=[amount, random.randint(3, 6)])
    mythread.start()
    threads.append(mythread)

for ​ t ​ in ​ threads:
    t.join()

print​ (sum(transactions), total)

