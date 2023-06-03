import os
import numpy as np

from PIL import Image
from data_load import image_numpy
from sklearn.cluster import KMeans

# 데이터 전처리
def preprocess_images(images):
    num_images, width, height, channels = images.shape
    reshaped_images = images.reshape(num_images, width * height, channels)
    return reshaped_images

# k-평균 알고리즘을 사용한 이미지 분류
def kmeans_clustering(image_data, num_clusters):
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(image_data)
    return kmeans.labels_

# 이미지 복원
def restore_images(labels, image_shape):
    num_images, num_pixels, channels = labels.shape[0], labels.shape[1], image_shape[2]
    restored_images = np.zeros((num_images, num_pixels, channels))
    for i in range(num_images):
        for j in range(num_pixels):
            restored_images[i, j] = kmeans.cluster_centers_[labels[i, j]]
    return np.uint8(restored_images.reshape(num_images, image_shape[0], image_shape[1], channels))

# 클러스터링 결과 저장
def save_clustered_images(images, labels, output_dir):
    num_images = images.shape[0]
    for i in range(num_images):
        img = Image.fromarray(images[i])
        img.save(output_dir + f"/clustered_image_{i}.jpg")
        print(f"Saved clustered image {i+1} to {output_dir}/clustered_image_{i}.jpg")

# 메인 함수
def main():
    # 이미지 데이터 전처리
    preprocessed_images = preprocess_images(image_numpy)

    # k-평균 알고리즘으로 이미지 분류
    num_clusters = 4
    labels = kmeans_clustering(preprocessed_images, num_clusters)

    # 이미지 복원
    restored_images = restore_images(labels, image_numpy.shape)

    # 클러스터링 결과 저장
    output_dir = "../Final_Project_Data/Clustered_Images/"
    os.makedirs(output_dir, exist_ok=True)
    save_clustered_images(restored_images, labels, output_dir)

if __name__ == '__main__':
    main()
