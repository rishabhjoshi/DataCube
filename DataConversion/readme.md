# Satellite Data Conversion

Objective :  To convert __GeoTIFF__ format images to 3 formats :

* HDF5
* NetCDF-4
* ECW

And to compare their performance for tera-byte sized data for read operations.

## Converting GeoTIFF to HDF5 and NetCDF4

### Prerequisites

GDAL by default doesn't add support for NetCDF and HDF5 conversion. So you have to install extra libraries. First install netCDF and HDF5. Then install libraries - _libnetcdf_ and _libhdf5_ (also _libdf_ to convert in HDF4 as GDAL cant convert to HDF5).

Steps : 

* Download GDAL - Geospatial Data Abstraction Library
* Install library - libnetcdf
* While configuring GDAL source, use :

```bash
	./configure --with-netcdf=/usr/local --with-hdf4=/usr/local --with-hdf5=/usr/local
```

* Make and install GDAL

> GDAL also supports ECW but ECW SDK 3.3 (current as of 6/6/16) uses JPEG2000 libraries which easily get overflowed so cant be used to convert to ECW. Since ECW is proprietary, the best way to use this format is through ERDAS Imagine.

* Installing HDF5. Follow [this](https://www.hdfgroup.org/ftp/HDF5/releases/hdf5-1.10/hdf5-1.10.0-patch1/src/unpacked/release_docs/INSTALL_parallel) link for parallel hdf5, [otherwise](https://www.hdfgroup.org/ftp/HDF5/releases/hdf5-1.10/hdf5-1.10.0-patch1/src/unpacked/release_docs/INSTALL).

* Install HDF4 and H4TOH5 conversion tools.

* Install NetCDF.

### To NetCDF4

Conversion to NetCDF4 is fairly straight forward.

* use the script TifToNetCDF

> It first uses _gdal translate_ to convert Tif to netCDF3 then converts netCDF3 to netCDF4.

### To HDF5

Direct conversion to HDF5 is not supported by GDAL.

You can use 2 methods to convert to HDF5

* Convert from NetCDF4 (Since NetCDF4 is built on HDF5 so a simple dump is sufficient)
* Use GDAL to convert Tif to HDF4 and then use HDF5 tools to convert to HDF5.

#### Using HDF4

Download the hdf4 to hdf5 conversion tools from [here](https://www.hdfgroup.org/h4toh5/libh4toh5.html).

Use the script tifToHDF5.py. The script converts the GeoTIFF files to HDF4 (which GDAL supports) and then uses the _h4toh5_ tool to convert HDF4 to HDF5. 

#### Using netCDF


### To ECW

GeoTIFF can be converted to ECW using ERDAS Imagine, which is a proprietary software. Although GDAL supports ECW too, but the SDK it uses cant be used to convert large files. (Gives Segmentation fault as it is unable to allocate enough memory).
This method is more involved. There are tools _ncdum_ and _ncgen_ in both HDFtools and NetCDF tools, so you'll have to rename one so that they dont clash. Another problem is that HDF uses netCDF 2.3.2 when building HDF versions of these tools, which is old, we have to therefore manually edit the intermediate CDL file because hdf-ncgen can't read everything that ncdump can write.
We therefore didn't use this method.

