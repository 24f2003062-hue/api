from fastapi import FastAPI, Request


app = FastAPI()



@app.post("/")
def read_root();
    return{"message": "Hello, World!"}

    
