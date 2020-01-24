from multiprocessing import Pool as ProcessPool
from multiprocessing.dummy import Pool as ThreadPool
import requests
# Парсинг

def get_html(url):
    requests.get(url)


urls = [
    'http://google.com',
    'http://yandex.ru'
] * 10



if __name__ == '__main__':
    processPool = ProcessPool(4)
    processPool.map(get_html, urls)  # медленей
    threadPool = ThreadPool(4)  # быстрей
