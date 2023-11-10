import matplotlib.pyplot as plt
import numpy as np
import os

def plot_kspace(data : np.ndarray):
    plt.figure()
    plt.imshow(data, cmap='gray')
    plt.colorbar()

def plot_transform(data : np.ndarray):
    plt.figure()
    plt.imshow(np.abs(data),cmap='gray')
    plt.colorbar()

def forward_2D(data : np.ndarray) -> np.ndarray:

    return kspace_transform(data, np.fft.fftshift, np.fft.fft2, np.fft.ifftshift, None, False)

def inverse_2D(data : np.ndarray) -> np.ndarray:

    return kspace_transform(data, np.fft.ifftshift, np.fft.ifft2, np.fft.fftshift, None, False)

def inverse_2D_1D(data : np.ndarray) -> np.ndarray:

    return kspace_transform(np.fft.ifftshift, np.fft.ifft, np.fft.ifft, np.fft.fftshift, True)

def forward_2D_1D(data : np.ndarray) -> np.ndarray:

    return kspace_transform(np.fft.fftshift, np.fft.fft, np.fft.fft, np.fft.ifftshift, True)

def save_data(data : np.ndarray, file_name : str = "sample_data"):

    np.save(os.getcwd() + '\\' + file_name, data)

def kspace_transform(data : np.ndarray, func1, func2, func3, func4, flag_1D : bool) -> np.ndarray:

    return func1(func2(func3(func4(data)))) if flag_1D else func1(func2(func3(data)))