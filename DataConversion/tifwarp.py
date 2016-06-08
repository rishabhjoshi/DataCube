import subprocess
import glob

files = glob.glob('*.tif')
inp = ''

for f in files:
    inp = inp + str(f) + " "

out = files[0].split('.')[0]
out = out[:-6] + "_warped.tif"

cmd = "gdalwarp -of GTiff " + inp + " " + out
# use "gdalwarp -of GTiff --config GDAL_CACHEMAX 3000 -wm 3000 in out
# This sets the cache of for gdalwarp. Dont define cache more than RAM
# 3000 signifies 3Gigs of RAM
subprocess.call(cmd, shell = True)
