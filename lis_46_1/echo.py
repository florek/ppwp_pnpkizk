from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def echo():
    return (
        f"METODA: {request.method}\n"
        f"NAGŁÓWKI:\n{request.headers}"
        f"TREŚĆ:\n{request.data.decode()}"
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0")
