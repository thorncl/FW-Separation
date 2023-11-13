import numpy as np
import matplotlib.pyplot as plt
import reconstruct as re

def import_data(file_path):
    data = np.load(file_path)
    fft = np.fft.fftshift(np.fft.ifft2(np.fft.fftshift(data)))
    return data, fft

def build_even_odd(data):
    even = np.zeros_like(data)
    odd = np.zeros_like(data)

    even[:,0::2] = data[:,0::2]
    odd[:,1::2] = data[:,1::2]

    fft_even = np.fft.fftshift(np.fft.ifft2(np.fft.fftshift(even)))
    fft_odd = np.fft.fftshift(np.fft.ifft2(np.fft.fftshift(odd)))

    return fft_even, fft_odd

def recon(fft_even, fft_odd,shift):
    for x in range(256):
        for y in range(256):
            fft_even[x,y] *= np.exp((-1j*2*np.pi*(x-128)*-shift)/256)
            fft_odd[x,y] *= np.exp((1j*2*np.pi*(x-128)*-shift)/256)

    return fft_even + fft_odd

def imshow(i):
    plt.imshow(np.concatenate((np.real(i),np.imag(i)),axis=1))
    plt.colorbar()

def main():

    data, fft = import_data("ClareArray2.npy")
    return data, fft

if __name__ == '__main__':
    
    data, fft = main()
    fft_even, fft_odd = build_even_odd(data)
    shift = re.get_shift(data,2)
    recon = recon(fft_even,fft_odd,shift)

    plt.figure()
    imshow(recon)
    