from dataclasses import dataclass
import os
import numpy as np
import matplotlib.pyplot as plt

@dataclass(kw_only = False)
class params():

    scale: float
    width: float
    offset: float
    shift: float
    row: float
    func: callable

@dataclass(kw_only = False)
class kspace_data():

    kx_params: params
    ky_params: params
    size: int = 256

    def __post_init__(self):
        
        self.kx,self.ky = self.__build_mesh()
        self.params = self.__build_param_dict()
        self.data = self.get_kspace()

    def __build_mesh(self) -> np.ndarray:

        return np.meshgrid(np.arange(self.size),np.arange(self.size))

    def __build_param_dict(self) -> np.ndarray:

        return {"k_xy_params": [self.kx_params, self.ky_params], 
                "k_xy": [self.ky, self.kx]}
    
    def __get_param(self, ax: int) -> np.ndarray:

        return self.params[list(self.params.keys())[0]][ax]
 
    def shift_term(self, data: np.ndarray, ax: int) -> np.ndarray:

        param = self.__get_param(ax)
        return np.where(data % param.row == 0, 
                        param.shift, -param.shift) if param.shift != 0 else 0

    def get_data(self, ax: int) -> np.ndarray:

        param = self.__get_param(ax)
        return param.func((param.scale*(self.params['k_xy'][ax] - param.offset 
                                        + self.shift_term(self.params['k_xy'][~ax], ax))/param.width))

    def get_kspace(self) -> np.ndarray:

        return self.get_data(0)*self.get_data(1)
    
def save_data(data : np.ndarray, file_name : str = "ClareArray") -> None:

    np.save(os.getcwd() + '\\' + file_name, data)

def load_data(file_name : str) -> None:

    np.load(file_name)

def plot_data(data : np.ndarray) -> None:
    
    plt.figure()
    plt.imshow(np.concatenate((np.real(data),np.imag(data)),axis=1))
    plt.colorbar()
