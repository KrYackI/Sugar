import csv

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QTableWidget, QPushButton, \
    QLineEdit, QVBoxLayout, QMessageBox, QFileDialog
from PyQt5.QtGui import QLinearGradient, QColor
import functional_interface as fi
from pyqtgraph import PlotWidget, PlotItem, LegendItem
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout.setObjectName("gridLayout")

        self.graphicsView = PlotWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.getPlotItem().showGrid(x=True, y=True, alpha=0.5)
        self.graphicsView.getPlotItem().setLabel(axis='left', text='Sugar value')
        self.graphicsView.getPlotItem().setLabel(axis='bottom', text='Days')
        self.graphicsView.getPlotItem().setTitle(title="Algorithms comparison")
        self.gridLayout.addWidget(self.graphicsView, 2, 1, 5, 2)

        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setMaximum(999)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_3.addWidget(self.spinBox, 1, 0, 1, 1)


        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setMaximum(999)
        self.spinBox_2.setObjectName("spinBox_2")
        self.gridLayout_3.addWidget(self.spinBox_2, 1, 1, 1, 1)

        self.label_n = QtWidgets.QLabel(self.centralwidget)
        self.label_n.setAutoFillBackground(False)
        self.label_n.setScaledContents(False)
        self.label_n.setWordWrap(True)
        self.label_n.setObjectName("label_n")
        self.gridLayout_3.addWidget(self.label_n, 0, 0, 1, 1)

        self.label_m = QtWidgets.QLabel(self.centralwidget)
        self.label_m.setAutoFillBackground(False)
        self.label_m.setScaledContents(False)
        self.label_m.setWordWrap(True)
        self.label_m.setObjectName("label_m")
        self.gridLayout_3.addWidget(self.label_m, 0, 1, 1, 1)

        self.param_1 = QtWidgets.QLabel(self.centralwidget)
        self.param_1.setWordWrap(True)
        self.param_1.setObjectName("param_1")
        self.gridLayout_3.addWidget(self.param_1, 2, 0, 1, 1)

        self.param_2 = QtWidgets.QLabel(self.centralwidget)
        self.param_2.setWordWrap(True)
        self.param_2.setObjectName("param_2")
        self.gridLayout_3.addWidget(self.param_2, 2, 1, 1, 1)

        self.param_3 = QtWidgets.QLabel(self.centralwidget)
        self.param_3.setWordWrap(True)
        self.param_3.setObjectName("param_3")
        self.gridLayout_3.addWidget(self.param_3, 4, 0, 1, 1)

        self.param_4 = QtWidgets.QLabel(self.centralwidget)
        self.param_4.setWordWrap(True)
        self.param_4.setObjectName("param_4")
        self.gridLayout_3.addWidget(self.param_4, 4, 1, 1, 1)

        self.param_5 = QtWidgets.QLabel(self.centralwidget)
        self.param_5.setWordWrap(True)
        self.param_5.setObjectName("param_5")
        self.gridLayout_3.addWidget(self.param_5, 6, 0, 1, 1)

        self.param_6 = QtWidgets.QLabel(self.centralwidget)
        self.param_6.setWordWrap(True)
        self.param_6.setObjectName("param_6")
        self.gridLayout_3.addWidget(self.param_6, 6, 1, 1, 1)

        self.min_size1 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.min_size1.setAccelerated(False)
        self.min_size1.setMinimum(0.01)
        self.min_size1.setMaximum(1.0)
        self.min_size1.setSingleStep(0.01)
        self.min_size1.setObjectName("min_size1")
        self.gridLayout_3.addWidget(self.min_size1, 3, 0, 1, 1)

        self.max_size1 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.max_size1.setMinimum(0.01)
        self.max_size1.setMaximum(1.0)
        self.max_size1.setSingleStep(0.01)
        self.max_size1.setObjectName("max_size1")
        self.gridLayout_3.addWidget(self.max_size1, 3, 1, 1, 1)

        self.min_size2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.min_size2.setMinimum(1.0)
        self.min_size2.setMaximum(3.0)
        self.min_size2.setSingleStep(0.01)
        self.min_size2.setObjectName("min_size2")
        self.gridLayout_3.addWidget(self.min_size2, 5, 0, 1, 1)

        self.max_size2 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.max_size2.setMinimum(1.0)
        self.max_size2.setMaximum(3.0)
        self.max_size2.setSingleStep(0.01)
        self.max_size2.setObjectName("max_size2")
        self.gridLayout_3.addWidget(self.max_size2, 5, 1, 1, 1)

        self.min_size3 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.min_size3.setMinimum(0.01)
        self.min_size3.setMaximum(1.0)
        self.min_size3.setSingleStep(0.01)
        self.min_size3.setObjectName("min_size3")
        self.gridLayout_3.addWidget(self.min_size3, 7, 0, 1, 1)

        self.max_size3 = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.max_size3.setMinimum(0.01)
        self.max_size3.setMaximum(1.0)
        self.max_size3.setSingleStep(0.01)
        self.max_size3.setObjectName("max_size3")
        self.gridLayout_3.addWidget(self.max_size3, 7, 1, 1, 1)


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.result("auto"))
        self.gridLayout_3.addWidget(self.pushButton_2, 8, 0, 2, 2)

        self.create_matrix_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_matrix_button.setObjectName("pushButton_3")
        self.create_matrix_button.clicked.connect(lambda: self.create_matrix(self.spinBox.value()))
        self.gridLayout_3.addWidget(self.create_matrix_button, 0, 1, 1, 1)
        self.create_matrix_button.hide()

        self.manual_result_button = QtWidgets.QPushButton(self.centralwidget)
        self.manual_result_button.setObjectName("pushButton_4")
        self.manual_result_button.clicked.connect(lambda: self.result("manual"))
        self.gridLayout_3.addWidget(self.manual_result_button, 3, 0, 2, 2)
        self.manual_result_button.hide()


        self.gridLayout.addLayout(self.gridLayout_3, 2, 0, 3, 1)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.result1 = QtWidgets.QLabel(self.centralwidget)
        self.result1.setObjectName("result1")
        self.result1.hide()
        self.verticalLayout.addWidget(self.result1)

        self.result2 = QtWidgets.QLabel(self.centralwidget)
        self.result2.setObjectName("result2")
        self.result2.hide()
        self.verticalLayout.addWidget(self.result2)

        self.result3 = QtWidgets.QLabel(self.centralwidget)
        self.result3.setObjectName("result3")
        self.result3.hide()
        self.verticalLayout.addWidget(self.result3)

        self.result4 = QtWidgets.QLabel(self.centralwidget)
        self.result4.setObjectName("result4")
        self.result4.hide()
        self.verticalLayout.addWidget(self.result4)

        self.result5 = QtWidgets.QLabel(self.centralwidget)
        self.result5.setObjectName("result5")
        self.result5.hide()
        self.verticalLayout.addWidget(self.result5)

        self.result6 = QtWidgets.QLabel(self.centralwidget)
        self.result6.setObjectName("result6")
        self.result6.hide()
        self.verticalLayout.addWidget(self.result6)

        self.gridLayout.addLayout(self.verticalLayout, 5, 0, 2, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")

        self.menuMode = QtWidgets.QMenu(self.menubar)
        self.menuMode.setObjectName("menuMode")

        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionManual = QtWidgets.QAction(MainWindow)
        self.actionManual.setObjectName("actionManual")
        self.actionManual.triggered.connect(self.manual_matrix_input)

        self.actionExperiment = QtWidgets.QAction(MainWindow)
        self.actionExperiment.setObjectName("actionExperiment")
        self.actionExperiment.triggered.connect(self.auto_matrix_input)

        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered.connect(self.save_results)

        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")

        self.menuMode.addAction(self.actionManual)
        self.menuMode.addAction(self.actionExperiment)
        self.menufile.addAction(self.actionSave)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuMode.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.matrix_count = 0
        self.create_manual_count = 0
        self.create_auto_count = 0
        self.manual_res_count = 0
        self.auto_res_count = 0
        self.mode = 0
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_n.setText(_translate("MainWindow", "Введите число партий"))
        self.label_m.setText(_translate("MainWindow", "Введите число дней дозаривания"))
        self.param_5.setText(_translate("MainWindow", "Мин. коэфф. деградации"))
        self.param_6.setText(_translate("MainWindow", "Макс. коэфф. деградации"))
        self.param_3.setText(_translate("MainWindow", "Мин. коэфф. дозаривания"))
        self.param_4.setText(_translate("MainWindow", "Макс. коэфф. дозаривания"))
        self.param_1.setText(_translate("MainWindow", "Мин. стартовая величина"))
        self.param_2.setText(_translate("MainWindow", "Макс. стартовая величина"))
        self.pushButton_2.setText(_translate("MainWindow", "Провести эксперимент"))
        self.create_matrix_button.setText(_translate("MainWindow", "Создать матрицу"))
        self.manual_result_button.setText(_translate("MainWindow", "Решить"))
        self.result1.setText(_translate("MainWindow", "TextLabel"))
        self.result2.setText(_translate("MainWindow", "TextLabel"))
        self.result3.setText(_translate("MainWindow", "TextLabel"))
        self.result4.setText(_translate("MainWindow", "TextLabel"))
        self.result5.setText(_translate("MainWindow", "TextLabel"))
        self.result6.setText(_translate("MainWindow", "TextLabel"))
        self.menuMode.setTitle(_translate("MainWindow", "Mode"))
        self.menufile.setTitle(_translate("MainWindow", "File"))
        self.actionManual.setText(_translate("MainWindow", "Manual"))
        self.actionExperiment.setText(_translate("MainWindow", "Experiment"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
    
    ''' input modes '''
    def manual_matrix_input(self):

        self.mode = 1
        self.create_manual_count = 1
        self.manual_res_count = 0

        self.graphicsView.clear()
        # self.spinBox.clear()

        self.create_matrix_button.show()

        self.label_m.hide()
        self.spinBox_2.hide()
        self.param_1.hide()
        self.param_2.hide()
        self.param_3.hide()
        self.param_4.hide()
        self.param_5.hide()
        self.param_6.hide()
        self.min_size1.hide()
        self.min_size2.hide()
        self.min_size3.hide()
        self.max_size1.hide()
        self.max_size2.hide()
        self.max_size3.hide()
        self.pushButton_2.hide()
        self.result1.hide()
        self.result2.hide()
        self.result3.hide()
        self.result4.hide()
        self.result5.hide()
        self.result6.hide()
        
    def auto_matrix_input(self):

        self.mode = 0
        self.create_auto_count = 1
        self.auto_res_count = 0

        self.graphicsView.clear()

        self.create_matrix_button.hide()
        if (self.matrix_count == 1):
            self.matrix.hide()
        self.manual_result_button.hide()
        self.result1.hide()
        self.result2.hide()
        self.result3.hide()
        self.result4.hide()
        self.result5.hide()
        self.result6.hide()

        self.label_m.show()
        self.spinBox_2.show()
        self.param_1.show()
        self.param_2.show()
        self.param_3.show()
        self.param_4.show()
        self.param_5.show()
        self.param_6.show()
        self.min_size1.show()
        self.min_size2.show()
        self.min_size3.show()
        self.max_size1.show()
        self.max_size2.show()
        self.max_size3.show()
        self.pushButton_2.show()

    ''' end of input modes '''
    
    def create_matrix(self, size):
        try:
            self.int_valid([size], 0)
        except Exception as ex:
            info_msg = QMessageBox()
            info_msg.setWindowTitle('Ввод матрицы')
            info_msg.setText(ex.args[0])
            info_msg.setIcon(QMessageBox.Icon.Critical)
            info_msg.exec()
            return
        self.manual_res_count = 0
        if self.matrix_count == 0:
            self.matrix = QTableWidget()
            self.matrix_count += 1
            self.matrix.horizontalHeader().setVisible(False)
            self.matrix.verticalHeader().setVisible(False)

        self.matrix.show()

        self.matrix.setRowCount(size)
        self.matrix.setColumnCount(size)
        self.matrix.resizeRowsToContents()


        self.matrix.setMaximumSize(self.matrix.columnCount() * self.matrix.columnWidth(size - 1) + 2, self.matrix.rowCount() * self.matrix.rowHeight(size - 1) + 2)
        self.gridLayout_3.addWidget(self.matrix, 2, 0, 1, 2)

        self.manual_result_button.show()

    def result(self, type):
        self.graphicsView.clear()
        if type == "manual":
            try:
                m = []
                for i in range(self.spinBox.value()):
                    vector = []
                    for j in range(self.spinBox.value()):
                        vector.append(self.matrix.item(i, j).text())
                    m.append(vector)
            except:
                info_msg = QMessageBox()
                info_msg.setWindowTitle('Ввод матрицы')
                info_msg.setText("Все ячейки матрицы должны быть заполнены")
                info_msg.setIcon(QMessageBox.Icon.Critical)
                info_msg.exec()
                return

            try:
                self.float_valid([k for v in m for k in v], 0)

            except Exception as ex:
                info_msg = QMessageBox()
                info_msg.setWindowTitle('Ввод матрицы')
                info_msg.setText(ex.args[0])
                info_msg.setIcon(QMessageBox.Icon.Critical)
                info_msg.exec()
                return
            for i in range(self.spinBox.value()):
                for j in range(self.spinBox.value()):
                    m[i][j] = float(m[i][j])
            self.manual_res_count = 1
            self.result1.show()
            self.result2.show()
            self.result3.show()
            self.result4.show()
            self.result5.show()
            self.result6.show()
            # self.result7.show()
            # self.result8.show()
            # self.result9.show()

            res, plots = fi.manual(self.spinBox.value(), m)

            self.draw(plots)

            self.result1.setText(res[0])
            self.result2.setText(res[1])
            self.result3.setText(res[2])
            self.result4.setText(res[3])
            self.result5.setText(res[4])
            self.result6.setText(res[5])
            ##################################
            # comment if only 6 algorithms
            # self.result7.setText(res[6])
            # self.result8.setText(res[7])
            # self.result9.setText(res[8])
            ##################################
        elif (type == "auto"):
            self.auto_res_count = 1
            try:
                self.int_valid([self.spinBox.value()], 1) # поменять на 1
                self.float_valid([self.min_size1.value(),
                                  self.max_size1.value(),
                                  self.min_size2.value(),
                                  self.max_size2.value(),
                                  self.min_size3.value(),
                                  self.max_size3.value()], 1)

            except Exception as ex:
                info_msg = QMessageBox()
                info_msg.setWindowTitle('Ввод параметров')
                info_msg.setText(ex.args[0])
                info_msg.setIcon(QMessageBox.Icon.Critical)
                info_msg.exec()
                return



            res, plots = fi.experiment(self.spinBox.value(), self.min_size1.value(),
                                                          self.max_size1.value(),
                                                          self.min_size2.value(),
                                                          self.max_size2.value(),
                                                          self.min_size3.value(),
                                                          self.max_size3.value())

            self.draw(plots)

            self.result1.setText(res[0])
            self.result2.setText(res[1])
            self.result3.setText(res[2])
            self.result4.setText(res[3])
            self.result5.setText(res[4])
            self.result6.setText(res[5])
            #################################
            # comment if only 6 algorithms
            # self.result7.setText(res[6])
            # self.result8.setText(res[7])
            # self.result9.setText(res[8])
            #################################

            self.result1.show()
            self.result2.show()
            self.result3.show()
            self.result4.show()
            self.result5.show()
            self.result6.show()
            # self.result7.show()
            # self.result8.show()
            # self.result9.show()

    ''' validations '''

    def float_valid(self, floatList, flag):
        if (flag):
            for i in range(len(floatList) // 2):
                if (float(floatList[2 * i]) > float(floatList[2 * i + 1])):
                    raise Exception("Минимальное значение параметра должно быть не больше максимального")
        return True

    def int_valid(self, intList, flag):
        if (intList[0] <= 0):
            raise Exception("Размер матрицы должен быть больше нуля")
        if (not flag and int(intList[0]) >= 10):
            raise Exception("Размер матрицы должен быть небольшим")
        if (flag==2):
            if (intList[1] <= intList[0]):
                raise Exception("Число экспериментов должно быть меньше общего числа партий")
        return True

    ''' end of validations '''


    ''' drawing '''
    def draw(self, plots):
        Days = [i + 1 for i in range(len(plots[0]))]
        names = ["Hungarian min", "Hungarian max", "Greedy", "Thrifty", "Greedy-thrifty", "Thrifty-greedy", "T(k)G", "CTG", "G(k)"]
        legend = self.graphicsView.getPlotItem().addLegend()
        for i in range(len(plots)):
            item = self.graphicsView.plot(Days, plots[i], pen=(i, len(plots)))
            legend.addItem(item=item, name=names[i])
    ''' end of drawing '''


    ''' save/load data '''
    def save_results(self):
        if self.mode==1:
            path=QFileDialog.getSaveFileName( caption='save CSV', filter='CSV(*.csv)')
            if path[0] != '':
                with open(path[0], 'w', newline='') as csv_file:
                    writer=csv.writer(csv_file, delimiter=';', lineterminator='\r')
                    for row in range(self.spinBox.value()):
                        row_data=[]
                        for column in range(self.spinBox.value()):
                            item=self.matrix.item(row, column)
                            if item is not None:
                                row_data.append(float(item.text()))
                            else:
                                row_data.append(' ')
                        writer.writerow(row_data)
                    writer.writerow([''])

                    if self.manual_res_count:
                        writer.writerow([self.result1.text()[:self.result1.text().find(':') + 1], self.result1.text()[self.result1.text().find(':') + 2:]])
                        writer.writerow([self.result2.text()[:self.result2.text().find(':') + 1], self.result2.text()[self.result2.text().find(':') + 2:]])
                        writer.writerow([self.result3.text()[:self.result3.text().find(':') + 1], self.result3.text()[self.result3.text().find(':') + 2:]])
                        writer.writerow([self.result4.text()[:self.result4.text().find(':') + 1], self.result4.text()[self.result4.text().find(':') + 2:]])
                        writer.writerow([self.result5.text()[:self.result5.text().find(':') + 1], self.result5.text()[self.result5.text().find(':') + 2:]])
                        writer.writerow([self.result6.text()[:self.result6.text().find(':') + 1], self.result6.text()[self.result6.text().find(':') + 2:]])
        if self.mode==0:
            path=QFileDialog.getSaveFileName( caption='save CSV', filter='CSV(*.csv)')
            if path[0] != '':
                with open(path[0], 'w', newline='') as csv_file:
                    writer=csv.writer(csv_file, delimiter=';', lineterminator='\r')
                    writer.writerow(["Число партий", "Число дней дозаривания"])
                    writer.writerow([self.spinBox.value(), self.spinBox_2.value()])
                    writer.writerow([''])
                    writer.writerow([self.param_1.text(), self.param_2.text()])
                    writer.writerow([self.min_size1.value(), self.max_size1.value()])
                    writer.writerow([self.param_3.text(), self.param_4.text()])
                    writer.writerow([self.min_size2.value(), self.max_size2.value()])
                    writer.writerow([self.param_5.text(), self.param_6.text()])
                    writer.writerow([self.min_size3.value(), self.max_size3.value()])
                    writer.writerow([''])

                    if self.auto_res_count:
                        writer.writerow([self.result1.text()[:self.result1.text().find(':') + 1], self.result1.text()[self.result1.text().find(':') + 2:]])
                        writer.writerow([self.result2.text()[:self.result2.text().find(':') + 1], self.result2.text()[self.result2.text().find(':') + 2:]])
                        writer.writerow([self.result3.text()[:self.result3.text().find(':') + 1], self.result3.text()[self.result3.text().find(':') + 2:]])
                        writer.writerow([self.result4.text()[:self.result4.text().find(':') + 1], self.result4.text()[self.result4.text().find(':') + 2:]])
                        writer.writerow([self.result5.text()[:self.result5.text().find(':') + 1], self.result5.text()[self.result5.text().find(':') + 2:]])
                        writer.writerow([self.result6.text()[:self.result6.text().find(':') + 1], self.result6.text()[self.result6.text().find(':') + 2:]])


    ''' end of save/load data '''


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
