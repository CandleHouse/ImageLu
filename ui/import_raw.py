# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'import_raw.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(319, 283)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.white_zero_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.white_zero_checkBox.setFont(font)
        self.white_zero_checkBox.setObjectName("white_zero_checkBox")
        self.gridLayout.addWidget(self.white_zero_checkBox, 4, 0, 1, 1)
        self.little_endian_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.little_endian_checkBox.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.little_endian_checkBox.setFont(font)
        self.little_endian_checkBox.setChecked(True)
        self.little_endian_checkBox.setObjectName("little_endian_checkBox")
        self.gridLayout.addWidget(self.little_endian_checkBox, 5, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.import_conf = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.import_conf.setFont(font)
        self.import_conf.setObjectName("import_conf")
        self.horizontalLayout_5.addWidget(self.import_conf)
        self.import_cancel = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.import_cancel.setFont(font)
        self.import_cancel.setObjectName("import_cancel")
        self.horizontalLayout_5.addWidget(self.import_cancel)
        self.import_help = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.import_help.setFont(font)
        self.import_help.setObjectName("import_help")
        self.horizontalLayout_5.addWidget(self.import_help)
        self.gridLayout.addLayout(self.horizontalLayout_5, 6, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4, 0, QtCore.Qt.AlignRight)
        self.height_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.height_lineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.height_lineEdit.setFont(font)
        self.height_lineEdit.setObjectName("height_lineEdit")
        self.horizontalLayout_3.addWidget(self.height_lineEdit)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6, 0, QtCore.Qt.AlignRight)
        self.offset_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.offset_lineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.offset_lineEdit.setFont(font)
        self.offset_lineEdit.setObjectName("offset_lineEdit")
        self.horizontalLayout_4.addWidget(self.offset_lineEdit)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignRight)
        self.width_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.width_lineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.width_lineEdit.setFont(font)
        self.width_lineEdit.setObjectName("width_lineEdit")
        self.horizontalLayout_2.addWidget(self.width_lineEdit)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignLeft)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignRight)
        self.image_type_comboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.image_type_comboBox.setFont(font)
        self.image_type_comboBox.setObjectName("image_type_comboBox")
        self.image_type_comboBox.addItem("")
        self.image_type_comboBox.addItem("")
        self.horizontalLayout.addWidget(self.image_type_comboBox)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 319, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.import_help.clicked.connect(MainWindow.import_help) # type: ignore
        self.import_cancel.clicked.connect(MainWindow.close) # type: ignore
        self.import_conf.clicked.connect(MainWindow.set_info) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Import>Raw???"))
        self.white_zero_checkBox.setText(_translate("MainWindow", "White is zero"))
        self.little_endian_checkBox.setText(_translate("MainWindow", "Little-endian byte order"))
        self.import_conf.setText(_translate("MainWindow", "OK"))
        self.import_cancel.setText(_translate("MainWindow", "Cancel"))
        self.import_help.setText(_translate("MainWindow", "Help"))
        self.label_4.setText(_translate("MainWindow", "Height:"))
        self.height_lineEdit.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "pixels"))
        self.label_6.setText(_translate("MainWindow", "Offset:"))
        self.offset_lineEdit.setText(_translate("MainWindow", "0"))
        self.label_7.setText(_translate("MainWindow", "bytes"))
        self.label_2.setText(_translate("MainWindow", "Width:"))
        self.width_lineEdit.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "pixels"))
        self.label.setText(_translate("MainWindow", "Image type:"))
        self.image_type_comboBox.setItemText(0, _translate("MainWindow", "16-bit Unsigned"))
        self.image_type_comboBox.setItemText(1, _translate("MainWindow", "32-bit Unsigned"))
