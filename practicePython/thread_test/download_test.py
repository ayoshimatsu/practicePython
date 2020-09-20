from hashlib import md5
from pathlib import Path
from urllib import request
from concurrent.futures import (ThreadPoolExecutor, as_completed)
from ..my_decorator import decorator as deco

urls = ["https://twitter.com",
        "https://facebook.com",
        "https://instagram.com"]

def download(url):
    req = request.Request(url)
    name = md5(url.encode("utf-8")).hexdigest()
    file_path = "../garbage/" + name
    with request.urlopen(req) as res:
        Path(file_path).write_bytes(res.read())
        return url, file_path

@deco.elapsed_time
def get_sequential():
    for url in urls:
        print(download(url))

@deco.elapsed_time
def get_multi_thread():
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(download, url) for url in urls]
        for futures in as_completed(futures):
            print(futures.result())


#get_sequential()
get_multi_thread()
