from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QTableWidget, QPushButton, \
    QLineEdit, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QLinearGradient, QColor
import functional_interface as fi


def dialog_window(text: str):
    dlg = QMessageBox()
    dlg.setInformativeText(text)
    dlg.setStyleSheet("QLabel{ color: gray}")
    dlg.exec()

class LabaInterface(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Full Screen Window")
        self.resize(1480, 1080)
        # self.showFullScreen()

        self.setStyleSheet("background-color: white;")

        # Устанавливаем белый цвет текста для всех элементов
        QApplication.instance().setStyleSheet("QLabel{ color : black; }"
                                              "QPushButton { color : black; }"
                                              "QLineEdit { color : black; }"
                                              "QTableWidget { color : black; }")

        gradient = QLinearGradient(0, 0, 0, self.height())  # Создаем градиент
        gradient.setColorAt(1, QColor(255, 255, 255))
        gradient.setColorAt(0, QColor(255, 255, 255))
        self.gradient = gradient

        self.first_winodow()

    def first_winodow(self):
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        self.sublayout1 = QGridLayout()
        self.sublayout2 = QGridLayout()
        self.sublayout3 = QGridLayout()
        main_layout.addLayout(self.sublayout1, 0)
        main_layout.addLayout(self.sublayout2, 1)
        main_layout.addLayout(self.sublayout3, 2)


        self.manual_matrix_input_button = QPushButton("Создать матрицу вручную")
        self.auto_matrix_input_button = QPushButton("Создать матрицу по ограничениям")
        self.choose_mode_button = QPushButton("Вернуться к выбору режима")

        self.sublayout1.addWidget(self.manual_matrix_input_button, 0, 0)
        self.sublayout1.addWidget(self.auto_matrix_input_button, 0, 1)
        self.sublayout1.addWidget(self.choose_mode_button, 1, 0, 1, 2)

        self.matrix_count = 0
        self.manual_matrix_input_button.clicked.connect(self.manual_matrix_input)
        self.auto_matrix_input_button.clicked.connect(self.auto_matrix_input)  # <- лямбда функция в параметре
        self.choose_mode_button.hide()
        self.choose_mode_button.clicked.connect(lambda: self.choose_mode())

        self.create_manual_count = 0
        self.create_auto_count = 0

    def choose_mode(self):
        if self.create_manual_count != 0:
            self.manual_matrix_input_button.show()
            self.auto_matrix_input_button.show()
            self.choose_mode_button.hide()

            self.matrix_size.hide()
            self.matrix_size.clear()
            # self.matrix_col_size.hide()
            # self.matrix_col_size.clear()
            self.create_matrix_button.hide()
            self.matrix_name.hide()

            if self.matrix_count != 0:
                self.matrix.hide()
                self.matrix.clear()
                self.manual_result_button.hide()


            if self.manual_res_count != 0:
                self.result1.hide()
                self.result2.hide()
                self.result3.hide()
                self.result4.hide()
                self.result5.hide()
                self.result6.hide()
                self.result1.clear()
                self.result2.clear()
                self.result3.clear()
                self.result4.clear()
                self.result5.clear()
                self.result6.clear()

            self.create_manual_count = 0
            self.manual_res_count = 0
            self.create_auto_count = 0
            self.auto_res_count = 0



        elif self.create_auto_count != 0:
            self.manual_matrix_input_button.show()
            self.auto_matrix_input_button.show()
            self.choose_mode_button.hide()

            self.first_string_name.hide()
            # self.auto_matrix_col_size.hide()
            self.second_string_name.hide()
            # self.auto_matrix_col_size.hide()
            self.auto_matrix_size.hide()
            # self.auto_matrix_col_size.hide()

            self.min_size1.hide()
            self.max_size1.hide()
            self.min_size2.hide()
            self.max_size2.hide()
            self.min_size3.hide()
            self.max_size3.hide()
            self.auto_result_button.hide()

            if self.auto_res_count != 0:
                self.result7.hide()

            self.create_manual_count = 0
            self.manual_res_count = 0
            self.create_auto_count = 0
            self.auto_res_count = 0

    def auto_matrix_input(self):
        self.manual_matrix_input_button.hide()
        self.auto_matrix_input_button.hide()
        self.choose_mode_button.show()

        self.create_auto_count = 1
        self.auto_res_count = 0


        self.first_string_name = QLineEdit("Введите размер матрицы")
        self.second_string_name = QLineEdit("Введите ограничения параметров")
        self.auto_matrix_size = QLineEdit()
        # self.auto_matrix_col_size = QLineEdit()
        self.min_size1 = QLineEdit()
        self.max_size1 = QLineEdit()
        self.min_size2 = QLineEdit()
        self.max_size2 = QLineEdit()
        self.min_size3 = QLineEdit()
        self.max_size3 = QLineEdit()

        self.result7 = QLineEdit()
        self.result7.hide()

        self.auto_result_button = QPushButton("Решить")
        self.auto_result_button.clicked.connect(lambda: self.result("auto"))

        self.sublayout3.addWidget(self.first_string_name, 0, 0, 1, 2)
        self.sublayout3.addWidget(self.auto_matrix_size, 1, 0)
        # self.sublayout3.addWidget(self.auto_matrix_col_size, 1, 1)
        self.sublayout3.addWidget(self.second_string_name, 2, 0, 1, 2)
        self.sublayout3.addWidget(self.min_size1, 3, 0)
        self.sublayout3.addWidget( self.max_size1, 3, 1)
        self.sublayout3.addWidget(self.min_size2, 4, 0)
        self.sublayout3.addWidget( self.max_size2, 4, 1)
        self.sublayout3.addWidget(self.min_size3, 5, 0)
        self.sublayout3.addWidget( self.max_size3, 5, 1)
        self.sublayout3.addWidget(self.auto_result_button, 6, 0, 1, 2)
        self.sublayout3.addWidget(self.result7, 7, 0, 1, 2)





    def manual_matrix_input(self):
        self.manual_matrix_input_button.hide()
        self.auto_matrix_input_button.hide()
        self.choose_mode_button.show()

        self.create_manual_count = 1
        self.manual_res_count = 0

        self.matrix_name = QLineEdit()
        # matrix_name.setReadOnly()
        self.matrix_name.setText("Введите размеры матрицы")
        self.matrix_size = QLineEdit()
        # self.matrix_col_size = QLineEdit()

        self. create_matrix_button = QPushButton("Создать")
        self.create_matrix_button.clicked.connect(lambda: self.create_matrix(self.matrix_size))

        self.sublayout2.addWidget(self.matrix_name, 0, 0, 1, 3)
        self.sublayout2.addWidget(self.matrix_size, 1, 0)
        # self.sublayout2.addWidget(self.matrix_col_size, 1, 1)
        self.sublayout2.addWidget(self.create_matrix_button, 1, 2)

    def create_matrix(self, size):
        try:
            self.int_valid([self.matrix_size.text()], 0)
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

        self.matrix.show()
        self.matrix.horizontalHeader().setVisible(False)
        self.matrix.verticalHeader().setVisible(False)

        self.matrix.setRowCount(int(size.text()))
        self.matrix.setColumnCount(int(size.text()))

        self.sublayout2.addWidget(self.matrix, 2, 0, 1, 3)
        self.matrix.setMaximumSize(int(size.text()) * 130, int(size.text()) * 46)

        self.result1 = QLineEdit()
        self.result2 = QLineEdit()
        self.result3 = QLineEdit()
        self.result4 = QLineEdit()
        self.result5 = QLineEdit()
        self.result6 = QLineEdit()
        self.result1.hide()
        self.result2.hide()
        self.result3.hide()
        self.result4.hide()
        self.result5.hide()
        self.result6.hide()
        self.manual_result_button = QPushButton("Решить")
        self.manual_result_button.clicked.connect(lambda: self.result("manual"))

        self.sublayout2.addWidget(self.manual_result_button, 3, 0, 1, 3)
        self.sublayout2.addWidget(self.result1, 4, 0, 1, 3)
        self.sublayout2.addWidget(self.result2, 5, 0, 1, 3)
        self.sublayout2.addWidget(self.result3, 6, 0, 1, 3)
        self.sublayout2.addWidget(self.result4, 7, 0, 1, 3)
        self.sublayout2.addWidget(self.result5, 8, 0, 1, 3)
        self.sublayout2.addWidget(self.result6, 9, 0, 1, 3)

    def result(self, type):
        if type == "manual":
            try:
                m = []
                for i in range(int(self.matrix_size.text())):
                    vector = []
                    for j in range(int(self.matrix_size.text())):
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
            for i in range(int(self.matrix_size.text())):
                for j in range(int(self.matrix_size.text())):
                    m[i][j] = float(m[i][j])
            self.manual_res_count = 1
            self.result1.show()
            self.result2.show()
            self.result3.show()
            self.result4.show()
            self.result5.show()
            self.result6.show()

            res = fi.manual(int(self.matrix_size.text()), m)

            self.result1.setText("Результат 1 = " + str(res[0]))
            self.result2.setText("Результат 2 = " + str(res[1]))
            self.result3.setText("Результат 3 = " + str(res[2]))
            self.result4.setText("Результат 4 = " + str(res[3]))
            self.result5.setText("Результат 5 = " + str(res[4]))
            self.result6.setText("Результат 6 = " + str(res[5]))
        elif (type == "auto"):
            self.auto_res_count = 1
            try:
                self.int_valid([self.auto_matrix_size.text()], 1)
                self.float_valid([self.min_size1.text(),
                                  self.max_size1.text(),
                                  self.min_size2.text(),
                                  self.max_size2.text(),
                                  self.min_size3.text(),
                                  self.max_size3.text()], 1)

            except Exception as ex:
                info_msg = QMessageBox()
                info_msg.setWindowTitle('Ввод параметров')
                info_msg.setText(ex.args[0])
                info_msg.setIcon(QMessageBox.Icon.Critical)
                info_msg.exec()
                return
            self.result7.show()

            self.result7.setText("Результат 7")

            fi.experiment(int(self.auto_matrix_size.text()), float(self.min_size1.text()),
                          float(self.max_size1.text()),
                          float(self.min_size2.text()) + 1.0,
                          float(self.max_size2.text()) + 1.0,
                          float(self.min_size3.text()),
                          float(self.max_size3.text()))

    def float_valid(self, floatList, flag):
        for param in floatList:
            try:
                float(param)
            except ValueError:
                raise Exception("Параметры должны быть числовыми значениями")
            if (float(param) <= 0):
                raise Exception("Параметры должны быть больше нуля")
        if (flag):
            for i in range(len(floatList) // 2):
                if (float(floatList[2 * i]) >= 1.0 or float(floatList[2 * i + 1]) >= 1.0):
                    raise Exception("Параметры должны быть меньше единицы")
                if (float(floatList[2 * i]) > float(floatList[2 * i + 1])):
                    raise Exception("Минимальное значение параметра должно быть не больше максимального")
        return True

    def int_valid(self, intList, flag):
        for num in intList:
            try:
                int(num)
            except ValueError:
                raise Exception("Размер матрицы должет быть целочисленным")
            if (int(num) < 0):
                raise Exception("Размер матрицы должет быть больше нуля")
        return True

    def paintEvent(self, event):
        self.setStyleSheet("border: 1px solid;"
                           "border-color : black;"
                           "font-size: 26px;")

if __name__ == '__main__':
    try:
        app = QApplication([])
        app.setStyle("Windows")
        windows = LabaInterface()

        windows.show()
        app.exec()
    except Exception as r:
        dialog_window(f"Ошибка: {type(r).__name__} - {r}")