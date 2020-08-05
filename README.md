PyNMC
=====

A Comprehensive Magnitudes Converter for JWST/NIRCam 
=====================================================

*Authors:* Arsh Nadkarni (UArizona)

*Contributors:* Jiten Sidhpura (SPIT, India)

**!!Under Development!!**

PyNMC is a comprehensive magnitudes converter for JWST/NIRCam, which can be used to plan observations or 
input source magnitudes into JWST simulators such as MIRAGE (https://mirage-data-simulator.readthedocs.io/en/latest/).

Currently, PyNMC can be used for the following conversions:

- Optical to NIRCam Magnitude Conversion
- NIRCam to NIRCam Magnitude Conversion

This package makes use of supporting packages such as pyNRC (https://pynrc.readthedocs.io/en/latest/) and PySynphot (https://pysynphot.readthedocs.io/en/latest/index.html) to convert source magnitudes realistically from any observation to a NIRCam observation.

**Note:** PyNMC takes in a host of input data files from pyNRC and PySynphot in
order to convert magnitudes. Owing to the large size of these reference files, they are not included
with this source distribution. Check out the documentation to download these files. 
and see how to use them.
