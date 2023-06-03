import numpy as np

from data_load import image_2D as image
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# pca = PCA(n_components=500)
# pca.fit(image)

# print(pca.components_.shape)

km = KMeans(n_clusters=4, random_state=42)
km.fit(image)

print(km.labels_)
print(np.unique(km.labels_, return_counts=True))