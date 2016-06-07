import subprocess
import glob

files = glob.glob('*.tif')
inp = ''

for f in files:
    inp = inp + str(f) + " "

out = files[0].split('.')[0]
out = out[:-6] + "merged.tif"

cmd = "gdal_merge.py -separate -o " + out + " -of GTiff " + inp
subprocess.call(cmd, shell = True)
