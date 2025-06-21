import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QListWidget, QPushButton, QLineEdit, QMessageBox, QListWidgetItem
)
from PyQt5.QtCore import Qt
from pymongo import MongoClient

# MongoDB setup
client = MongoClient("mongodb+srv://sewlesew:sewlesew1219@mycluster.q4ok5hq.mongodb.net/")
db = client["todo_app"]
tasks_col = db["tasks"]

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My To-Dos")
        self.setGeometry(200, 200, 400, 450)
        self.init_ui()
        self.load_tasks()

    def init_ui(self):
        layout = QVBoxLayout()

        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter a new task...")
        self.task_input.setClearButtonEnabled(True)
        self.task_input.setFocus()
        self.task_input.setFixedHeight(40)

        # ✅ Combine styles in a single call
        self.task_input.setStyleSheet("""
            QLineEdit {
                font-size: 16px;
                padding: 10px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
        """)

        layout.addWidget(self.task_input)


        add_button = QPushButton("Add Task")
        add_button.clicked.connect(self.add_task)
        layout.addWidget(add_button)

        self.task_list = QListWidget()
        self.task_list.itemDoubleClicked.connect(self.toggle_task_done)
        layout.addWidget(self.task_list)

        btn_layout = QHBoxLayout()

        delete_button = QPushButton("Delete Selected")
        delete_button.clicked.connect(self.delete_selected)

        clear_button = QPushButton("Clear All")
        clear_button.clicked.connect(self.clear_all)

        btn_layout.addWidget(delete_button)
        btn_layout.addWidget(clear_button)

        layout.addLayout(btn_layout)
        self.setLayout(layout)

    def load_tasks(self):
        """Load tasks from MongoDB into the list widget."""
        self.task_list.clear()
        for task in tasks_col.find():
            item = QListWidgetItem(task["text"])
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Checked if task.get("done") else Qt.Unchecked)
            font = item.font()
            font.setStrikeOut(task.get("done", False))
            item.setFont(font)
            self.task_list.addItem(item)

    def add_task(self):
        task_text = self.task_input.text().strip()
        if not task_text:
            QMessageBox.warning(self, "Empty Task", "Please enter a task.")
            return

        tasks_col.insert_one({"text": task_text, "done": False})
        self.task_input.clear()
        self.load_tasks()

    def toggle_task_done(self, item):
        task_text = item.text()
        new_done = item.checkState() == Qt.Unchecked
        tasks_col.update_one({"text": task_text}, {"$set": {"done": new_done}})
        self.load_tasks()

    def delete_selected(self):
        selected_items = self.task_list.selectedItems()
        if not selected_items:
            QMessageBox.information(self, "No Selection", "Select a task to delete.")
            return
        for item in selected_items:
            tasks_col.delete_one({"text": item.text()})
        self.load_tasks()

    def clear_all(self):
        reply = QMessageBox.question(self, "Clear All", "Are you sure you want to clear all tasks?")
        if reply == QMessageBox.Yes:
            tasks_col.delete_many({})
            self.load_tasks()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())
