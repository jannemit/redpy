import astropy.units as u
import astropy.constants as c
from astropy.coordinates import SkyCoord, search_around_sky
from astropy.time import Time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import glob
from astropy.io import fits
import pickle
from astropy.cosmology import WMAP9 as cosmo
import seaborn as sns
from astropy.table import Table


#plt.rcParams['figure.figsize'] = (10, 10)
#plt.rc('axes', labelsize=27)
##plt.rc('axes', labelweight='bold')
#plt.rc('axes', titlesize=27)
#plt.rc('axes', titleweight='bold')
#plt.rc('font', family='sans-serif')
#plt.rcParams.update({'font.size': 20})


z = input('Enter redshift:')
z = float(z)

def get_lines(z):
    """
    
    params
    ---
    z: redshift, float

    returns
    ---
    #what comes out when its run
    """

    ##Setting the figure size
    #plt.rcParams['figure.figsize'] = (35, 15)


    ##plotting the James Webb Space Telescope filters
    #plt.axvspan(5.054, 6.171, label = 'F560W', color = '#FF7950', alpha = .5)

    #plt.axvspan(3.881, 4.982, label = 'F444W', color = '#FF9400', alpha = .5)
    #plt.axvspan(3.866, 4.302, label = 'F410M', color = '#FFD107', alpha = .5)
    #plt.axvspan(3.135, 3.981, label = 'F356W', color = '#E6FF2C', alpha = .5)
    #plt.axvspan(2.423, 3.132, label = 'F277W', color = '#589C00', alpha = .5)
    #plt.axvspan(1.755, 2.227, label = 'F200W', color = '#147A21', alpha = .5)

    #plt.axvspan(1.331, 1.668, label = 'F150W', color = '#43ACB3', alpha = .5)
    #plt.axvspan(1.013, 1.282, label = 'F115W', color = '#3486CC', alpha = .5)


    #Assigning the restframe wavelenghs to variables
    lya = 1215
    lb = 912
    n4 = 1487
    c4 = 1550
    heii = 1640
    c3 = 1909
    ne4 = 2439
    mgii = 2799
    ne5 = 3347
    ne5_2 = 3427
    bb = 3645
    o2 = 3726
    o2_2 = 3729
    ne3 = 3869
    ne3_2 = 3890
    ne3_3 = 3867
    hd = 4102
    hg = 4342
    hb = 4863
    o3 = 4960
    o3_2 = 5008
    hei = 5876
    oi = 6302
    nii = 6550
    nii_2 = 6585
    ha = 6565
    sii = 6718
    sii_2 = 6732
    ar3 = 7753
    s3 = 9069
    s3_2 = 9531
    pad = 10052.6
    pab = 12820
    pag = 12821
    paa = 18750
    
    ##font size for the wavelength labels on the plot
    #font = 18

    ##range of values for redshift from 0 to 100
    #zarr = np.arange(0,100)

    ##plotting lines for wavelengths over the range of redshift values and plotting labels for the lines
    #plt.plot(1e-4*lya*(1+zarr),zarr, color='crimson')
    #plt.plot(1e-4*lb*(1+zarr),zarr, color='crimson')
    #plt.text(1.04, 8, r'Lyman break + Ly$\alpha$', rotation = 64, c = 'crimson', zorder = 1, fontsize = font)

    #plt.plot(1e-4*n4*(1+zarr),zarr, color='mediumorchid')
    #plt.text(1.45, 9.18, 'NIV]', rotation = 59, c = 'mediumorchid', zorder = 1, fontsize = font)

    #plt.plot(1e-4*c4*(1+zarr),zarr, color='darkviolet')
    #plt.text(1.45, 8.65, 'CIV', rotation = 58, c = 'darkviolet', zorder = 1, fontsize = font)

    #plt.plot(1e-4*heii*(1+zarr),zarr, color='purple')
    #plt.text(1.45, 8.17, 'HeII', rotation = 57, c = 'purple', zorder = 1, fontsize = font)

    #plt.plot(1e-4*c3*(1+zarr),zarr, color='indigo')
    #plt.text(1.45, 6.91, 'CIII]', rotation = 53, c = 'indigo', zorder = 1, fontsize = font)

    #plt.plot(1e-4*ne4*(1+zarr),zarr, color='darkslateblue')
    #plt.text(1.9, 7.05, '[NeIV]', rotation = 45, c = 'darkslateblue', zorder = 1, fontsize = font)

    #plt.plot(1e-4*mgii*(1+zarr),zarr, color='slateblue')
    #plt.text(2.6, 8.46, 'MgII', rotation = 41, c = 'slateblue', zorder = 1, fontsize = font)

    #plt.plot(1e-4*ne5_2*(1+zarr),zarr, color='steelblue')
    #plt.plot(1e-4*ne5*(1+zarr),zarr, color='steelblue')
    #plt.text(2.6, 6.95, '[NeV]', rotation = 36, c = 'steelblue', zorder = 1, fontsize = font)

    #plt.plot(1e-4*bb*(1+zarr),zarr, color='lightseagreen')
    #plt.text(2.5, 6, 'Balmer break', rotation = 33, c = 'lightseagreen', zorder = 1, fontsize = font)
    
    #plt.plot(1e-4*o2*(1+zarr),zarr, color='blue')
    #plt.plot(1e-4*o2_2*(1+zarr),zarr, color='blue')
    #plt.plot(1e-4*ne3*(1+zarr),zarr, color='blue')
    #plt.plot(1e-4*ne3_2*(1+zarr),zarr, color='blue')
    #plt.plot(1e-4*ne3_3*(1+zarr),zarr, color='blue')
    #plt.text(3.3, 7.7, '[OII]+[NeIII]', rotation = 32, c = 'blue', zorder = 1, fontsize = font)

    #plt.plot(1e-4*hd*(1+zarr),zarr, color='royalblue')
    #plt.text(4.1, 9.12, r'H$\delta$', rotation = 32, c = 'royalblue', zorder = 1, fontsize = font)

    #plt.plot(1e-4*hg*(1+zarr),zarr, color='teal')
    #plt.text(4.1, 8.58, r'H$\gamma$', rotation = 30, c = 'teal', zorder = 1, fontsize = font)

    #plt.plot(1e-4*o3*(1+zarr),zarr, color='darkgreen')
    #plt.plot(1e-4*o3_2*(1+zarr),zarr, color='darkgreen')
    #plt.plot(1e-4*hb*(1+zarr),zarr, color='darkgreen')
    #plt.text(4.50, 8.37, r'H$\beta$+[OIII]', rotation = 28, c = 'darkgreen',zorder = 1, fontsize = font)

    #plt.plot(1e-4*hei*(1+zarr),zarr, color='darkgreen')
    #plt.text(4.50, 6.75, 'HeI', rotation = 25, c = 'darkgreen',zorder = 1, fontsize = font)

    #plt.plot(1e-4*oi*(1+zarr),zarr, color='olivedrab')
    #plt.text(4.50, 6.25, '[OI]', rotation = 22, c = 'olivedrab',zorder = 1, fontsize = font)

    #plt.plot(1e-4*ha*(1+zarr),zarr, c= 'red')
    #plt.plot(1e-4*nii*(1+zarr),zarr, c= 'red')
    #plt.plot(1e-4*nii_2*(1+zarr),zarr, color='red')
    #plt.text(4.50, 5.95, r'H$\alpha$ + [NII]', rotation = 21, c = 'red', zorder = 1, fontsize = font)

    #plt.plot(1e-4*sii*(1+zarr),zarr, color='darkred')
    #plt.plot(1e-4*sii_2*(1+zarr),zarr, color='darkred')
    #plt.text(4.50, 5.5, '[SII]', rotation = 19, c = 'darkred',zorder = 1, fontsize = font)

    #plt.plot(1e-4*ar3*(1+zarr),zarr, color = 'rebeccapurple')
    #plt.text(4.50, 4.9, '[ArIII]', rotation = 18, c = 'rebeccapurple',zorder = 1, fontsize = font)

    #plt.plot(1e-4*s3*(1+zarr),zarr, color='indigo')
    #plt.plot(1e-4*s3_2*(1+zarr),zarr, color='indigo')
    #plt.text(4.50, 4.08, '[SIII]', rotation = 16, c = 'indigo',zorder = 1, fontsize = font)

    #plt.plot(1e-4*pad*(1+zarr),zarr, color='brown')
    #plt.text(4.50, 3.54, r'Pa$\delta$', rotation = 14, c = 'brown', zorder = 1, fontsize = font)

    #plt.plot(1e-4*pab*(1+zarr),zarr, color='brown')
    #plt.plot(1e-4*pag*(1+zarr),zarr, color='brown')
    #plt.text(4.50, 2.6, r'Pa$\beta$ + Pa$\gamma$', rotation = 11, c = 'brown',zorder = 1, fontsize = font)

    #plt.plot(1e-4*paa*(1+zarr),zarr, color='brown')
    #plt.text(4.50, 1.46, r'Pa$\alpha$', rotation = 8, c = 'brown', zorder = 1, fontsize = font)

    ##x-axis labels for the pivot wavelength of each filter
    #ticks = [1.154, 1.501, 1.990, 2.786, 3.563, 4.092, 4.421, 5.635]
    #labels = ticks

    ##x and y axes limits 
    #plt.ylim(1,10)
    #plt.xlim(1, 6.175)

    ##x and y axes labels
    #plt.ylabel('Redshift')
    #plt.xlabel('Wavelength [$\mu$m]')
    ##x and y axes ticks labels
    #plt.xticks(ticks, labels, rotation = 70)
    #plt.tick_params('y', length=10, width=1, which='minor')
    ##legend of filters
    #plt.legend(loc = 'lower right', ncols = 2, fancybox = False, framealpha = .75, facecolor = 'w');

    #generating the output for which wavelengths fall in which filters at a given redshift 
    #the major lines
    #making a list for wavelenghs and names
    m = [4960, 5008, 6565]
    mname = ['[OIII]1', '[OIII]2', 'H\u03B1']

    #making empty lists for each filter
    mF115W = []
    mF150W = []
    mF200W = []
    mF277W = []
    mF356W = []
    mF410M = []
    mF444W = []
    mF560W = []

    #equation for wavelength at a given redshift 
    ml = [1e-4*x*(1+z) for x in m]

    #checking to see if the equation falls in each filter for the given redshift
    #if it is, then it adds the name of the line to the empty filter list
    for i in range(len(ml)):
    
        x=ml[i]
        mnam=mname[i]
        
        if x>1.013 and x<1.282:
            mF115W.append(mnam)
        if x>1.331 and x<1.668:
            mF150W.append(mnam)
        if x>1.755 and x<2.227:
            mF200W.append(mnam)
        if x>2.423 and x<3.132:
            mF277W.append(mnam)
        if x>3.135 and x<3.981:
            mF356W.append(mnam)
        if x>3.866 and x<4.302:
            mF410M.append(mnam)
        if x>3.881 and x<4.982:
            mF444W.append(mnam)
        if x>5.054 and x<6.171:
            mF560W.append(mnam)

    #printing out the list of wavelengths for each filter, if there are none then nothing is output
    print('Major Lines:')
    if not mF115W:
        print(end = '')
    else:
        print('In F115W', end = ': ')
        print(*mF115W, sep = ', ')
    if not mF150W:
        print(end = '')
    else:
        print('In F150W', end = ': ')
        print(*mF150W, sep = ', ')
    if not mF200W:
        print(end = '')
    else:
        print('In F200W', end = ': ')
        print(*mF200W, sep = ', ')
    if not mF277W:
        print(end = '')
    else:
        print('In F277W', end = ': ')
        print(*mF277W, sep = ', ')
    if not mF356W:
        print(end = '')
    else:
        print('In F356W', end = ': ')
        print(*mF356W, sep = ', ')
    if not mF410M:
        print(end = '')
    else:
        print('In F410M', end = ': ')
        print(*mF410M, sep = ', ')
    if not mF444W:
        print(end = '')
    else:
        print('In F444W', end = ': ')
        print(*mF444W, sep = ', ')
    if not mF560W:
        print(end = '')
    else:
        print('In F560W', end = ': ')
        print(*mF560W, sep = ', ')
    print('\n')

    #the breaks 
    #making a list for wavelenghs and names
    b = [912, 3645]
    bname = ['Lyman Break', 'Balmer Break']

    #making empty lists for each filter
    bF115W = []
    bF150W = []
    bF200W = []
    bF277W = []
    bF356W = []
    bF410M = []
    bF444W = []
    bF560W = []

    #equation for wavelength at a given redshift 
    bl = [1e-4*x*(1+z) for x in b]

    #checking to see if the equation falls in each filter for the given redshift
    #if it is, then it adds the name of the line to the empty filter list
    for i in range(len(bl)):
    
        x=bl[i]
        bnam=bname[i]
        
        if x>1.013 and x<1.282:
            bF115W.append(bnam)
        if x>1.331 and x<1.668:
            bF150W.append(bnam)
        if x>1.755 and x<2.227:
            bF200W.append(bnam)
        if x>2.423 and x<3.132:
            bF277W.append(bnam)
        if x>3.135 and x<3.981:
            bF356W.append(bnam)
        if x>3.866 and x<4.302:
            bF410M.append(bnam)
        if x>3.881 and x<4.982:
            bF444W.append(bnam)
        if x>5.054 and x<6.171:
            bF560W.append(bnam)

    #printing out the list of wavelengths for each filter, if there are none then nothing is output
    print('Breaks:')
    if not bF115W:
        print(end = '')
    else:
        print('In F115W', end = ': ')
        print(*bF115W, sep = ', ')
    if not bF150W:
        print(end = '')
    else:
        print('In F150W', end = ': ')
        print(*bF150W, sep = ', ')
    if not bF200W:
        print(end = '')
    else:
        print('In F200W', end = ': ')
        print(*bF200W, sep = ', ')
    if not bF277W:
        print(end = '')
    else:
        print('In F277W', end = ': ')
        print(*bF277W, sep = ', ')
    if not bF356W:
        print(end = '')
    else:
        print('In F356W', end = ': ')
        print(*bF356W, sep = ', ')
    if not bF410M:
        print(end = '')
    else:
        print('In F410M', end = ': ')
        print(*bF410M, sep = ', ')
    if not bF444W:
        print(end = '')
    else:
        print('In F444W', end = ': ')
        print(*bF444W, sep = ', ')
    if not bF560W:
        print(end = '')
    else:
        print('In F560W', end = ': ')
        print(*bF560W, sep = ', ')
    print('\n')

    #the minor lines 
    #making a list for wavelenghs and names
    e = [1215, 1487, 1550, 1640, 1909, 2439, 2799, 3347, 3427, 3726, 3729, 3869, 3890, 
         3867, 4102, 4342, 4863, 5876, 6302, 6550, 6585, 6718, 6732, 7753, 9069, 9531, 10052.6, 
         12820, 12821, 18750]
    name = ['Ly\u03B1', 'NIV]', 'CIV', 'HeII', 'CIII]', '[NeIV]', 'MgII', '[NeV]1', '[NeV]2', '[OII]1', '[OII]2', 
            '[NeIII]1', '[NeIII]2', '[NeIII]3', 'H\u03B4', 'H\u03B3', 'H\u03B2', 'HeI', '[OI]', '[NII]1', '[NII]2', 
            '[SII]1', '[SII]2', '[ArIII]', '[SIII]1', '[SIII]2', 'Pa\u03B4', 'Pa\u03B2', 'Pa\u03B3', 'Pa\u03B1']

    #making empty lists for each filter
    F115W = []
    F150W = []
    F200W = []
    F277W = []
    F356W = []
    F410M = []
    F444W = []
    F560W = []

    #equation for wavelength at a given redshift 
    el = [1e-4*x*(1+z) for x in e]

    #checking to see if the equation falls in each filter for the given redshift
    #if it is, then it adds the name of the line to the empty filter list
    for i in range(len(el)):
    
        x=el[i]
        nam=name[i]
        
        if x>1.013 and x<1.282:
            F115W.append(nam)
        if x>1.331 and x<1.668:
            F150W.append(nam)
        if x>1.755 and x<2.227:
            F200W.append(nam)
        if x>2.423 and x<3.132:
            F277W.append(nam)
        if x>3.135 and x<3.981:
            F356W.append(nam)
        if x>3.866 and x<4.302:
            F410M.append(nam)
        if x>3.881 and x<4.982:
            F444W.append(nam)
        if x>5.054 and x<6.171:
            F560W.append(nam)

    #printing out the list of wavelengths for each filter, if there are none then nothing is output
    print('Minor Lines:')
    if not F115W:
        print(end = '')
    else:
        print('In F115W', end = ': ')
        print(*F115W, sep = ', ')
    if not F150W:
        print(end = '')
    else:
        print('In F150W', end = ': ')
        print(*F150W, sep = ', ')
    if not F200W:
        print(end = '')
    else:
        print('In F200W', end = ': ')
        print(*F200W, sep = ', ')
    if not F277W:
        print(end = '')
    else:
        print('In F277W', end = ': ')
        print(*F277W, sep = ', ')
    if not F356W:
        print(end = '')
    else:
        print('In F356W', end = ': ')
        print(*F356W, sep = ', ')
    if not F410M:
        print(end = '')
    else:
        print('In F410M', end = ': ')
        print(*F410M, sep = ', ')
    if not F444W:
        print(end= '')
    else:
        print('In F444W', end = ': ')
        print(*F444W, sep = ', ')
    if not F560W:
        print(end = '')
    else:
        print('In F560W', end = ': ')
        print(*F560W, sep = ', ')

    ##plotting a horizontal line at the given redshift
    #plt.axhline(y = z, color = 'k', linestyle = '-', linewidth = 2.5)
    #plt.show()
    #plt.close()
    
    return z

get_lines(z)
