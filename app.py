from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit
from PyQt6.QtCore import Qt
from functions import word_result

def clear():
    if result.text().strip() != "":
        text.setText('')
        result.setText('')
        window.adjustSize()

def show_definitions():
    input_text = text.text()

    if input_text.strip() != "":
        entries = word_result(input_text.lower())

        if entries == []:
            result.setText('The word you searched for does not exist. Please, check your spelling')
        else:
            definitions = ""

            for x, entry in enumerate(entries):
                definitions = definitions + f"{x + 1}. {entry['senses'][0]['definition']}\n"
        
            result.setText(definitions)


app = QApplication([])

layout = QVBoxLayout()

text = QLineEdit()
text.setPlaceholderText("Search for a word...")
layout.addWidget(text)

search_button = QPushButton('Search word')
layout.addWidget(search_button)
search_button.clicked.connect(show_definitions)

clear_button = QPushButton('Clear results')
layout.addWidget(clear_button)
clear_button.clicked.connect(clear)

result = QLabel()
layout.addWidget(result)

window = QWidget()
window.setWindowTitle("Dictionary App")
window.setLayout(layout)
window.show()

app.exec()