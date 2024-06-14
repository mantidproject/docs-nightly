''' ----------- Wireframe plot ----------- '''

from mantid.simpleapi import *
import matplotlib.pyplot as plt

# This file can be found in the Usage Examples folder, available
# here https://www.mantidproject.org/installation/index#sample-data
data = Load('PG3_733.nxs')

fig, ax = plt.subplots(subplot_kw={'projection':'mantid3d'})
ax.plot_wireframe(data, color='green')
#fig.show()