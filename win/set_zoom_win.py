from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore

from ui import set_zoom


class Set_Zoom(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUI()
        self.__initData()

    def __initData(self):
        pass

    def __initUI(self):
        self.UI = set_zoom.Ui_MainWindow()
        self.UI.setupUi(self)
        self.setWindowFlags(Qt.WindowCloseButtonHint)  # 只显示关闭按钮
        self.UI.zoom_label.setFont(QFont("Microsoft YaHei"))
        self.UI.xcenter_label.setFont(QFont("Microsoft YaHei"))
        self.UI.ycenter_label.setFont(QFont("Microsoft YaHei"))

    # 从 menuBar 转入，暂存图片信息，等待确定调用
    def action_set_zoom(self, display_file):
        self.display_obj = display_file  # 保存Display对象

    def zoom_conf(self):
        self.zoom = float(self.UI.zoom_lineEdit.text())/100  # 获取缩放比例
        self.xcenter = int(self.UI.xcenter_lineEdit.text())  # 获取缩放中心x
        self.ycenter = int(self.UI.ycenter_lineEdit.text())  # 获取缩放中心y

        # 拿 Display的所有数据操作，只有上面三个变量是自己的
        self.display_obj.zoom_width, self.display_obj.zoom_height =\
            self.display_obj.width*self.zoom, self.display_obj.height*self.zoom  # 更新新缩放尺寸
        self.display_obj.UI.pic.resize(self.display_obj.zoom_width, self.display_obj.zoom_height)  # 重置图像显示宽高
        # pixImg = QPixmap(self.display_obj.temp_img).scaled(self.display_obj.UI.pic.width(), self.display_obj.UI.pic.height())  # 重置图像大小
        # self.display_obj.UI.pic.setPixmap(pixImg)

        # 由于setPixmap会回到初始化位置，所以采用pic自适应来跳过setPixmap，相应的滚轮缩放等需要移动的操作都要取消自适应

        self.display_obj.UI.pic.setScaledContents(True)
        self.display_obj.UI.pic.setGeometry(QtCore.QRect(self.display_obj.size().width()//2-self.xcenter*self.zoom,
                                                         self.display_obj.size().height()//2-self.ycenter*self.zoom,
                                                         self.display_obj.zoom_width, self.display_obj.zoom_height))

        self.display_obj.setWindowTitle(self.display_obj.filename+' '+'({:.1f}%)'.format(self.zoom*100))  # 修改缩放比例
        self.display_obj.scale = self.zoom  # 修改原图缩放比例参数

    def zoom_reset(self):
        self.UI.zoom_lineEdit.setText(str(int(self.display_obj.scale*100)))
        self.UI.xcenter_lineEdit.setText(str(0))
        self.UI.ycenter_lineEdit.setText(str(0))
        # 调用display_win中的重置函数
        self.display_obj.display_win_reset()
