# redpy 

redpy is a tool for the Cosmic Evolution Early Release Science (CEERS) survey using the James Webb Space Telescope (JWST) NIRCam photometric filters. redpy takes an input redshift, z, and outputs a list of photometric filters and the emission lines that fall in each. An example of this  emission line output with z=6.5887 is shown below.

![emissionlineoutput](https://github.com/user-attachments/assets/6bba328e-580a-4ff0-ae94-43b7fa847c2c)

The filters used are F115W, F150W, F200W, F277W, F356W, F410M, F444W, and F560W.

The emission lines used are [ArIII]=7753, Balmer break=3645, CIII]=1909, CIV=1550, Ha=6565, Hb=4863, Hd=4102, HeI=5876, HeII=1640, Hg=4342, Lyman break=1215, Lya=1215, MgII=2799, NIV]=1487, [NeIII]1=3869, [NeIII]2=3890, [NeIII]3=3867, [NeIV]=2439, [NeV]1=3347, [NeV]2=3427, [NII]1=6550, [NII]2=6585, [OI]=6302, [OII]1=3726, [OII]2=3729, [OIII]1=4960, [OIII]2=5008, Paa=18750, Pab=12820, Pad=10052.6, Pag=12821, [SII]1=6718, [SII]2=6718, [SIII]1=9069, [SIII]2=9531.



For a Linux OS or MacOS:

0. If you're familiar with running .py files, run redshift_finder.py in your command line, and it will prompt you. If you are not familiar, follow this step by step guide

1. Download redshift_finder.py, in terminal type

<code> git clone https://github.com/jannemit/redpy.git </code> 

2. In terminal navigate to file location (redshift_finder.py)

3. input at the command line

<code> ipython </code>

4. input at the command line

<code> run redshift_finder.py </code>

5. You will be prompted with "Enter redshift:", input a positive number with or without a decimal
    
6. The output will be a list of emission line filter locations 
