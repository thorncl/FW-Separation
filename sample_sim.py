import numpy as np
import reconstruct as re
from kspace import *

def main():

    delays = np.random.uniform(-0.8,0.8,(256,1))

    kspace = kspace_data(params(1.0,2.0,128.0,delays,2.0,np.sinc,256,False))

    recon = re.reconstruct(kspace)

    plot_data(kspace.img)
    plt.title('Corrupted Image')

    plot_data(recon.corrected_img)
    plt.title('Corrected Image')

if __name__ == '__main__':

    main()