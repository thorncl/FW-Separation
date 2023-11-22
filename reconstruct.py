import numpy as np
from scipy import optimize
import transforms as tr

def get_odd_even_shift(data : np.ndarray, width : int = 2, init : float = 0.1,
              tol : float = 1e-6,
              max_iter : int = 1000) -> float:

    fc = data[128,128]

    f = lambda shift: np.arcsin(np.pi * shift * fc / width) - np.pi * shift / width
    f_prime = lambda shift: (np.pi * fc) / (width * np.sqrt(1 - (np.pi * shift * fc / width)**2))

    return optimize.newton(f, init, fprime = f_prime, tol = tol, maxiter = max_iter)

def reconstruct(data : np.ndarray, shift : float,
                offset : int = 128) -> np.ndarray:

    fft_even, fft_odd = build_odd_even_arrays(data)
    fft_even, fft_odd = even_odd_delay_correction([fft_even, fft_odd], shift, offset)

    return fft_even + fft_odd

def build_odd_even_arrays(data: np.ndarray) -> np.ndarray:

    even, odd = np.zeros_like(data), np.zeros_like(data)
    even[:, 0::2], odd[:, 1::2] = data[:, 0::2], data[:, 1::2]
    return tr.inverse_2d(even), tr.inverse_2d(odd)

def even_odd_delay_correction(ffts : np.ndarray, shift : float,
                     offset : int) -> np.ndarray:

    size = ffts[0].shape[0]
    x, y = np.meshgrid(np.arange(size),np.arange(size))
    ffts[0][x,y] *= np.exp((-1j*2*np.pi*(x-offset)*-shift)/size)
    ffts[1][x,y] *= np.exp((1j*2*np.pi*(x-offset)*-shift)/size)
    return ffts
