import asyncio

async def generate():
    import random
    while True:
        await asyncio.sleep(2)
        yield random.randint(1, 10)

async def consume(generator):
    while True:
        num = await generator
        print(num)

async def gui():
    import tkinter as tk 
    root = tk.Tk()
    canvas = tk.Canvas(root, width = 300, height = 300)      
    canvas.grid(column = 0, row = 0, columnspan = 2)
    canvas.create_line(10, 20, 300, 50)

    btn = tk.Button(root, text = "yas queen", command = None)
    btn.grid(column = 0, row = 1)
    btn = tk.Button(root, text = "yuck", command = None)
    btn.grid(column = 1, row = 1)

    while True:
        root.update()
        await asyncio.sleep(1/20)

loop = asyncio.get_event_loop()
# loop.create_task(gui())
generator = loop.create_task(generate())
loop.create_task(consume(generator))
loop.run_forever()