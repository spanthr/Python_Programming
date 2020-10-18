# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 01:58:25 2020

@author: shaur
"""


from matplotlib import pyplot as plt
import numpy as np 
import scipy
from scipy import fftpack

#Frequency in terms of Hertz
fre  = 5 
#Sample rate
fre_samp = 50
t = np.linspace(0, 2, 2 * fre_samp, endpoint = False )
a = np.sin(fre  * 2 * np.pi * t)
figure, axis = plt.subplots()
axis.plot(t, a)
axis.set_xlabel ('Time (s)')
axis.set_ylabel ('Signal amplitude')
plt.title("Time Response")
plt.show()

#do DFT and visualize:

A=fftpack.fft(a)

frequency=fftpack.fftfreq(len(a)) * fre_samp
# frequency=scipy.freq(len(a)) * fre_samp

figure, axis = plt.subplots()
axis.plot(frequency, np.abs(A))
axis.set_xlabel ('Frequency in Hertz (Hz)')
axis.set_ylabel ('Frequency Domain Magnitude')
plt.title("Frequency Response")
plt.show()

