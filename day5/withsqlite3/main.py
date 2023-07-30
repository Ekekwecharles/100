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
              task TEXT NOT NULL,
              done INTEGER NOT NULL)""")
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('todos.db')
    c = conn.cursor()
    c.execute("SELECT * FROM todos")
    todos = [{"id": row[0], "task": row[1], "done": bool(row[2])} for row in c.fetchall()]
    conn.close()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form['todo']
    conn = sqlite3.connect('todos.db')
    c = conn.cursor()
    c.execute("INSERT INTO todos (task, done) VALUES (?, ?)", (todo, 0))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:index>', methods=['POST', 'GET'])
def edit(index):
    conn = sqlite3.connect('todos.db')
    c = conn.cursor()
    c.execute("SELECT * FROM todos WHERE id=?", (index,))
    todo = dict(c.fetchone())
    c.close()

    if request.method == 'POST':
        new_task = request.form['todo']
        conn = sqlite3.connect('todos.db')
        c = conn.cursor()
        c.execute("UPDATE todos SET task=? WHERE id=?", (new_task, index))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    else:
        return render_template('edit.html', todo=todo, index=index)

@app.route('/delete/<int:index>')
def delete(index):
    conn = sqlite3.connect('todos.db')
    c = conn.cursor()
    c.execute("DELETE FROM todos WHERE id=?", (index,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/check/<int:index>')
def check(index):
    conn = sqlite3.connect('todos.db')
    c = conn.cursor()
    c.execute("SELECT * FROM todos WHERE id=?", (index,))
    todo = c.fetchone()

    if todo is None:
        conn.close()
        return "Todo not found!"
    
    # todo = dict(c.fetchone())
    new_done = 1 if not todo[2] else 0
    c.execute("UPDATE todos SET done=? WHERE id=?", (new_done, index))
    conn.commit()
    conn.close()    
    return redirect(url_for('index'))


if __name__ == "__main__":
    if flag:
        delete_all_records()
    else:    
        init_db()
        app.run(debug=True) #development mode