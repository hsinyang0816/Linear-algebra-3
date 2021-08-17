import sys
import numpy as np
import os

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plot_wave(x, path = './wave.png'):
    plt.gcf().clear()
    plt.plot(x)
    plt.xlabel('n')
    plt.ylabel('xn')
    plt.savefig(path)

def plot_ak(a, path = './freq.png'):
    plt.gcf().clear()

    # Only plot the mag of a
    a = np.abs(a)
    plt.plot(a)
    plt.xlabel('k')
    plt.ylabel('ak')
    plt.savefig(path)

def CosineTrans(x, B):
    # TODO
    # implement cosine transform
    a = np.dot(B, x)
    return a

def InvCosineTrans(a, B):
    # TODO
    # implement inverse cosine transform
    x = np.dot(np.linalg.inv(B), a)
    return x

def gen_basis(N):
    # TODO
    B = np.zeros((N, N))
    for i in range(N):
        B[i][0] = 1 / np.sqrt(N)
    for n in range(N):
        for k in range(1, N):
            B[n][k] = (np.sqrt(2)/np.sqrt(N)) * np.cos((n + 0.5) * k * np.pi / N)
    return B

if __name__ == '__main__':
    # Do not modify these 2 lines
    signal_path = sys.argv[1]
    out_directory_path = sys.argv[2]
    
    # TODO
    x = []
    f = open(signal_path)
    file_as_list = f.readlines()
    for line in file_as_list:
        x.append(float(line))
    x = np.array(x)
    x = x.reshape((1000, 1))
    B = gen_basis(x.shape[0])
    a = InvCosineTrans(x, B)
    temp = []
    for i in range(a.shape[0]):
        if abs(a[i]) > 12.8:
            temp.append(i)
    mask_f1 = np.zeros((1000, 1))
    mask_f3 = np.zeros((1000, 1))
    mask_f1[temp[0]] = a[temp[0]]
    mask_f3[temp[2]] = a[temp[2]]
    # print(mask_f1)
    f1 = CosineTrans(mask_f1, B)
    f3 = CosineTrans(mask_f3, B)
    # print(temp)
    # Do not modify these 3 lines
    plot_ak(a, path=os.path.join(out_directory_path, 'freq.png'))
    plot_wave(f1, path=os.path.join(out_directory_path, 'f1.png'))
    plot_wave(f3, path=os.path.join(out_directory_path, 'f3.png'))

