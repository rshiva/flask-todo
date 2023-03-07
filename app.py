from flask import Flask, render_template, redirect, request

app = Flask(__name__)

store_data=[]

@app.route("/", methods=['GET'])
def index():
    records = store_data
    return render_template('index.html',**locals())

@app.route("/tasks", methods=['POST'])
def create():
  if request.method == "POST":
    store_data.append(request.form["task"])
    records = store_data
    return redirect("/")


if __name__ == "__main__":
    app.run(port=8001,debug=True)