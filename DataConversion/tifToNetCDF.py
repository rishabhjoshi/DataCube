import subprocess
import glob

files = glob.glob('*.tif')

for f in files:
    x = f.split('.')
    cmd = "gdal_translate -of netCDF "+f+" "+x[0]+"temp.nc"
    subprocess.call(cmd, shell = True)
    cmd = "ncdump -k "+x[0]+"temp.nc"
    out = subprocess.check_output(cmd, shell = True)
    out = out.splitlines()[0]
#the file is in netCDF3. nccopy command converts it to v4. **Time consuming step is file is large**
    if out == "classic" or out == "64-bit offset":
        cmd = "nccopy -k 4 "+x[0]+"temp.nc "+x[0]+".nc"
        subprocess.call(cmd, shell = True)
        cmd = "rm "+x[0]+"temp.nc"
        subporcess.call(cmd, shell = True)
    else:
        cmd = "mv "+x[0]+"temp.nc "+x[0]+".nc" 
        subprocess.call(cmd, shell = True)
