import numpy as np
from scipy import optimize
from dataclasses import dataclass
from kspace import *
import transforms as tr

@dataclass(kw_only = False)
class reconstruct():

    data: kspace_data

    def __post_init__(self):

        ifft_calib = tr.inverse_1d(self.data.calib, 1)
        ifft_calib_shftd = np.roll(ifft_calib, shift = 1, axis = 1)

        self.conj = self.complex_conj(ifft_calib_shftd)
        self.slope = self.complex_slope(ifft_calib, self.conj)
        self.corrected_img = self.reconstruct()

    def complex_conj(self, ifft_calib_shftd) -> np.ndarray:

        return np.conj(ifft_calib_shftd)
        
    def complex_slope(self, ifft : np.ndarray, conj : np.ndarray) -> np.ndarray:

        return ifft * conj
        
    def correction(self, complex_slope : np.ndarray) -> np.ndarray:

        row_sum = np.sum(complex_slope, 1)
        row_correction = np.arctan2(np.imag(row_sum),np.real(row_sum))

        return np.exp(-1j*(self.data.param.kxy[0]-128)*(np.transpose(row_correction*np.ones((256,256)))))

    def reconstruct(self) -> np.ndarray:

        ifft_img = tr.inverse_1d(self.data.data, 1)
        corrected_img = ifft_img * self.correction(self.slope)

        return tr.inverse_1d(corrected_img, 0)
