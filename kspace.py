from dataclasses import dataclass
import numpy as np

@dataclass(kw_only = False)
class params():

    scale: float 
    width: int
    offset: int
    shift: float
    row: int
    func: callable 

class kspace_data():

    kx_params: params
    ky_params: params
    size: int = 256
    kx, ky = np.meshgrid(np.arange(size),np.arange(size))
    data = np.zeros((size,size))

    def __init__(self, kx_params, ky_params):
        self.kx_params = kx_params
        self.ky_params = ky_params
        self.params = {"k_xy_params": [self.kx_params, self.ky_params], "k_xy": [self.kx, self.ky]}
        self.data = self.get_kspace()
 
    def shift_term(self, data: np.ndarray, ax: int) -> np.ndarray:
        param = self.params[list(self.params.keys())[0]][ax]
        return np.where(data % param.row == 0, param.shift, -param.shift) if (param.shift and param.row) != 0 else 0

    def get_data(self, ax: int) -> np.ndarray:
        k_xy = self.params[list(self.params.keys())[1]]
        param = self.params[list(self.params.keys())[0]]
        return param[ax].func(param[ax].scale*(k_xy[ax] - param[ax].offset + self.shift_term(k_xy[ax], ax))/param[ax].width)

    def get_kspace(self) -> np.ndarray:
        return np.transpose(self.get_data(0)*self.get_data(1))
