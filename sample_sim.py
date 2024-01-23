import numpy as np
import reconstruct as re
from kspace import *

def main():

    # induce a random, uniformly distributed delay
    delays = 0.05*np.random.uniform(-0.8, 0.8, (256,1))

    # apply the delay to each row of kspace
    kspace = kspace_data(params(1, 2, 128, delays, 2, True))

    # perform the reconstruction
    recon = re.reconstruct(kspace)

    plot_data((kspace.img))
    plt.title('Corrupted Image')

    plot_data((recon.corrected_img))
    plt.title('Corrected Image')

if __name__ == '__main__':

    main()
