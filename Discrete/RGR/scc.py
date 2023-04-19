import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QCheckBox

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.adj_matrix = None
        self.components = None

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Strongly Connected Components')

        layout = QGridLayout()
        self.setLayout(layout)

        size_label = QLabel('Size:')
        layout.addWidget(size_label, 0, 0)

        self.size_input = QLineEdit()
        layout.addWidget(self.size_input, 0, 1)

        load_button = QPushButton('Load')
        load_button.clicked.connect(self.on_load_click)
        layout.addWidget(load_button, 0, 2)

        self.find_button = QPushButton('Find Components')
        self.find_button.setEnabled(False)
        self.find_button.clicked.connect(self.on_find_click)
        layout.addWidget(self.find_button, 1, 0, 1, 3)

        self.result_label = QLabel('')
        layout.addWidget(self.result_label, 2, 0, 1, 3)

    def on_load_click(self):
        try:
            size = int(self.size_input.text())
            if size <= 0:
                raise ValueError("Size must be a positive integer")

            if self.adj_matrix:
                for row in self.adj_matrix:
                    for cb in row:
                        self.layout().removeWidget(cb)
                        cb.deleteLater()

            self.adj_matrix = []
            for i in range(size):
                row = []
                for j in range(size):
                    cb = QCheckBox()
                    self.layout().addWidget(cb, i+2, j+1)
                    row.append(cb)
                self.adj_matrix.append(row)

            self.find_button.setEnabled(True)
        except Exception as e:
            print(e)

    def on_find_click(self):
        try:
            if self.adj_matrix:
                self.components = strongly_connected_components(self.adj_matrix)
                print("Components:", self.components)
                self.result_label.setText(str(self.components))
        except Exception as e:
            print(e)

def strongly_connected_components(adj_matrix):
    n = len(adj_matrix)
    visited = [False] * n
    stack = []
    for i in range(n):
        if not visited[i]:
            dfs(i, adj_matrix, visited, stack.append)
    transposed = transpose(adj_matrix)
    visited = [False] * n
    components = []
    while stack:
        node = stack.pop()
        if not visited[node]:
            component = []
            dfs(node, transposed, visited, lambda x: component.append(x))
            components.append(component)
    return components

def transpose(adj_matrix):
    return [[adj_matrix[j][i] for j in range(len(adj_matrix))] for i in range(len(adj_matrix[0]))]


def dfs(node, adj_matrix, visited, callback):
    visited[node] = True
    for i in range(len(adj_matrix)):
        if adj_matrix[node][i] and not visited[i]:
            dfs(i, adj_matrix, visited, callback)
    callback(node)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
