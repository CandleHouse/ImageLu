import matplotlib.pyplot as plt
import numpy as np

class Fourier_Spectrum:
    def __init__(self, img):
        self.img = img

    def show_fourier_spectrum(self):
        m, n = self.img.shape
        temp = np.zeros((m, n))
        # 频率中心移动
        for i in range(m):
            for j in range(n):
                temp[i][j] = self.img[i][j] * (-1)**(i+j+2)

        f = np.fft.fft2(temp)
        f_img = np.log(np.abs(f))
        plt.figure()
        plt.imshow(f_img, cmap='gray'), plt.title('Fourier Spectrum'), plt.axis('off')
        plt.show()


if __name__ == '__main__':
    imgData = np.fromfile(r'..\..\image\lumbar.raw', dtype='uint16')
    imgData = imgData[4:].reshape(imgData[2], imgData[0])

    spectrum = Fourier_Spectrum(imgData)
    spectrum.show_fourier_spectrum()

# m, n = imgData.shape
# 快速傅里叶变换算法得到频率分布
# f = np.fft.fft2(imgData)

# 默认结果中心点位置是在左上角,
# 调用fftshift()函数转移到中间位置

# fshift = np.fft.fftshift(f)

# fft结果是复数, 其绝对值结果是振幅
# fimg = np.log(np.abs(fshift))


# # 展示结果
# plt.subplot(131), plt.imshow(imgData, 'gray'), plt.title('Original Fourier')
# plt.axis('off')
# plt.subplot(132), plt.imshow(fimg, 'gray'), plt.title('Fourier Fourier')
# plt.axis('off')
#
# plt.show()