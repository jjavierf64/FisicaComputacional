import numpy as np 
import matplotlib.pyplot as plt 
import scipy 
from scipy import integrate 
# Define la señal periódica 
T = 2 * np.pi  # Periodo 
omega = 2 * np.pi / T  # Frecuencia angular 
t = np.linspace(0, T, 1000)  # Vector de tiempo 
x = np.cos(2 * omega * t) + 0.5 * np.sin(4 * omega * t)  # Señal periódica 
 
# Calcula los coeficientes de Fourier 
N = 10  # Numero de coeficientes a calcular 
a0 = (2/T) * scipy.integrate.simpson(x, t) 
 
an = np.zeros(N) 
bn = np.zeros(N) 
 
for n in range(1, N+1): 
    an[n-1] = (2/T) * scipy.integrate.simpson(x * np.cos(n * omega * t), t) 
    bn[n-1] = (2/T) * scipy.integrate.simpson(x * np.sin(n * omega * t), t) 
 
# Reconstruye la señal a partir de los coeficientes de Fourier 
x_reconstruido = a0/2 
for n in range(1, N+1): 
    x_reconstruido += an[n-1] * np.cos(n * omega * t) + bn[n-1] * np.sin(n * omega * t) 
 
# Grafica la señal original y la reconstruida 
plt.plot(t, x, label='Señal original') 
plt.plot(t, x_reconstruido, label='Señal reconstruida') 
plt.legend() 
plt.show()