import numpy as np
import transforms as tr
import os

def save_data(data: np.ndarray, file_name: str = "ClareArray2") -> None:

    np.save(os.getcwd() + '\\' + file_name, data)

def load_data(file_name: str) -> None:

    np.load(file_name)

def get_shift(data: np.ndarray, width) -> float:

    fc = data[128,128]

    def equation(shift: float) -> callable:
        return np.arcsin(np.pi*shift*fc/width) - np.pi*shift/width
    
    def newton(equation: callable, derivative: callable, init: float = 0.1, tolerance: float = 1e-6, max_iter: int = 1000) -> float:
        shift = init
        for i in range(max_iter):
            shift = shift - equation(shift) / derivative(shift)
            if np.abs(equation(shift)) < tolerance:
                return shift

    def derivative(shift) -> callable:
        return (np.pi * fc) / (width * np.sqrt(1 - (np.pi * shift * fc / width)**2))

    return newton(equation, derivative)

def reconstruct(data: np.ndarray, shift: float, offset: int) -> np.ndarray:

    size = int(data.shape[0])

    even = np.zeros_like(data)
    odd = np.zeros_like(data)

    even[:,0::2] = data[:,0::2]
    odd[:,1::2] = data[:,1::2]

    fft_even = tr.inverse_2D(even)
    fft_odd = tr.inverse_2D(odd)

    for x in range(fft_even.shape[0]):
        for y in range(fft_odd.shape[0]):
            fft_even[x,y] *= np.exp((-1j*2*np.pi*(x-offset)*-shift)/size)
            fft_odd[x,y] *= np.exp((1j*2*np.pi*(x-offset)*-shift)/size)

    reconstruction = fft_odd + fft_even

    return reconstruction