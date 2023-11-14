import numpy as np
import transforms as tr
import reconstruct as re
from kspace import params, kspace_data
import matplotlib.pyplot as plt

def main():

    kx_params = params(1.0,2.0,128.0,0.9,2.0,np.sinc)
    ky_params = params(1.0,2.0,128.0,0,0,np.sinc)

    datas = kspace_data(kx_params,ky_params)
    data = datas.data

    ffts = tr.inverse_2D(data)

    re.save_data(data)

    shift = re.get_shift(data)
    recon = re.reconstruct(data,shift,128)

    return data, ffts, shift, recon

if __name__ == '__main__':
    data, fft, shift, recon = main()