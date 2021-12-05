import os
import numpy as np
from PIL import Image

from PyQt5.QtCore import QFileInfo, QPoint
from PyQt5.QtGui import QPixmap, QFont, QTransform
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui

from ui import display


# 图片窗口
class Display(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initData()
        self.__initUI()

    def __initData(self):
        self.scale = 0.4  # 初始缩放比例
        self.start_pos = None  # 光标开始位置
        self.end_pos = None  # 光标结束位置
        self.point = QPoint(0, 0)  # 累加坐标点
        self.left_click = False  # 左键默认未点击
        self.offset = 4  # 默认图像为 uint16, 往后 8字节开始读

    def __initUI(self):
        self.UI = display.Ui_MainWindow()
        self.UI.setupUi(self)
        # 更改字体和背景
        self.UI.info.setFont(QFont("Microsoft YaHei"))
        self.setStyleSheet('''QWidget{background-color:rgb(255, 255, 255);}''')
        self.UI.verticalLayoutWidget.setMouseTracking(True)

    def get_img_np(self):
        return self.img_np, self.width, self.height

    def display_func(self, openfile_name, open_parameter=None):
        # 用 display window 打开图片
        if open_parameter is not None:
            imgData = np.fromfile(openfile_name, dtype=open_parameter['image_type'])
            if open_parameter['while_is_zero']:
                imgData = 4095 - imgData
            self.width, self.height = open_parameter['width'], open_parameter['height']
            offset = open_parameter['offset']  # bytes
            if open_parameter['image_type'] == 'uint16':
                self.offset = offset // 2
                self.bit_resolution = '16-bit'
            elif open_parameter['image_type'] == 'uint32':
                self.offset = offset // 4
                self.bit_resolution = '32-bit'
        # 拖拽打开的图片
        else:
            imgData = np.fromfile(openfile_name, dtype='uint16')
            self.width, self.height = imgData[0], imgData[2]
            self.bit_resolution = '16-bit'

        # 图像比较小就直接显示
        if self.width < 1000 and self.height < 1000:
            self.scale = 1

        width = self.width * self.scale  # 宽
        height = self.height * self.scale  # 高
        arr = imgData[self.offset:].reshape(self.height, self.width)

        self.UI.verticalLayoutWidget.resize(width+10, height+25)  # 重置水平布局宽高
        self.UI.pic.resize(width, height)  # 重置图像显示宽高
        self.resize(self.UI.verticalLayoutWidget.size())  # 重置窗口宽高

        # 准备图片，设置为 QPixmap
        img = (arr - arr.min()) / (arr.max() - arr.min()) * 255.
        img = img.astype(np.uint8)
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # 彩色
        temp_img = Image.fromarray(img).toqpixmap()  # 为了缩放，需要保存 未调整大小 的 映射后的数据
        pixImg = QPixmap(temp_img).scaled(self.UI.pic.width(), self.UI.pic.height())
        self.UI.pic.setPixmap(pixImg)

        # 设置 title 与 info
        self.filename = os.path.basename(openfile_name)
        zoom_size = '({:.1f}%)'.format(self.scale*100)
        self.setWindowTitle(self.filename+' '+zoom_size)
        self.UI.info.setText('{}×{} pixels; {}; {:.1f}MB'
                             .format(self.width, self.height, self.bit_resolution,
                                     QFileInfo(openfile_name).size()/(1024*1024)))
        # 每个窗口单独保存自己的numpy格式图片信息
        self.img_np = arr
        self.temp_img_np = arr  # 备份图片，用于reset
        self.img_uint8 = img  # 保存 display 图片用于滚轮缩放，避免重复计算
        # 打开时保存当前图像的缩放尺寸
        self.zoom_width, self.zoom_height = self.width*self.scale, self.height*self.scale

    # 接管如 wl_hist 和 detail_enhance 的更新图片的操作
    def fresh_pic(self, arr):
        self.img_np = arr  # 时刻保存当前结果
        img = (arr - arr.min()) / (arr.max() - arr.min()) * 255.
        img = img.astype(np.uint8)
        self.img_uint8 = img  # 刷新时重新保存 display 图片
        img = Image.fromarray(img)
        img = img.toqpixmap()
        pixImg = QPixmap(img).scaled(self.UI.pic.width(), self.UI.pic.height())
        self.UI.pic.setPixmap(pixImg)

    # 滚轮放大
    def wheelEvent(self, event):
        self.UI.pic.setScaledContents(False)  # 取消自适应
        angle = event.angleDelta() / 8  # 返回QPoint对象，为滚轮转过的数值，单位为1/8度
        angleY = angle.y()
        # 获取当前鼠标相对于view的位置
        if angleY > 0:
            self.scale *= 1.1
        else:  # 滚轮下滚
            self.scale *= 0.9

        self.zoom_width, self.zoom_height = self.width*self.scale, self.height*self.scale  # 更新新缩放尺寸
        # self.UI.verticalLayoutWidget.resize(self.zoom_width+10, self.zoom_height+25)  # 重置水平布局宽高
        self.UI.pic.resize(self.zoom_width, self.zoom_height)  # 重置图像显示宽高
        # 重置图像大小，Qt.SmoothTransformation指定使用双线性插值
        img = Image.fromarray(self.img_uint8).toqpixmap()
        pixImg = QPixmap(img).scaled(self.UI.pic.width(), self.UI.pic.height(), transformMode=Qt.SmoothTransformation)
        self.UI.pic.setPixmap(pixImg)
        self.setWindowTitle(self.filename+' '+'({:.1f}%)'.format(self.scale*100))  # 修改缩放比例

        self.point = QPoint(0, 0)  # 使得每次缩放后，移动距离不继承

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.left_click = True
            self.start_pos = e.pos()
        # 右击恢复缩放的图像
        elif e.button() == Qt.RightButton:
            self.display_win_reset()

    # 单独写reset函数，使得缩放也可以使用
    def display_win_reset(self):
        self.UI.pic.setScaledContents(False)  # 取消自适应
        self.scale = 0.4  # 恢复为原始比例
        if self.width < 1000 and self.height < 1000:
            self.scale = 1
        self.zoom_width, self.zoom_height = self.width * self.scale, self.height * self.scale  # 更新新缩放尺寸
        self.UI.pic.resize(self.zoom_width, self.zoom_height)  # 重置图像显示宽高
        # 重置图像大小，Qt.SmoothTransformation指定使用双线性插值
        arr = self.temp_img_np  # 用保存的 np 原图像格式恢复
        img = (arr - arr.min()) / (arr.max() - arr.min()) * 255.
        img = img.astype(np.uint8)
        self.img_uint8 = img  # 刷新时重新保存 display 图片
        img = Image.fromarray(img).toqpixmap()
        pixImg = QPixmap(img).scaled(self.UI.pic.width(), self.UI.pic.height(), transformMode=Qt.SmoothTransformation)
        self.UI.pic.setPixmap(pixImg)  # 注意使用setPixmap后QLabel标签会自动填充初始位置
        self.img_np = self.temp_img_np  # 恢复为保存的图像
        self.setWindowTitle(self.filename + ' ' + '({:.1f}%)'.format(self.scale * 100))  # 修改缩放比例
        self.point = QPoint(0, 0)  # 使得每次缩放后，移动距离不继承

    def mouseMoveEvent(self, e):
        # 监听鼠标位置，显示当前像素值
        x_pos = int(min(max((e.pos().x()-5-self.point.x())//self.scale, 0), self.width-1))
        y_pos = int(min(max((e.pos().y()-20-self.point.y())//self.scale, 0), self.height-1))
        self.setWindowTitle(self.filename + ' ' + '({:.1f}%)'.format(self.scale * 100) + '; x={}, y={}, value={}'
                            .format(x_pos, y_pos, self.img_np[y_pos][x_pos]))
        # 拖拽图像
        if self.left_click:
            self.end_pos = e.pos() - self.start_pos
            self.point = self.point + self.end_pos
            self.start_pos = e.pos()

            self.UI.pic.setGeometry(QtCore.QRect(self.point.x(), self.point.y(), self.zoom_width, self.zoom_height))
            self.UI.pic.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.left_click = False
            self.UI.pic.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))

    # verticalLayoutWidget大小与window一致，使得当图像比窗口小时，仍能够自由移动
    def resizeEvent(self, event):
        self.UI.pic.setScaledContents(False)  # 取消自适应
        self.UI.verticalLayoutWidget.resize(event.size())