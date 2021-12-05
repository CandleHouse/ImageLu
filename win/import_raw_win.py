import numpy as np
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from ui import import_raw
from win.display_win import Display


class Import_Raw(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUI()
        self.__initData()

    def __initData(self):
        self.open_parameter = {}  # 包含所有选择的参数
        self.open_parameter['open_mode'] = 'use_options'  # 设置打开方式
        self.openfile_name = ''
        self.display = Display()  # 返回给menuBar

    def __initUI(self):
        self.UI = import_raw.Ui_MainWindow()
        self.UI.setupUi(self)

    def import_help(self):
        msg_box = QMessageBox(QMessageBox.Question, 'Tips', 'No one can help you!')
        msg_box.exec_()

    # 打开界面显示的内容
    def open_settings(self, openfile_name):
        self.openfile_name = openfile_name
        # 以 uint16 查找宽高，写入lineEdit，如果不是，用户自行修改
        imgData = np.fromfile(openfile_name, dtype='uint16')
        self.open_parameter['width'] = imgData[0]  # 宽
        self.open_parameter['height'] = imgData[2]  # 高
        self.UI.width_lineEdit.setText(str(self.open_parameter['width']))
        self.UI.height_lineEdit.setText(str(self.open_parameter['height']))

        return self.display

    # 点击 import Conf 确认按钮触发
    def set_info(self):
        # image_type: 0. uint16; 1. uint32
        image_type = self.UI.image_type_comboBox.currentIndex()
        # 图像格式
        if image_type == 0:
            self.open_parameter['image_type'] = 'uint16'
        elif image_type == 1:
            self.open_parameter['image_type'] = 'uint32'

        # 更新宽与高
        self.open_parameter['width'] = int(self.UI.width_lineEdit.text())
        self.open_parameter['height'] = int(self.UI.height_lineEdit.text())
        self.open_parameter['offset'] = int(self.UI.offset_lineEdit.text())

        # 获得combobox
        self.open_parameter['while_is_zero'] = self.UI.white_zero_checkBox.isChecked()
        self.open_parameter['little_endian'] = self.UI.little_endian_checkBox.isChecked()

        # 关闭窗口
        self.close()

        self.display.display_func(self.openfile_name, self.open_parameter)
        self.display.show()