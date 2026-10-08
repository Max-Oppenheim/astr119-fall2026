import requests
import time

url = input("Paste the URL for the website you're poking: ")

#This records the time that it takes for python to download/read the URL for the bytes of the website
def download_time(url):
    start_time = time.perf_counter()
    response = requests.get(url)
    nbytes = len(response.content)
    end_time = time.perf_counter()

    total_time = end_time - start_time
    print(total_time)
   
    return total_time

response = requests.get(url)
nbytes = len(response.content)
num_megabytes = nbytes/1000000
megabytes_per_second = num_megabytes/download_time(url)

download_time(url)

print(f'These are the mbps: {megabytes_per_second}')

print(f'Total time is {download_time(url)}')

print(f"{num_megabytes} megabytes read from {url}")
