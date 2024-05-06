from fastapi import FastAPI


app = FastAPI()

n = 10


@app.get('/metrics')
def get_metrics():
    return {
        "instances": n,
        "users": n-2
    }


@app.get('/healthcheck')
def healthcheck():
    return {"Hello": "world"}
