# Homomorphic filter class
import matplotlib.pyplot as plt
import numpy as np


class HomomorphicFilter:
    def __init__(self, a=0.5, b=1.5, c=2):
        # 滤波器权重 H = a + b*H
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)
        self.filter_img = None  # 保存选定的滤波器用于展示

    # 滤波器
    def __butterworth_filter(self, I_shape, filter_params):
        P = I_shape[0] / 2
        Q = I_shape[1] / 2
        U, V = np.meshgrid(range(I_shape[0]), range(I_shape[1]), sparse=False, indexing='ij')
        Duv = ((U - P) ** 2 + (V - Q) ** 2).astype(float)
        H = 1 / (1 + (Duv / filter_params[0] ** 2) ** filter_params[1])
        return (1 - H)

    def __gaussian_filter(self, I_shape, filter_params):
        P = I_shape[0] / 2
        Q = I_shape[1] / 2
        H = np.zeros(I_shape)
        U, V = np.meshgrid(range(I_shape[0]), range(I_shape[1]), sparse=False, indexing='ij')
        Duv = ((U - P) ** 2 + (V - Q) ** 2)
        H = np.exp(self.c*(-Duv / ((filter_params[0]) ** 2)))
        return (1 - H)

    def __apply_filter(self, I, H):
        self.filter_img = (self.a + self.b * H)  # 用于展示滤波器频谱

        H = np.fft.fftshift(H)
        I_filtered = (self.a + self.b * H) * I
        return I_filtered

    # 主滤波操作
    def filter(self, I, filter_params, filter='gaussian', H=None):
        """
        butterworth:
            filter_params[0]: Cutoff frequency
            filter_params[1]: Order of filter
        gaussian:
            filter_params[0]: Cutoff frequency
        """
        #  Validating image
        if len(I.shape) is not 2:
            raise Exception('Improper image')

        # log(1+I)，并转换到频域
        I_log = np.log1p(np.array(I, dtype="float"))
        I_fft = np.fft.fft2(I_log)

        # 获得滤波器
        if filter == 'butterworth':
            H = self.__butterworth_filter(I_shape=I_fft.shape, filter_params=filter_params)
        elif filter == 'gaussian':
            H = self.__gaussian_filter(I_shape=I_fft.shape, filter_params=filter_params)
        elif filter == 'external':
            print('external')
            if len(H.shape) is not 2:
                raise Exception('Invalid external filter')
        else:
            raise Exception('Selected filter not implemented')

        # 频域内完成乘积并转换为空间域
        I_fft_filt = self.__apply_filter(I=I_fft, H=H)
        I_filt = np.fft.ifft2(I_fft_filt)
        I = np.exp(np.real(I_filt)) - 1

        # 归一化到 4095 uint16格式
        interval = np.max(I) - np.min(I)
        outcome = (4095 * (I-np.min(I)) / interval).astype(np.uint16)
        return outcome


if __name__ == '__main__':
    imgData = np.fromfile(r'..\..\image\lumbar.raw', dtype='uint16')
    imgData = imgData[4:].reshape(imgData[2], imgData[0])
    homo_filter = HomomorphicFilter(a=0.8, b=1)  # HH = 1.8, HL = 0.8
    img_filtered = homo_filter.filter(I=imgData, filter_params=[40, 2])

    # plt.imshow(img_filtered, cmap='gray')
    # plt.show()

    m, n = imgData.shape
    filename = r'..\..\image\retinex.raw'
    with open(filename, 'w') as f:
        image = img_filtered.flatten()  # 插入数据必须要打平
        info = np.array([n, 0, m, 0], dtype='uint16')  # 以 uint16 格式准备长宽
        image = np.append(info, image, axis=0)  # 在image的 0 位置插入 info
        image.tofile(filename)