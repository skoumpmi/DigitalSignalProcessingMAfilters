import numpy
import scipy
import matplotlib
from matplotlib import pyplot as pyplot
from scipy.io import wavfile as wav


#rate,data=wav.read("President Obama tears up during gun control speech - BBC News.wav")
data=wav.read("President Obama tears up during gun control speech - BBC News.wav")
datafft=numpy.fft.rfft(data)
#datafft=abs(datafft)
#datafft=10*(numpy.log10(datafft))
resample=numpy.fft.irfft(datafft)
pyplot.plot(resample)
pyplot.show()
resample=numpy.asarray(datafft,numpy.int16)
pyplot.plot(resample)
pyplot.show()
resample=wav.write('resampling.wav',44100,resample)
pyplot.plot(data)
pyplot.show()
pyplot.plot(datafft)

pyplot.show()