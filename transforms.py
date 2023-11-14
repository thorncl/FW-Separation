import numpy as np

def forward_2d(data : np.ndarray) -> np.ndarray:

    return kspace_transform(data, np.fft.fftshift, np.fft.fft2, np.fft.ifftshift)

def inverse_2d(data : np.ndarray) -> np.ndarray:

    return kspace_transform(data, np.fft.ifftshift, np.fft.ifft2, np.fft.fftshift)

def kspace_transform(data : np.ndarray, func1 : callable, func2 : callable, 
                     func3 : callable) -> np.ndarray:

    return func1(func2(func3(data)))
