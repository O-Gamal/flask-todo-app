class Todo:
    id = 0
    def __init__(self, title, is_done=False):
        self.id = Todo.id
        self.title = title
        self.is_done = is_done
        Todo.id += 1

    def toggle (self):
        self.is_done = not self.is_done

    def __repr__(self):
        return f'{self.title}'


class Todos:
    def __init__(self):
        self.todos = []

    def add(self, title):
        self.todos.append(Todo(title))

    def delete(self, id):
        for todo in self.todos:
            if todo.id == id:
                self.todos.remove(todo)
                break

    def toggle(self, id):
        for todo in self.todos:
            if todo.id == id:
                todo.toggle()
                break

    def __len__(self):
      return len(self.todos)

    def __iter__(self):
      return iter(self.todos)

    def __repr__(self):
        return self.todos


