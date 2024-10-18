import serial
import asyncio
import time

ser = serial.Serial('/dev/ttyS9', 115200)

async def data_write(resp):
    with open('uart_log.txt', 'a+') as file:
        named_tuple = time.localtime()
        timestamp = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
        data = f"INFO {timestamp}   Received data: {resp.decode('utf-8', errors='ignore')}\n"
        file.write(data)


async def main():
    while True:
        if ser.in_waiting > 0:
            resp = ser.read(ser.in_waiting)
            save_task = asyncio.create_task(data_write(resp))
            await save_task

if __name__ == '__main__':
    asyncio.run(main())
