import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, QInputDialog, QMessageBox

class TodoList(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.load_tasks()

    def initUI(self):
        self.setWindowTitle('To-Do List App')
        self.setGeometry(100, 100, 400, 300)

        main_layout = QVBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setStyleSheet("QLineEdit { border-radius: 10px; padding: 6px; }")
        main_layout.addWidget(self.input_field)

        buttons_layout = QHBoxLayout()

        self.add_button = QPushButton('ADD')
        self.add_button.setStyleSheet("QPushButton { background-color: yellow; border-radius: 15px; padding: 10px; margin: 5px; }")
        self.delete_button = QPushButton('DELETE')
        self.delete_button.setStyleSheet("QPushButton { background-color: yellow; border-radius: 15px; padding: 10px; margin: 5px; }")
        self.edit_button = QPushButton('EDIT')
        self.edit_button.setStyleSheet("QPushButton { background-color: yellow; border-radius: 15px; padding: 10px; margin: 5px; }")
        self.save_button = QPushButton('Save Task')
        self.save_button.setStyleSheet("QPushButton { background-color: yellow; border-radius: 15px; padding: 10px; margin: 5px; }")

        buttons_layout.addWidget(self.add_button)
        buttons_layout.addStretch()  
        buttons_layout.addWidget(self.delete_button)
        buttons_layout.addStretch()  
        buttons_layout.addWidget(self.edit_button)
        buttons_layout.addStretch() 
        buttons_layout.addWidget(self.save_button)

        main_layout.addLayout(buttons_layout)

        self.task_list = QListWidget()
        main_layout.addWidget(self.task_list)
        self.setLayout(main_layout)

        self.add_button.clicked.connect(self.add_task)
        self.delete_button.clicked.connect(self.delete_task)
        self.edit_button.clicked.connect(self.edit_task)
        self.save_button.clicked.connect(self.save_tasks)

    def add_task(self):
        task = self.input_field.text()
        if task:
            self.task_list.addItem(task)
            self.input_field.clear()

    def delete_task(self):
        selected_items = self.task_list.selectedItems()
        if not selected_items:
            return
        for item in selected_items:
            self.task_list.takeItem(self.task_list.row(item))

    def edit_task(self):
        selected_item = self.task_list.currentItem()
        if not selected_item:
            return
        text, ok = QInputDialog.getText(self, 'Edit Task', 'Edit the selected task:', QLineEdit.Normal, selected_item.text())
        if ok and text:
            selected_item.setText(text)

    def save_tasks(self):
        tasks = []
        for index in range(self.task_list.count()):
            tasks.append(self.task_list.item(index).text())
        with open('tasks.txt', 'w') as file:
            for task in tasks:
                file.write(task + '\n')
        self.show_message('Tasks Saved', 'Your tasks have been successfully saved.')

    def show_message(self, title, message):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec_()

    def load_tasks(self):
        try:
            with open('tasks.txt', 'r') as file:
                tasks = file.readlines()
            self.task_list.clear()
            for task in tasks:
                self.task_list.addItem(task.strip())
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TodoList()
    ex.show()
    sys.exit(app.exec_())
