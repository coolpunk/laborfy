import uvicorn


if __name__ == '__main__':
    uvicorn.run("src.handlers:app", port=8000, reload=True)
