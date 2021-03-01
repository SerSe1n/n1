import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QVBoxLayout, QHBoxLayout, \
    QTableWidget, QWidget, QLabel

#code
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(768, 512)
        self.vl = QVBoxLayout(self)
        self.hl = QHBoxLayout(self)
        self.hl2 = QHBoxLayout(self)
        self.tableWidget = QTableWidget(self)
        self.label = QLabel(self)

        self.con = sqlite3.connect("coffee.db")
        cur = self.con.cursor()
        result = cur.execute("""SELECT * FROM info""").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))

        myl = ["ID", "Название", "Степень обжарки", "молотый/в зёрнах", "вкус", "цена", "объём"]

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setHorizontalHeaderItem(j, QTableWidgetItem(str(myl[j])))
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

        self.vl.addWidget(self.tableWidget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())
