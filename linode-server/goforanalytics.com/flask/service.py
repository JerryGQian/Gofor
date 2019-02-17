from flask import Flask
app = Flask(__name__)
@app.route("/")
def dat():
    return "Data is yum."

if __name__ == "__main__":
    app.run()
