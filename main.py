from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/")
async def root():
    return HTMLResponse(content='<h1>Hello world</h1>')

@app.get("/my-branch")
async def root():
    return HTMLResponse(content='<h1>Hello my-branch!</h1>')
