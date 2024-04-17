import numpy as np
import matplotlib.pyplot as plt

a = 110
tid = 3
lengde = 50
noder = 30

#initialisering
dx = lengde / noder
dy = lengde / noder
# dt = min(dx**2 / (4 * a), dy**2 / (4 * a))
dt=0.25*dx*dy/a
t_noder = int(tid / dt)

u = np.zeros((noder, noder)) + 20  # startverdi
u[0, :] = -100  # innerste node x retning
u[-1, :] = 100  # ytterste node x retning
u[:,0]=100 #innerste node y retning
u[:,-1]=100 #ytterste node y retning

#vi ønsker en simulasjon gjennom tiden 
fig, axis = plt.subplots()
pcm = axis.pcolormesh(u, cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm, ax=axis)
# axis.set_ylim([-2, 3])

counter = 0

while counter < tid:
    w = u.copy()

    for i in range(1, noder - 1):
        for j in range(1, noder - 1):
            dd_ux = (w[i - 1, j] - 2 * w[i, j] + w[i + 1, j]) / dx**2
            dd_uy = (w[i, j - 1] - 2 * w[i, j] + w[i, j + 1]) / dy**2
            u[i, j] = dt * a * (dd_ux + dd_uy) + w[i, j]

    counter += dt
    print("t: {:.3f} [s], Gjennomsnittlig temperatur: {:.2f} Grader [Celcius]".format(counter, np.average(u)))

    pcm.set_array(u.ravel())
    axis.set_title("Varmefordeling ved t:{:.3f} [s]".format(counter))
    plt.pause(0.01)

plt.show()