from flask import Flask, render_template, request, redirect
from todos import Todo, Todos

app = Flask(__name__)

todos = Todos()

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    title = request.form['todo']
    todos.add(title)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete_todo(id):
    todos.delete(id)
    return redirect('/')

@app.route('/toggle/<int:id>')
def toggle_todo(id):
    todos.toggle(id)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)