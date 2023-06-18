import requests
import time

servers = ["maria.ru", "rose.ru", "sina.ru"]
interval = 60  # Интервал опроса в секундах

while True:
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    for server in servers:
        url = f"http://{server}/api/count"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                count = data["count"]
                print(f"{current_time} {server} {count}")
            else:
                print(f"{current_time} {server} Error: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"{current_time} {server} Error: {e}")
    time.sleep(interval)
