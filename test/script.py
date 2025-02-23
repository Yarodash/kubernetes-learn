import os
import time
from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import threading
import uvicorn
import random

app = FastAPI()
directory = os.environ.get("DIRECTORY", "./mount-test-dir")

random_text = "".join([chr(random.randint(65, 90)) for _ in range(10)])

def append_random_text():
    while True:
        with open(os.path.join(directory, 'file.txt'), 'r') as f:
            content = f.read()

        new_content = content + f"{datetime.now()} - {random_text}\n"
        new_content = new_content[-200:]

        with open(os.path.join(directory, 'file.txt'), 'w') as f:
            f.write(new_content)
        
        time.sleep(3)

@app.get("/file")
def list_files():
    with open(os.path.join(directory, 'file.txt'), 'r') as f:
        content = f.read()
    return JSONResponse(content={"file_content": content, "whoami": random_text})

@app.post('/clear')
def clear_files():
    for file in os.listdir(directory):
        os.remove(os.path.join(directory, file))
    return JSONResponse(content={"message": "Files cleared"})

if __name__ == "__main__":
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist")
        exit(1)

    threading.Thread(target=append_random_text, daemon=True).start()
    uvicorn.run(app, host="0.0.0.0", port=8000)
