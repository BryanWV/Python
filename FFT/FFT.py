import numpy as np, matplotlib.pyplot as plt, pandas as pd;
from scipy import fftpack
data = pd.read_excel("Excel.xlsx",sheet_name="Data",index_col=[0],header=None,decimal=",")
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


f=fftpack.fftfreq(n)*Fs
#Gráfica de frecuencia
Y = fftpack.fft(data)
fig,bx = plt.subplots()
plt.plot(f,np.abs(Y))
plt.show()
