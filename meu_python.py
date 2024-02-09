from flask import Flask

app = Flask(__name__)


a = 3
b = 2

c = a + b

print("olá mundo: ", c)


print("olá mundo 4: ", c)
























@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    app.run()
