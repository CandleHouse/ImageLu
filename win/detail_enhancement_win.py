from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow

from ui import detail_enhancement
from win.process.retinex import HomomorphicFilter


class Detail_Enhancement(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUI()
        self.__initData()

    def __initData(self):
        self.filter_spectrum = None

    def __initUI(self):
        self.UI = detail_enhancement.Ui_MainWindow()
        self.UI.setupUi(self)
        self.setWindowFlags(Qt.WindowCloseButtonHint)  # 只显示关闭按钮
        self.UI.label_6.setToolTip('For Butterworth Only')
        self.UI.filter_order_lineEdit.setToolTip('For Butterworth Only')

    def action_detail_enhance(self, display_file):
        self.display_obj = display_file  # 保存Display对象

    # 执行图像细节增强操作
    def detail_enhance_conf(self):
        filters = ['gaussian', 'butterworth']
        filter = filters[self.UI.filter_comboBox.currentIndex()]  # 获取选择的滤波器
        HL = float(self.UI.hl_lineEdit.text())  # 低频减益系数
        HH = float(self.UI.hh_lineEdit.text())  # 高频增益系数
        C = float(self.UI.c_lineEdit.text())  # 坡度控制参数
        Cut_off_freq = float(self.UI.cutoff_freq_lineEdit.text())   # 截止频率
        Order_of_filter = float(self.UI.filter_order_lineEdit.text())  # 滤波器阶数

        imgData, width, height = self.display_obj.get_img_np()  # 从Display窗口对象拿到对应图片
        homo_filter = HomomorphicFilter(a=HL, b=HH-HL, c=C)  # HH = 1.85, HL = 0.8
        img_filtered = homo_filter.filter(I=imgData, filter_params=[Cut_off_freq, Order_of_filter], filter=filter)
        self.display_obj.fresh_pic(img_filtered)

        self.filter_spectrum = homo_filter.filter_img  # 获取滤波器频谱

    # 恢复操作
    def detail_enhance_reset(self):
        self.display_obj.display_win_reset()