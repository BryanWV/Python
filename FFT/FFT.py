import numpy as np, matplotlib.pyplot as plt, pandas as pd;
from scipy import fftpack;
from scipy.fft import fftfreq;
from scipy.fft import fft;
data = pd.read_excel("Excel.xlsx",sheet_name="Data",index_col=[0],decimal=",")
data.info()
data.head(50)
data.describe()

ts = 0.2 # Tiempo de muestreo de la señal
Fs = 1 / ts # Frecuencia de muestreo

n = len(data)

#Gráfica de tiempo
t=np.linspace(0,(n-1)*ts,n)

fig,ax = plt.subplots()
plt.plot(t,data)
plt.xlabel("# of Samples")
plt.ylabel("Measured data")

'''
f=fftpack.fftfreq(n)*Fs
#Gráfica de frecuencia
Y = fftpack.fft(data)
fig,bx = plt.subplots()
plt.plot(f,np.abs(Y))
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
'''
dt= np.diff(t)[0]
print ('Value of dt is %s' % (dt))

f= fftfreq(len(t),np.diff(t)[0])
Y_FFT= fft(data)
#Solo se va a considerar la mitad del espectro de frecuencias
fig,ax = plt.subplots()
plt.plot(f[:n//2], np.abs(Y_FFT[:n//2]))
plt.axvline(1/(2*dt),ls="--", color='k') #Frecuencia de Nyquist
plt.xlabel('$f_n$ [$s^{-1}$]', fontsize =20)
plt.ylabel('|$\hat{x}_n$|', fontsize= 20)

plt.show()