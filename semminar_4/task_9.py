import os
import requests
import time
import concurrent.futures
import asyncio

def download_image(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            image_name = url.split('/')[-1]
            with open(image_name, 'wb') as f:
                f.write(response.content)
            return image_name
        else:
            return None
    except Exception as e:
        print(f"Error downloading image from {url}: {e}")
        return None

def multi_threaded_download(urls):
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(download_image, urls))
    end_time = time.time()
    return results, end_time - start_time

def multi_process_download(urls):
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(download_image, urls))
    end_time = time.time()
    return results, end_time - start_time

async def async_download(url):
    return download_image(url)

async def async_main(urls):
    start_time = time.time()
    tasks = [async_download(url) for url in urls]
    results = await asyncio.gather(*tasks)
    end_time = time.time()
    return results, end_time - start_time

def print_results(results, total_time):
    for result in results:
        if result:
            print(f"Downloaded: {result}")
    print(f"Total time: {total_time:.2f} seconds")

def main():
    urls = [
        'https://example.com/images/image1.jpg',
        'https://example.com/images/image2.jpg',
        'https://example.com/images/image3.jpg',
    ]

    print("Multi-threaded download:")
    results, total_time = multi_threaded_download(urls)
    print_results(results, total_time)

    print("\nMulti-process download:")
    results, total_time = multi_process_download(urls)
    print_results(results, total_time)

    print("\nAsync download:")
    loop = asyncio.get_event_loop()
    results, total_time = loop.run_until_complete(async_main(urls))
    print_results(results, total_time)

if __name__ == "__main__":
    main()
