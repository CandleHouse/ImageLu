# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detail_enhancement.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(199, 291)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5, 0, QtCore.Qt.AlignRight)
        self.filter_comboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.filter_comboBox.setFont(font)
        self.filter_comboBox.setObjectName("filter_comboBox")
        self.filter_comboBox.addItem("")
        self.filter_comboBox.addItem("")
        self.horizontalLayout_6.addWidget(self.filter_comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.hl_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.hl_lineEdit.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.hl_lineEdit.setFont(font)
        self.hl_lineEdit.setObjectName("hl_lineEdit")
        self.horizontalLayout_2.addWidget(self.hl_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.hh_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.hh_lineEdit.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.hh_lineEdit.setFont(font)
        self.hh_lineEdit.setObjectName("hh_lineEdit")
        self.horizontalLayout_4.addWidget(self.hh_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.c_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.c_lineEdit.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.c_lineEdit.setFont(font)
        self.c_lineEdit.setObjectName("c_lineEdit")
        self.horizontalLayout_3.addWidget(self.c_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.cutoff_freq_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.cutoff_freq_lineEdit.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.cutoff_freq_lineEdit.setFont(font)
        self.cutoff_freq_lineEdit.setObjectName("cutoff_freq_lineEdit")
        self.horizontalLayout.addWidget(self.cutoff_freq_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)
        self.filter_order_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.filter_order_lineEdit.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.filter_order_lineEdit.setFont(font)
        self.filter_order_lineEdit.setObjectName("filter_order_lineEdit")
        self.horizontalLayout_7.addWidget(self.filter_order_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.detail_reset = QtWidgets.QPushButton(self.centralwidget)
        self.detail_reset.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.detail_reset.setFont(font)
        self.detail_reset.setObjectName("detail_reset")
        self.horizontalLayout_5.addWidget(self.detail_reset)
        self.detail_conf = QtWidgets.QPushButton(self.centralwidget)
        self.detail_conf.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.detail_conf.setFont(font)
        self.detail_conf.setObjectName("detail_conf")
        self.horizontalLayout_5.addWidget(self.detail_conf)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 199, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.detail_conf.clicked.connect(MainWindow.detail_enhance_conf) # type: ignore
        self.detail_reset.clicked.connect(MainWindow.detail_enhance_reset) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Detail Enhancement"))
        self.label_5.setText(_translate("MainWindow", "Filter:"))
        self.filter_comboBox.setItemText(0, _translate("MainWindow", "Gaussian"))
        self.filter_comboBox.setItemText(1, _translate("MainWindow", "Butterworth"))
        self.label_2.setText(_translate("MainWindow", "HL:"))
        self.hl_lineEdit.setText(_translate("MainWindow", "0.8"))
        self.label_4.setText(_translate("MainWindow", "HH:"))
        self.hh_lineEdit.setText(_translate("MainWindow", "1.85"))
        self.label_3.setText(_translate("MainWindow", "C:"))
        self.c_lineEdit.setText(_translate("MainWindow", "2"))
        self.label.setText(_translate("MainWindow", "Cut-off Freq:"))
        self.cutoff_freq_lineEdit.setText(_translate("MainWindow", "40"))
        self.label_6.setText(_translate("MainWindow", "Order of Filter:"))
        self.filter_order_lineEdit.setText(_translate("MainWindow", "2"))
        self.detail_reset.setText(_translate("MainWindow", "Reset"))
        self.detail_conf.setText(_translate("MainWindow", "Conf"))