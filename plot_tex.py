def main():
    from physics import cube_Tex
    from spectral_cube import SpectralCube
    import numpy as np
    from astropy.io import fits
    import matplotlib.pyplot as plt
    from astropy.wcs import WCS
    
    cube = SpectralCube.read("../carma_orion/mask_imfit_12co_pix_2_Tmb.fits")
    wcs = WCS(cube.header)
    Tex = cube_Tex(cube, thick=True, snr_cutoff=False, average=False, plot=False)
    
    fig = plt.figure()
    ax = fig.add_subplot(121, projection=wcs.celestial, slices=('x','y'))
    ax.imshow(Tex.data, cmap='inferno', interpolation='none', origin='lower')


    hdu = fits.open("../shells/catalogs/planck_herschel_dustT.fits")[0] 
    wcs = WCS(hdu.header)
    ax = fig.add_subplot(122, projection=wcs)
    ax.imshow(hdu.data, cmap='inferno', interpolation='none', origin='lower',
            vmin=20, vmax=50)
    
    plt.savefig("Tex_dustT.pdf", dpi=350)
    
    

    print("Mean Tex is {}. Median Tex is {}.".format(np.nanmean(Tex.value), np.nanmedian(Tex.value)))
if __name__ == '__main__':
    main()