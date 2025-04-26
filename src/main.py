import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def get_user():
    return {
        'user': 'user'
    }


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)