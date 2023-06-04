import numpy as np
import matplotlib.pyplot as plt

from data_load import image_2D
from data_load import image_numpy
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# pca = PCA(n_components=500)
# pca.fit(image)

# print(pca.components_.shape)

km = KMeans(n_clusters=4, random_state=42, n_init=10)
km.fit(image_2D)

print(km.labels_)
print(np.unique(km.labels_, return_counts=True))

inertia = []
for k in range(2, 10):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(image_2D)
    inertia.append(km.inertia_)

plt.plot(range(2, 10), inertia)
plt.xlabel('k')
plt.ylabel('inertia')
plt.show()

# data_0 = np.array()
# data_1 = np.array()
# data_2 = np.array()
# data_3 = np.array()

# def draw_clusters(arr, ratio=1):
#     n = len(arr)
#     rows = int(np.ceil(n / 10))
#     cols = n if rows < 2 else 10
#     fig, axs = plt.subplots(rows, cols, figsize=(cols * ratio, rows * ratio), squeeze=False)
    
#     for i in range(rows):
#         for j in range(cols):
#             if i * 10 + j < n:
#                 axs[i, j].imshow(arr[i * 10 + j])
#             axs[i, j].axis('off')
#     plt.show()

# draw_clusters(image_numpy[km.labels_==0])
# draw_clusters(image_numpy[km.labels_==1])
# draw_clusters(image_numpy[km.labels_==2])
# draw_clusters(image_numpy[km.labels_==3])