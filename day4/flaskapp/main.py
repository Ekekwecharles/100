from flask import Flask, render_template, request, url_for
import json
from todo_funcs import *

app = Flask(__name__, template_folder="templates")


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks_data = []
        
    return tasks_data


@app.route("/")
def index():
    tasks = load_tasks()
    return render_template("index.html", todos=tasks)


@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("todo")
    if task:
        add_task(task)
    return index()


@app.route("/delete/<int:_index>")
def delete(_index):
    remove_task(_index)
    return index()


if __name__ == "__main__":
    app.run(debug=True)
