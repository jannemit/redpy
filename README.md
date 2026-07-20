# redpy 

redpy is a tool for the Cosmic Evolution Early Release Science (CEERS) survey using the James Webb Space Telescope (JWST) NIRCam photometric filters. redpy takes an input redshift, z, and outputs a list of photometric filters and the emission lines that fall in each. An example of this  emission line output with z=6.5887 is shown below.

-----------------------------------------------

Major Lines:<br/>
In F356W: [OIII]1, [OIII]2<br/>
In 360M: [OIII]1, [OIII]2<br/>
In F444W: Hα<br/>


Breaks:<br/>
In F070W: Lyman Break<br/>
In F277W: Balmer Break<br/>


Minor Lines:<br/>
In F090W: Lα<br/>
In F115W: NIV], CIV, HeII<br/>
In F140M: CIII]<br/>
In F150W: CIII]<br/>
In F182M: [NeIV]
In F200W: [NeIV], MgII<br/>
In F210M: MgII<br/>
In F250M: [NeV]1<br/>
In F277W: [NeV]1, [NeV]2, [OII]1, [OII]2, [NeIII]1, [NeIII]2, [NeIII]3, Hδ<br/>
In F300M: [NeIII]1, [NeIII]2, [NeIII]3, Hδ<br/> 
In F335M: Hγ<br/>
In F356W: Hγ, Hβ<br/>
In F360M: Hβ<br/>
In F444W: HeI, [OI], [NII]1<br/>
In F480M: [OI], [NII]1<br/>
In F560W: [SII]1, [SII]2, [ArIII]<br/>

-----------------------------------------------


The filters used are F070W, F090W, F115W, F140M, F150W, F162M, F182M, F200W, F210M, F250M, F277W, F300M, F335M, F356W, F360M, F410M, F430M, F444W, F460M, F480M and F560W.

The emission lines used are [ArIII]=7753, Balmer Break=3645, CIII]=1909, CIV=1550, Ha=6565, Hb=4863, Hd=4102, HeI=5876, HeII=1640, Hg=4342, Lyman Break=912, Lya=1215, MgII=2799, NIV]=1487, [NeIII]1=3869, [NeIII]2=3890, [NeIII]3=3867, [NeIV]=2439, [NeV]1=3347, [NeV]2=3427, [NII]1=6550, [NII]2=6585, [OI]=6302, [OII]1=3726, [OII]2=3729, [OIII]1=4960, [OIII]2=5008, Paa=18750, Pab=12820, Pad=10052.6, Pag=12821, [SII]1=6718, [SII]2=6732, [SIII]1=9069, and [SIII]2=9531 in units of Angstroms. 



For a Linux OS or MacOS:

0. If you're familiar with running .py files, run redshift_finder.py in your command line, and it will prompt you. If you are not familiar, follow this step by step guide

1. Download redshift_finder.py, in terminal type

<code> git clone https://github.com/jannemit/redpy.git </code> 

2. In terminal navigate to file location (redshift_finder.py)

<code> cd /path/to/redpy </code>

3. input at the command line

<code> ipython </code>

4. input at the command line

<code> run redshift_finder.py </code>

5. You will be prompted with "Enter redshift:", input a positive number with or without a decimal
    
6. The output will be a list of emission line filter locations
<br/>


ALTERNATIVE for Lixus OS or Mac OS (follow from above until step 3):

3. input at the command line

<code> python redshift_finder.py </code>

or

<code> python3 redshift_finder.py </code>

depending on the version of python used

4. You will be prompted with "Enter redshift:", input a positive number with or without a decimal
    
5. The output will be a list of emission line filter locations 
