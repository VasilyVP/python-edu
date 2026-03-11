import asyncio
from time import sleep


def test():
    sleep(2)  # Simulate a time-consuming task
    return "Test function completed."



async def main():
    # Run two async tasks concurrently
    [result1, _] = await asyncio.gather(
        asyncio.to_thread(test),
        asyncio.to_thread(lambda: print("Another task completed.")),
    )
    print(result1)


if __name__ == "__main__":
    asyncio.run(main())
