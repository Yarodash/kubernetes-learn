import requests
import time
import threading

url = "http://localhost:30001/file"

results = {}

def show_results():
    while True:
        print(results)
        time.sleep(1)

show_results_thread = threading.Thread(target=show_results, daemon=True)
show_results_thread.start()

while True:
    try:
        response = requests.get(url)
        data = response.json()
        whoami = data.get('whoami')
        results[whoami] = results.get(whoami, 0) + 1
    except Exception as e:
        print(f"An error occurred: {e}")
