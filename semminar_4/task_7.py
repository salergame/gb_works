import random
import time
import concurrent.futures
import asyncio

arr = [random.randint(1, 100) for _ in range(1000000)]

def multi_threaded_sum(arr):
    start_time = time.time()
    total_sum = sum(arr)
    end_time = time.time()
    return total_sum, end_time - start_time

def multi_process_sum(arr):
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        total_sum = sum(executor.map(sum, [arr[i::10] for i in range(10)]))
    end_time = time.time()
    return total_sum, end_time - start_time

async def async_sum(arr):
    total_sum = sum(arr)
    return total_sum

async def async_main(arr):
    start_time = time.time()
    total_sum = await async_sum(arr)
    end_time = time.time()
    return total_sum, end_time - start_time

def main():
    print("Multi-threaded sum:")
    total_sum, time_taken = multi_threaded_sum(arr)
    print(f"Total sum: {total_sum}, Time taken: {time_taken:.4f} seconds")

    print("\nMulti-process sum:")
    total_sum, time_taken = multi_process_sum(arr)
    print(f"Total sum: {total_sum}, Time taken: {time_taken:.4f} seconds")

    print("\nAsync sum:")
    loop = asyncio.get_event_loop()
    total_sum, time_taken = loop.run_until_complete(async_main(arr))
    print(f"Total sum: {total_sum}, Time taken: {time_taken:.4f} seconds")

if __name__ == "__main__":
    main()
