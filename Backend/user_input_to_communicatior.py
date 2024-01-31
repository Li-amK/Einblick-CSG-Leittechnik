# sieht nach wenig aus, aber diese Datei ist zum testen gold wert.

import asyncio

from gateway_communicator import write


async def main():
    while True:
        group_value = input("Gruppenadresse: ")
        value = input("Value: ")
        value_int = int(value)
        await write(group_value, value_int)


asyncio.run(main())
