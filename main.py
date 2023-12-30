import sys
import sqlite3
import datetime
import matplotlib.pyplot as plt
import numpy as np
import re
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from gymka_ui import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.spisok = []
        self.con = sqlite3.connect("2023.12.30-15.38.28_manual.db")
        self.pushButton_1.clicked.connect(self.run_button1)
        self.pushButton_2.clicked.connect(self.run_button2)
        self.pushButton_3.clicked.connect(self.run_button3)

    def run_button1(self):
        try:
            self.tableWidget.clear
            self.search_1 = ''
            self.search_2 = ''
            self.search_3 = ''
            self.search_1 = self.lineEdit_1.text()
            self.search_2 = self.lineEdit_2.text()
            self.search_3 = self.lineEdit_3.text()
            try:
                int(self.search_1)
                if self.search_1 == '':
                    request = "SELECT training_id,th_exercise_id FROM workout".format(self.search_1)
            except:
                if self.search_1 == '':
                    request = "SELECT training_id,th_exercise_id FROM workout".format(self.search_1)

            cur = self.con.cursor()
            result = cur.execute(request).fetchall()
            self.tableWidget.setColumnCount(len(result[0]))
            columns = [column[0] for column in cur.description]
            self.tableWidget.setHorizontalHeaderLabels(columns)
            self.tableWidget.setRowCount(len(result))
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
            self.tableWidget.resizeColumnsToContents()
            self.lineEdit_1.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
        except Exception:
            self.label_4.setText('Введите значения полей')

    def run_button2(self):
        try:
            self.tableWidget.clear
            self.search_1 = ''
            self.search_2 = ''
            self.search_3 = ''
            self.search_1 = self.lineEdit_1.text()
            self.search_2 = self.lineEdit_2.text()
            self.search_3 = self.lineEdit_3.text()
            try:
                int(self.search_1)
                if self.search_1 == '':
                    request = "SELECT _id,name,startDateTime,setsAmount FROM training".format(self.search_1)
            except:
                if self.search_1 == '':
                    request = "SELECT _id,name,startDateTime,setsAmount FROM training".format(self.search_1)

            cur = self.con.cursor()
            result = cur.execute(request).fetchall()
            self.tableWidget.setColumnCount(len(result[0]))
            columns = [column[0] for column in cur.description]
            self.tableWidget.setHorizontalHeaderLabels(columns)
            self.tableWidget.setRowCount(len(result))
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    if j == 2:
                        val = datetime.datetime.fromtimestamp(val / 1000.0, tz=datetime.timezone.utc)
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
            self.tableWidget.resizeColumnsToContents()
            self.lineEdit_1.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
        except Exception:
            self.label_4.setText('Введите значения полей')

    def run_button3(self):
        try:
            # Линейная зависимость
            x = np.linspace(0, 10, 50)
            y1 = x
            # Квадратичная зависимость
            y2 = [i ** 2 for i in x]
            # Построение графиков
            plt.figure(figsize=(9, 9))
            plt.subplot(2, 1, 1)
            plt.plot(x, y1)  # построение графика
            plt.title('Зависимости: y1 = x, y2 = x^2')  # заголовок
            plt.ylabel('y1', fontsize=14)  # ось ординат
            plt.grid(True)  # включение отображение сетки
            plt.subplot(2, 1, 2)
            plt.plot(x, y2)  # построение графика
            plt.xlabel('x', fontsize=14)  # ось абсцисс
            plt.ylabel('y2', fontsize=14)  # ось ординат
            plt.grid(True)  # включение отображение сетки

            plt.show()

        except Exception:
            self.label_4.setText('Введите значения полей')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())