import subprocess
import glob

files = glob.glob('*.tif')

for f in files:
    x = f.split('.')
    cmd = "gdal_translate -of HDF4Image "+f+" "+x[0]+".hdf4"
    subprocess.call(cmd, shell = True)
    cmd = "h4toh5 "+x[0]+".hdf4 "+x[0]+".hdf5"
	subprocess.call(cmd, shell = True)
	cmd = "rm "+x[0]+".hdf4"
	subprocess.call(cmd, shell = True)
