from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/hello/{name}")
def read_item(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/docker/resources")
def read_resources():
    return {"message": ["https://courses.devopsdirective.com/docker-beginner-to-pro","https://docs.docker.com/","https://docs.docker.com/get-started/",]}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)