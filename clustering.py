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

K = 3
cluster = km.labels_
color=['blue','green','cyan']
for k in range(K):
    data = image_2D[cluster == k]
    plt.scatter(data[:, 0],data[:, 1], c=color[k], alpha=0.8, label='cluster %d' % k)
    # plt.scatter(centers[k, 0],centers[k, 1], c='red', marker="x")
plt.legend(fontsize=12, loc='upper right') # legend position
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.show()

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