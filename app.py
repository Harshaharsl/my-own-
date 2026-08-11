from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Employee Management Application"

@app.route("/employees")
def employees():
    return "Employee List"

@app.route("/health")
def health():
    return "Application is healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
