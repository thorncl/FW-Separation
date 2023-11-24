from dataclasses import dataclass
import os
import numpy as np
import matplotlib.pyplot as plt
import transforms as tr

@dataclass(kw_only = False)
class params():
   
    scaling_factor: float
    voxel_width_factor: float
    pixel_offset: float
    delay: float | np.ndarray
    modulo: float
    func: callable
    image_size: int = 256

    def __post_init__(self):

        ky, kx = self.__build_mesh()
        self.kxy = [ky, kx]

    def __build_mesh(self) -> np.ndarray:

        return np.meshgrid(np.arange(self.image_size), np.arange(self.image_size))
    
@dataclass(kw_only = False)
class kspace_data():

    param: params
    
    def __post_init__(self):
        
        self.data = self.get_kspace(False, True)
        self.calib = self.get_kspace(False, False)
        self.img = tr.inverse_2d(self.data)

    def constant_delay(self) -> np.ndarray:

        return np.where(self.param.kxy[1] % self.param.modulo == 0, 
                        self.param.delay, -self.param.delay)
    
    def random_delay(self) -> np.ndarray:

        return self.param.delay
    
    def get_delay(self) -> np.ndarray:

        return self.constant_delay() if type(self.param.delay) is float else self.random_delay()

    def compute(self, ax : int, delay : bool = True, no_calib : bool = True) -> np.ndarray:

        return self.param.func((no_calib*self.param.scaling_factor*(self.param.kxy[ax] - 
                                                                    self.param.pixel_offset + delay*self.get_delay()) / self.param.voxel_width_factor))
        
    def get_kspace(self, delay : bool = True, no_calib : bool = True) -> np.ndarray:

        return self.compute(0)*self.compute(1, delay, no_calib)

    
def save_data(data : np.ndarray, file_name : str = "ClareArray") -> None:

    np.save(os.getcwd() + '\\' + file_name, data)

def load_data(file_name : str) -> None:

    np.load(file_name)

def plot_data(data : np.ndarray) -> None:
    
    plt.figure()
    plt.imshow(np.concatenate((np.real(data),np.imag(data)), axis = 1), cmap = 'gray')
    plt.colorbar()
