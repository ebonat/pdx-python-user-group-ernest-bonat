import asyncio
# import resquest 

async def show_message1(message):
    print(message)
    
async def show_message2(message):
    print(message)    
    
async def slow_operation(n):
    await asyncio.sleep(n)
    print("Slow operation {} complete".format(n))    
    
async def main2():
    tasks = [asyncio.Task(slow_operation(5)), asyncio.Task(slow_operation(2)), asyncio.Task(slow_operation(4)), asyncio.Task(slow_operation(1)), asyncio.Task(slow_operation(3))]
    await asyncio.wait(tasks)    
    
async def main3():
    tasks1 = [asyncio.Task(show_message1("show_message1"))]
    await asyncio.wait(tasks1)    
    tasks2 = [asyncio.Task(slow_operation(2)), asyncio.Task(slow_operation(4)), asyncio.Task(slow_operation(3))]
    await asyncio.wait(tasks2)    
    tasks3 = [asyncio.Task(show_message2("show_message2"))]
    await asyncio.wait(tasks3)    
     
# async def main1():
#     await asyncio.wait([
#         slow_operation(2),
#         slow_operation(4),
#         slow_operation(3),
#         slow_operation(5),
#         slow_operation(1),
#     ])
# 
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main1())
#     loop.close()

if __name__ == '__main__':
#     show_message1("1")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main3())
    loop.close()
#     show_message1("2")
    

# if __name__ == "__main__":
#     show_message1("1")
#     tasks = [asyncio.Task(slow_operation(2)), 
#              asyncio.Task(slow_operation(4)), 
#              asyncio.Task(slow_operation(3))]
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait(tasks))
#     loop.close()
#     show_message2("2")