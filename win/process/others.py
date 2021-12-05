import math

import cv2
import numpy as np
import scipy.signal as signal


class Others:
    def __init__(self):
        pass

    # 拉普拉斯算子
    def laplacianSharpen(self, img, alpha=1.2, median_filter=True):
        if median_filter:
            img = signal.medfilt2d(np.array(img), kernel_size=3)  # 二维中值滤波
        k = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) + alpha * np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
        # k = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        # k = np.array([[0.0625, 0.125, 0.0625],[0.125, 0.25, 0.125],[0.0625, 0.125, 0.0625]])
        dst = cv2.filter2D(img, -1, k)

        return dst

    # 中值滤波
    def median_filter(self, img, kernel_size=3):
        outImg = signal.medfilt2d(np.array(img), kernel_size=kernel_size)
        return outImg

    # 线性变换
    def line_transfer(self, img, scale=1.1):
        out = scale * img
        out[out > 4095] = 4095
        return out

    # γ 变换
    def gama_transfer(self, img, power1=1.5):
        img = 4095 * np.power(img / 4095, power1)
        img = np.around(img)
        img[img > 4095] = 4095
        return img

    # 分段线性分割
    def seg_augment_img(self, img, start, c1, end, c2, b2, c3, b3):
        out_img = np.zeros(img.shape)
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if img[i][j] < start:
                    out_img[i][j] = img[i][j] * c1
                elif img[i][j] < end:
                    out_img[i][j] = img[i][j] * c2 + b2
                else:
                    out_img[i][j] = img[i][j] * c3 + b3

        out_img[out_img > 4095] = 4095
        return out_img

    # 直方图均衡化
    def cal_equalhist(self, img):
        h, w = img.shape
        grathist = cv2.calcHist([img], [0], None, [256], [0, 255])

        zerosumMoment = np.zeros([256], np.uint32)
        for p in range(256):
            if p == 0:
                zerosumMoment[p] = grathist[0]
            else:
                zerosumMoment[p] = zerosumMoment[p - 1] + grathist[p]

        output_q = np.zeros([256], np.uint8)
        cofficient = 256.0 / (h * w)
        for p in range(256):
            q = cofficient * float(zerosumMoment[p]) - 1
            if q >= 0:
                output_q[p] = math.floor(q)
            else:
                output_q[p] = 0

        equalhistimage = np.zeros(img.shape, np.uint8)
        for i in range(h):
            for j in range(w):
                equalhistimage[i][j] = output_q[img[i][j]]

        return equalhistimage

    # 膨胀
    def erode_img(self, img):
        kernel = np.ones((5, 5), np.uint8)
        erosion = cv2.erode(img, kernel, iterations=1)
        return erosion

    # 扩张
    def dilate_img(self, img):
        kernel = np.ones((5, 5), np.uint8)
        dilation = cv2.dilate(img, kernel, iterations=1)
        return dilation

    # 使用腐蚀扩张进行边界划分
    def divide_border(self, img):
        kernel = np.ones((5, 5), np.uint8)
        dilation = cv2.dilate(img, kernel, iterations=1)
        erosion = cv2.erode(img, kernel, iterations=1)
        absdiff_img = cv2.absdiff(dilation, erosion)
        return absdiff_img