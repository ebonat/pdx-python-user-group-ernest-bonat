import time
import threading
import asyncio

# @asyncio.coroutine
# def slow_operation_asyncio(n):
#     yield from asyncio.sleep(n)
#     print("Slow operation {} complete".format(n))  
  
async def slow_operation_asyncio(n):
    await asyncio.sleep(n)
    print("Slow operation {} complete".format(n))    

# # async function
# async def main_asyncio():
#     tasks = [asyncio.Task(slow_operation_asyncio(5)), asyncio.Task(slow_operation_asyncio(2)), asyncio.Task(slow_operation_asyncio(4)), asyncio.Task(slow_operation_asyncio(1)), asyncio.Task(slow_operation_asyncio(3))]
#     await asyncio.wait(tasks)    

# async function
async def main_asyncio():
#     slow_operation_sleep(5)
    tasks1 = [asyncio.Task(slow_operation_asyncio(5))]
    await asyncio.wait(tasks1)  
    tasks2 = [asyncio.Task(slow_operation_asyncio(2)), asyncio.Task(slow_operation_asyncio(4)), asyncio.Task(slow_operation_asyncio(1)), asyncio.Task(slow_operation_asyncio(3))]
    await asyncio.wait(tasks2)    
    
def slow_operation_sleep(n):
    time.sleep(n)
    print("Slow operation {} complete".format(n))    

# concurrent function
def main_sleep():
    slow_operation_sleep(5)
    slow_operation_sleep(2)
    slow_operation_sleep(4)
    slow_operation_sleep(1)
    slow_operation_sleep(3)
            
if __name__ == '__main__':
    start_time = time.time()         
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_asyncio())
    loop.close()             
    end_time = time.time()
    elapse_time = end_time - start_time
    print("Program Runtime: " + str(round(elapse_time, 2)) + " seconds" + "\n")

# if __name__ == '__main__':
#     start_time = time.time()    
#     main_sleep()        
#     end_time = time.time()
#     elapse_time = end_time - start_time
#     print("Program Runtime: " + str(round(elapse_time, 2)) + " seconds" + "\n")    

# if __name__ == '__main__':
#     start_time = time.time()        
#     thread_5 = threading.Thread(target = slow_operation_sleep , args = (5,))
#     thread_2 = threading.Thread(target = slow_operation_sleep , args = (2,))
#     thread_4 = threading.Thread(target = slow_operation_sleep , args = (4,))
#     thread_1 = threading.Thread(target = slow_operation_sleep , args = (1,))
#     thread_3 = threading.Thread(target = slow_operation_sleep , args = (3,))    
#     thread_5.start()
#     thread_2.start()
#     thread_4.start()
#     thread_1.start()
#     thread_3.start()
#     thread_5.join()
#     thread_2.join()
#     thread_4.join()
#     thread_1.join()
#     thread_3.join()         
#     end_time = time.time()
#     elapse_time = end_time - start_time
#     print("Program Runtime: " + str(round(elapse_time, 2)) + " seconds" + "\n")    

