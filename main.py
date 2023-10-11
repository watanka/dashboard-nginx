from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from domain.question import question_router
from domain.answer import answer_router

app = FastAPI(
    title = 'dashboard',
    description = 'simple dashboard copying pybo from "Jump to FastAPI"'
)

origins = [
    'http://127.0.0.1:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)

@app.get('/ping')
def pingpong() :
    return {'ping' : 'pong'}


app.include_router(question_router.router)
app.include_router(answer_router.router)

if __name__ == '__main__' : 
    app.run()