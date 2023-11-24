import numpy as np

def forward_2d(data : np.ndarray) -> np.ndarray:

    return kspace_transform(data, np.fft.fftshift, np.fft.fft2, np.fft.ifftshift)

def inverse_2d(data : np.ndarray) -> np.ndarray:

    return kspace_transform(data, np.fft.ifftshift, np.fft.ifft2, np.fft.fftshift)

def forward_1d(data : np.ndarray, axis : int) -> np.ndarray:

    return kspace_transform(data, np.fft.fftshift, np.fft.fft, np.fft.ifftshift, axis)

def inverse_1d(data : np.ndarray, axis : int) -> np.ndarray:

    return kspace_transform(data, np.fft.ifftshift, np.fft.ifft, np.fft.fftshift, axis)

def kspace_transform(data : np.ndarray, func1 : callable, func2 : callable, 
                     func3 : callable, axis : int | None = None) -> np.ndarray:

    return func1(func2(func3(data), axis = axis)) if axis is not None else func1(func2(func3(data)))
