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


@app.get('/loaderio-ec469e1dfeec45c4c99c121fbf333c99')
def loaderio_test():
    return """
    loaderio-ec469e1dfeec45c4c99c121fbf333c99

    """
