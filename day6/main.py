import sqlite3
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__, template_folder='templates')

flag = 0

def delete_all_records():
    conn = sqlite3.connect('todos.db')
    c = conn.cursor()
    c.execute("DELETE FROM todos")
    conn.commit()
    conn.close()

def init_db():
    conn = sqlite3.connect('todos.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS todos 
              (id INTEGER PRIMARY KEY AUTOINCREMENT,
              my_id INTEGER NOT NULL,
              task TEXT NOT NULL,
              done INTEGER NOT NULL)""")
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('todos.db')
    c = conn.cursor()
    c.execute("SELECT * FROM todos")
    todos = [{"my_id": row[1], "task": row[2], "done": bool(row[3])} for row in c.fetchall()]
    conn.close()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form['todo']
    conn = sqlite3.connect('todos.db')
    c = conn.cursor()
    c.execute("SELECT MAX(my_id) FROM todos")
    max_id = c.fetchone()[0]

    # if max_id is None:
    #     new_id = 1
    # else:
    #     new_id = max_id + 1

    new_id = max_id + 1 if max_id is not None else 1
    c.execute("INSERT INTO todos (my_id, task, done) VALUES (?, ?, ?)", (new_id, todo, 0))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:index>', methods=['POST', 'GET'])
def edit(index):
    conn = sqlite3.connect('todos.db')
    c = conn.cursor()
    c.execute("SELECT * FROM todos WHERE my_id=?", (index,))
    row = c.fetchone()
    c.close()

    if row is None:
        return "Todo not found"
    todo = {
        "id": row[0],
        "my_id": row[1],
        "task": row[2],
        "done": bool(row[3])
    }

    if request.method == 'POST':
        new_task = request.form['todo']
        conn = sqlite3.connect('todos.db')
        c = conn.cursor()
        c.execute("UPDATE todos SET task=? WHERE my_id=?", (new_task, index))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    else:
        return render_template('edit.html', todo=todo, index=index)

@app.route('/delete/<int:index>')
def delete(index):
    conn = sqlite3.connect('todos.db')
    c = conn.cursor()
    c.execute("DELETE FROM todos WHERE my_id=?", (index,))
    c.execute("UPDATE todos SET my_id=my_id-1 WHERE my_id > ?", (index,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/check/<int:index>')
def check(index):
    conn = sqlite3.connect('todos.db')
    c = conn.cursor()
    c.execute("SELECT * FROM todos WHERE my_id=?", (index,))
    todo = c.fetchone()

    if todo is None:
        conn.close()
        return "Todo not found!"
    
    # todo = dict(c.fetchone())
    new_done = 1 if not todo[3] else 0
    c.execute("UPDATE todos SET done=? WHERE my_id=?", (new_done, index))
    conn.commit()
    conn.close()    
    return redirect(url_for('index'))


if __name__ == "__main__":
    if flag:
        delete_all_records()
    else:    
        init_db()
        app.run(debug=True) #development mode