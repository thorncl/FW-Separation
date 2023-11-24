import numpy as np
import reconstruct as re
from kspace import *

def main():

    rand_delays = np.random.randint(-10,10,(256,1))

    kspace_params = params(1.0,2.0,128.0,rand_delays,2.0,np.sinc)

    kspace = kspace_data(kspace_params)

    recon = re.reconstruct(kspace)

    plot_data(kspace.img)
    plt.title('Corrupted Image')

    plot_data(recon.corrected_img)
    plt.title('Corrected Image')

    return recon

if __name__ == '__main__':
    recon = main()