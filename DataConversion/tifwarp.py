import subprocess
import glob

files = glob.glob('*.tif')
inp = ''

for f in files:
    inp = inp + str(f) + " "

out = files[0].split('.')[0]
out = out[:-6] + "_warped.tif"

cmd = "gdalwarp -of GTiff " + inp + " " + out
subprocess.call(cmd, shell = True)
