import re
import sys

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

from win.detail_enhancement_win import Detail_Enhancement
from win.display_win import Display
from win.import_raw_win import Import_Raw
from win.process.others import Others
from win.process.fourier_spectrum import Fourier_Spectrum
from win.set_zoom_win import Set_Zoom
from win.wl_hist_win import WL_Hist

from ui import menuBar

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon


# 工具栏
class MenuBar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initData()
        self.__initUI()

    def __initData(self):
        # 统计文件数量，满足 打开多张files 和 连续打开i
        self.files, self.i = [], 0
        self.setAcceptDrops(True)

    def __initUI(self):
        self.UI = menuBar.Ui_MainWindow()
        self.UI.setupUi(self)

    # 普通打开图片
    def openfile(self):
        # 自行选择的路径，不存贮
        openfile_names = QFileDialog.getOpenFileNames(self, '选择医学 RAW 图像', '', '*.raw')
        # [0] 是文件名路径集合
        for openfile_name in openfile_names[0]:
            self.files.append(Display())
            self.files[self.i].display_func(openfile_name)
            self.files[self.i].show()
            self.i += 1

    # 保存文件 -原格式，需要保留图片宽高
    def savefile(self):
        filename = QFileDialog.getSaveFileName(self, '保存为医学 RAW 图像', '', '*.raw')
        # [0] 为自定义保存文件名称路径
        with open(filename[0], 'w') as f:
            imgData, width, height = self.files[self.i-1].get_img_np()
            image = imgData.flatten()  # 插入数据必须要打平
            info = np.array([width, 0, height, 0], dtype='uint16')  # 以 uint16 格式准备长宽
            image = np.append(info, image, axis=0)  # 在image的 0 位置插入 info
            image.tofile(filename[0])

    # 单独处理拖拽打开的图片
    def drag_open(self, openfile_name):
        if self.UI.import_checkBox.isChecked():
            self.files.append(Display())
            self.files[self.i].display_func(openfile_name)
            self.files[self.i].show()
            self.i += 1
        else:
            self.import_raw = Import_Raw()
            display = self.import_raw.open_settings(openfile_name)
            self.import_raw.show()
            # 把 import 申明的 Display 加入打开队列
            self.files.append(display)
            self.i += 1

    # 是否接受拖拽
    def dragEnterEvent(self, e):
        # 单文件拖拽
        filename = e.mimeData().text()
        # 多文件拖拽
        filenames = re.split(r'[\n\t]', e.mimeData().text())[0:-1]
        if filename.endswith('.raw'):
            e.accept()
        else:
            for name in filenames:
                if name.endswith('.raw'):
                    e.accept()
                else:
                    e.ignore()

    # 释放显示
    def dropEvent(self, e):
        # 单文件拖拽
        filename = e.mimeData().text()
        # 多文件拖拽
        filenames = re.split(r'[\n\t]', e.mimeData().text())[0:-1]
        if filename.endswith('.raw'):
            self.drag_open(filename[8:])  # 获取文件绝对路径
        else:
            for name in filenames:
                if name.endswith('.raw'):
                    self.drag_open(name[8:])

    # 调整图像窗宽窗位
    def wl_hist(self):
        self.wl_hist = WL_Hist()
        # 传入当前操作的窗口对象，图片在窗口中保存
        self.wl_hist.action_wl_hist(self.files[self.i-1])
        self.wl_hist.show()

    # 图像缩放，指定参数
    def set_zoom(self):
        self.set_zoom = Set_Zoom()
        self.set_zoom.action_set_zoom(self.files[self.i-1])
        self.set_zoom.show()

    # 图像细节增强
    def detail_enhancement(self):
        self.detail_enhancement = Detail_Enhancement()
        self.detail_enhancement.action_detail_enhance(self.files[self.i-1])
        self.detail_enhancement.show()

    # 展示 Fourier Spectrum
    def show_fourier_spectrum(self):
        imgData, width, height = self.files[self.i-1].get_img_np()
        spectrum = Fourier_Spectrum(imgData)
        spectrum.show_fourier_spectrum()

    # 展示 滤波器频谱
    def show_filter_spectrum(self):
        # 获取传递来的滤波器
        plt.figure()
        plt.imshow(self.detail_enhancement.filter_spectrum, cmap='gray')
        plt.show()

    # 以下为其他功能：
    # 拉普拉斯算子
    def action_laplacian(self):
        other = Others()
        imgData, width, height = self.files[self.i-1].get_img_np()
        outImg = other.laplacianSharpen(imgData, 1.2, median_filter=True)  # 使用中值滤波，否则图像噪声敏感
        self.files[self.i-1].fresh_pic(outImg)

    # 中值滤波
    def action_median_filter(self):
        other = Others()
        imgData, width, height = self.files[self.i-1].get_img_np()
        outImg = other.median_filter(imgData, kernel_size=9)
        self.files[self.i-1].fresh_pic(outImg)

    # 线性变换
    def action_line_transfer(self):
        other = Others()
        imgData, width, height = self.files[self.i-1].get_img_np()
        outImg = other.line_transfer(imgData, scale=1.1)
        self.files[self.i-1].fresh_pic(outImg)

    # γ 变换
    def action_gama_transfer(self):
        other = Others()
        imgData, width, height = self.files[self.i-1].get_img_np()
        outImg = other.gama_transfer(imgData, power1=1.5)
        self.files[self.i-1].fresh_pic(outImg)

    # 分段线性分割
    def action_seg_augment(self):
        other = Others()
        imgData, width, height = self.files[self.i-1].get_img_np()
        outImg = other.seg_augment_img(imgData, 50, 0.5, 150, 3.6, -310, 0.238, 194)  # 参数详见 Others() 类定义
        self.files[self.i-1].fresh_pic(outImg)

    # 直方图均衡化
    def action_histogram_equalization(self):
        other = Others()
        imgData, width, height = self.files[self.i-1].get_img_np()
        arr = imgData
        img = (arr - arr.min()) / (arr.max() - arr.min()) * 255.
        img = img.astype(np.uint8)
        outImg = other.cal_equalhist(img)
        self.files[self.i-1].fresh_pic(outImg)

    # 腐蚀
    def action_erode_img(self):
        other = Others()
        imgData, width, height = self.files[self.i-1].get_img_np()
        outImg = other.erode_img(imgData)
        self.files[self.i-1].fresh_pic(outImg)

    # 扩张
    def action_dilate_img(self):
        other = Others()
        imgData, width, height = self.files[self.i-1].get_img_np()
        outImg = other.dilate_img(imgData)
        self.files[self.i-1].fresh_pic(outImg)

    # 使用腐蚀扩张进行边界划分
    def action_divide_border(self):
        other = Others()
        imgData, width, height = self.files[self.i-1].get_img_np()
        outImg = other.divide_border(imgData)
        self.files[self.i-1].fresh_pic(outImg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon/24gf-pictures.png"))

    menu_bar = MenuBar()
    menu_bar.show()

    sys.exit(app.exec_())