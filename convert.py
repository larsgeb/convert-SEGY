import segyio
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sys import getsizeof


vp = np.empty((13601,2801))
density = np.empty((13601,2801))
vs = np.empty((13601,2801))

with segyio.open('density_marmousi-ii.segy') as f:
    it = 0
    for trace in f.trace:
        density[it,] = trace
        it = it + 1
f.close()
del f
density = density[7250:7750,250:500] * 1000

plt.imshow(np.transpose(density))
plt.colorbar()
plt.savefig("dens.png")
plt.close()

with segyio.open('vs_marmousi-ii.segy') as f:
    it = 0
    for trace in f.trace:
        vs[it,] = trace
        it = it + 1
f.close()
del f
vs = vs[7250:7750,250:500] * 1000

plt.imshow(np.transpose(vs))
plt.colorbar()
plt.savefig("vs.png")
plt.close()

with segyio.open('vp_marmousi-ii.segy') as f:
    it = 0
    for trace in f.trace:
        vp[it,] = trace
        it = it + 1
f.close()
del f
vp = vp[7250:7750,250:500] * 1000


plt.imshow(np.transpose(vp))
plt.colorbar()
plt.savefig("vp.png")
plt.close()


mu = np.multiply(np.square(vs), density)
lm = np.multiply(np.square(vp), density) 
la = lm - 2*mu

plt.imshow(np.transpose(mu))
plt.colorbar()
plt.savefig("mu.png")
plt.close()

plt.imshow(np.transpose(la))
plt.colorbar()
plt.savefig("lambda.png")
plt.close()

plt.imshow(np.transpose(lm))
plt.colorbar()
plt.savefig("la2mu.png")

np.savetxt("lm.txt",lm)
np.savetxt("la.txt",la)
np.savetxt("mu.txt",mu)
np.savetxt("de.txt",density)
