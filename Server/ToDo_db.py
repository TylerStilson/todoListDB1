import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class TODOdb:
    def __init__(self):
        self.connection = sqlite3.connect("todo.db")
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()
        return

    def getAllTasks(self):
        self.cursor.execute("SELECT * FROM todo")
        todo = self.cursor.fetchall()
        return todo

    def getOneTask(self,task_id):
        data = [task_id]
        self.cursor.execute("SELECT * FROM todo WHERE id = ?", data)
        task = self.cursor.fetchone()
        return task

    def createTask(self, task, priority, assignment, estimate):
        data = [task, priority, assignment, estimate]
        self.cursor.execute("INSERT INTO todo (task, priority, assignment, estimate) VALUES (?,?,?,?)", data)
        self.connection.commit()
        return
        
    def deleteTask(self, task_id):
        data = [task_id]
        self.cursor.execute("DELETE FROM todo WHERE id = ?", data)
        self.connection.commit()
        return

    def updateTask(self, task_id, task_title, task_priority, task_assignment, task_estimate):
        data = [task_title, task_priority, task_assignment, task_estimate, task_id]
        self.cursor.execute("UPDATE todo SET task = ?, priority = ?, assignment = ?, estimate = ? WHERE id = ?", data)
        self.connection.commit()
        return