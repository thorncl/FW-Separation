import numpy as np
import transforms as tr
from kspace import params, kspace_data

def main():

    # kx_params = kspace_params(1.0,2,128,0.0,0,np.sinc)
    # ky_params = kspace_params(1.0,2,128,0.0,0,np.sinc)

    # shifted_data_kx = kspace(kx_params,ky_params)
    # shifted_data = shifted_data_kx.data

    kx_params = params(1.0,2,128,0.3,2,np.sinc)
    ky_params = params(1.0,2,128,0.0,0,np.sinc)

    shifted_data_kx = kspace_data(kx_params,ky_params)
    shifted_data1 = shifted_data_kx.data

    kx_params = params(1.0,2,128,0.3,4,np.sinc)
    ky_params = params(1.0,2,128,0,0,np.sinc)

    shifted_data_kx = kspace_data(kx_params,ky_params)
    shifted_data2 = shifted_data_kx.data

    fft_shifted_data = tr.inverse_2D(shifted_data2)

    #save_data(shifted_data)

    return shifted_data1, shifted_data2