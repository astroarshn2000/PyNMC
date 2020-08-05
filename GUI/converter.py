# Import Libraries
import os


# Converter Function
def converter(path1,path2,path3,input_filter,input_spectral,input_magnitude,input_photometric,output_filter,output_photometric):

    final_output = None
    
    os.environ["PYNRC_PATH"] =str(path1)
    os.environ["PYSYN_CDBS"] =str(path2)
    os.environ["WEBBPSF_PATH"] = str(path3)
    
    import pysynphot as S
    import pynrc
    
    bp_K = S.ObsBandpass(input_filter)
    bg = pynrc.nrc_utils.stellar_spectrum(input_spectral,input_magnitude,input_photometric,bp_K)
    bp_ncfilter = pynrc.nrc_utils.read_filter(output_filter)
    obs = S.Observation(bg,bp_ncfilter,binset=bg.wave)
    final_output = obs.effstim(output_photometric)


    


    return final_output