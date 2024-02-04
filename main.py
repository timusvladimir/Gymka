import sys
import sqlite3
import datetime
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
AutoMinorLocator)
import matplotlib.dates

import numpy as np
import pandas as pd

import openpyxl
import re

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from gymka_ui import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.spisok = []
        self.con = sqlite3.connect("2024.02.04-14.40.23_manual.db")
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
            slovar = {}
            spisokdata = []
            spisoktime = []
            time_x = []
            data_y = []

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
                    request = "SELECT _id,name,startDateTime,setsAmount,repsAmount FROM training".format(self.search_1)
            except:
                if self.search_1 == '':
                    request = "SELECT _id,name,startDateTime,setsAmount,repsAmount FROM training".format(self.search_1)

            cur = self.con.cursor()
            result = cur.execute(request).fetchall()

            file_export = 'export_data.xlsx'
            wb = openpyxl.Workbook()
            ws = wb.active

            self.tableWidget.setColumnCount(len(result[0]))
            columns = [column[0] for column in cur.description]
            self.tableWidget.setHorizontalHeaderLabels(columns)

            ws.append(columns)

            spisok = []

            self.tableWidget.setRowCount(len(result))
            for i, elem in enumerate(result):
                ws.append(spisok)
                spisok.clear()
                for j, val in enumerate(elem):
                    if j == 2:
                        timedata = val
                        val = datetime.datetime.fromtimestamp(val / 1000.0, tz=datetime.timezone.utc)
                        val = val.strftime('%x %X')

                        spisoktime.append(val)
                    if j == 3:
                        value = val
                        spisokdata.append(val)
                        slovar[timedata] = value
                    spisok.append(val)
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
            self.tableWidget.resizeColumnsToContents()
            self.lineEdit_1.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
       #     data = [[row * col for col in range(1, 10)] for row in range(1, 31)]
         #   for row in data:
          #      ws.append(row)

            wb.save(file_export)
            wb.close()

            sorted_slovar = dict(sorted(slovar.items()))
            #time_x = spisoktime
            #data_y = spisokdata

            for key, value in sorted_slovar.items():
                key_to_data = datetime.datetime.fromtimestamp(key / 1000.0, tz=datetime.timezone.utc)
              #  key_to_data = key_to_data.strftime('%x')
                time_x.append(key_to_data)
                data_y.append(value)

            fig, ax = plt.subplots(figsize=(14, 6))
            ax.plot(time_x, data_y, 'o-r', label='подходы')
            ax.set_title('График количества подходов', fontsize=16)
            ax.set_xlabel('time', fontsize=14)
            # Повернем метки рисок на 55 градусов
            ax.tick_params(axis="x", labelrotation=55)
            # Изменим формат календарных данных
            ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%d.%m.%Y"))

            # !!! Изменим локатор, используемый по умолчанию
            locator = matplotlib.dates.MonthLocator()
            ax.xaxis.set_major_locator(locator)

            ax.legend(bbox_to_anchor=(1, 0.6))

            # Отмасштабируем график, чтобы в окно уместились повернутые надписи
            plt.tight_layout()
            plt.grid(True)
            plt.show()

        except Exception:
            self.label_4.setText('Введите значения полей')

    def run_button3(self):
        try:
            x = np.linspace(0, 10, 10)
            y1 = 4 * x
            y2 = [i ** 2 for i in x]
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.set_title('Графики зависимостей: y1=4*x, y2=x^2', fontsize=16)
            ax.set_xlabel('x', fontsize=14)
            ax.set_ylabel('y1, y2', fontsize=14)
            ax.grid(which='major', linewidth=1.2)
            ax.grid(which='minor', linestyle='--', color='gray', linewidth=0.5)
            ax.scatter(x, y1, c='red', label='y1 = 4*x')
            ax.plot(x, y2, label='y2 = x^2')
            ax.legend()
            ax.xaxis.set_minor_locator(AutoMinorLocator())
            ax.yaxis.set_minor_locator(AutoMinorLocator())
            ax.tick_params(which='major', length=10, width=2)
            ax.tick_params(which='minor', length=5, width=1)

            plt.show()

        except Exception:
            self.label_4.setText('Введите значения полей')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())