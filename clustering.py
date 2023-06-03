from data_load import image_numpy as image
from sklearn.cluster import KMeans

km = KMeans(n_clusters=4, random_state=42)
km.fit(image)