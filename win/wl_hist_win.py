import numpy as np
from PyQt5.QtWidgets import QMainWindow
from matplotlib import pyplot as plt
from numpy import histogram

from ui import wl_hist
import pyqtgraph as pg


# 窗宽窗位和直方图窗口
class WL_Hist(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUI()  # 先装 UI 才有数据
        self.__initData()

    def __initData(self):
        self.window_level = self.UI.level_slider.value()  # 窗位
        self.windowing = self.UI.window_slider.value()  # 窗宽

    def __initUI(self):
        self.UI = wl_hist.Ui_MainWindow()
        self.UI.setupUi(self)
        # 更改背景
        self.setStyleSheet('''QWidget{background-color:rgb(255, 255, 255);}''')

    # 绘制当前图像的直方图
    def action_wl_hist(self, display_file):
        self.display_obj = display_file  # 保存Display对象
        imgData, width, height = display_file.get_img_np()  # 从Display窗口对象拿到对应图片
        self.imgData = imgData  # 注意wl_hist中imgData只保存一开始的图像，更新在display_win
        arr = imgData.flatten()
        nx, xbins, patchs = plt.hist(arr, 50)  # nx:每个bin的元素数量，xbins:每个bin的区间范围，patchs:每个bin包含的数据
        bar = pg.BarGraphItem(x=xbins[0:50], height=nx, width=xbins[1]-xbins[0])

        self.UI.hist_view.addItem(bar)

    # lineEdit显示窗位
    def level_changed(self):
        self.window_level = self.UI.level_slider.value()  # int类型
        self.UI.level_lineEdit.setText(str(self.window_level))
        self.adjust_pic()

    # lineEdit设置窗位
    def lineEdit_level(self):
        self.window_level = int(self.UI.level_lineEdit.text())
        self.UI.level_slider.setValue(self.window_level)
        self.adjust_pic()

    # 显示窗宽
    def window_changed(self):
        self.windowing = self.UI.window_slider.value()  # int类型
        self.UI.window_lineEdit.setText(str(self.windowing))
        self.adjust_pic()

    # 设置窗宽
    def lineEdit_window(self):
        self.windowing = int(self.UI.window_lineEdit.text())
        self.UI.window_slider.setValue(self.windowing)
        self.adjust_pic()

    # 调整并显示
    def adjust_pic(self):
        # 修改显示的图像
        img = self.imgData.copy()
        max_, min_ = np.max(self.imgData), np.min(self.imgData)  # 0 - 4095
        interval_min = max(min_, self.window_level - self.windowing//2)
        interval_max = min(max_, self.window_level + self.windowing//2)
        img[img < interval_min] = interval_min
        img[img > interval_max] = interval_max

        self.display_obj.fresh_pic(img)

        # 修改hist
        arr = img.flatten()
        # nx, xbins, patchs = plt.hist(arr, 50)  # nx:每个bin的元素数量，xbins:每个bin的区间范围，patchs:每个bin包含的数据
        nx, xbins = histogram(arr, 50)  # numpy少返回一个patchs，直方图更快一些
        bar = pg.BarGraphItem(x=xbins[0:50], height=nx, width=xbins[1]-xbins[0], color='g')
        self.UI.hist_view.clear()
        self.UI.hist_view.addItem(bar)

    # 重置
    def reset_wl_hist(self):
        self.window_level = 2048
        self.UI.level_lineEdit.setText(str(self.window_level))
        self.UI.level_slider.setValue(self.window_level)
        self.windowing = 4096
        self.UI.window_lineEdit.setText(str(self.windowing))
        self.UI.window_slider.setValue(self.windowing)

        self.adjust_pic()