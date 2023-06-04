import os
import numpy as np
import matplotlib.pyplot as plt

from data_load import image_2D
from data_load import image_numpy
from data_load import dir_
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

image_ext_ = ".jpg"
output_dir_ = '../Final_Project_Data/After'

# pca = PCA(n_components=500)
# pca.fit(image)

# print(pca.components_.shape)

km = KMeans(n_clusters=4, random_state=42, n_init=10)
km.fit(image_2D)
cluster_labels = km.predict(image_2D)

print(km.labels_)
print(np.unique(km.labels_, return_counts=True))

os.makedirs(output_dir_, exist_ok=True)
for cluster_id in range(4):
    cluster_directory = os.path.join(output_dir_, f'cluster_{cluster_id}')
    os.makedirs(cluster_directory, exist_ok=True)

for idx, file in enumerate(3426):
    image_path = os.path.join(dir_, file)
    cluster_id = cluster_labels[idx]
    cluster_directory = os.path.join(output_dir_, f'cluster_{cluster_id}')
    output_path = os.path.join(cluster_directory, file)
    
    # 이미지 파일 복사
    os.copy(image_path, output_path)

# inertia = []
# for k in range(2, 10):
#     km = KMeans(n_clusters=k, random_state=42, n_init=10)
#     km.fit(image_2D)
#     inertia.append(km.inertia_)

# plt.plot(range(2, 10), inertia)
# plt.xlabel('k')
# plt.ylabel('inertia')
# plt.show()

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