# %%
import numpy as np
import matplotlib.pyplot as plt

nx, ny = 256, 128

data = np.fromfile('output/t_00400000.dat', dtype=np.float64)  # or float64
print("Data size:", data.size)
data = data.reshape((ny, nx))  # rows = y, columns = x

plt.figure(figsize=(14,6))
plt.imshow(data, cmap='jet', origin='lower', aspect='auto')
plt.colorbar(label='Temperature')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('scaled')
plt.show()
#1D plot
#line_data = data[:, nx // 2]  # middle column
#plt.subplot(1, 2, 2)
#plt.plot(line_data, np.arange(ny), color='black')
#plt.xlabel('Variable')
#plt.ylabel('y')
#plt.title('1D Profile along y (x = nx/2)')
#plt.grid(True)

#plt.tight_layout()
#plt.show()

# %%
