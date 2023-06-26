import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import colors



def k_means_for_gray_m(image, K, iteration):
    # Gri-seviyeli görüntüyü 1 boyutlu sütun vektörüne dönüştürüyoruz
    image_vector = image.reshape((-1, 1))
    
    # Küme merkezleri için başlangıç değerlerini rastgele seçiyoruz
    np.random.seed(42)
    centers = np.random.randint(0, 256, size=(K, 1))


    # Öklid ile kümeleme işlemini 5 kez tekrarlayalım
    for _ in range(5):
        euclidean_distances = np.abs(image_vector - centers[:, np.newaxis])
        labels = np.argmin(euclidean_distances, axis=0)
        
        for k in range(K):
            cluster_data = image_vector[labels == k]
            if len(cluster_data) > 0:
                new_center = np.mean(cluster_data)
                if not np.array_equal(new_center, centers[k]):
                    centers[k] = new_center
    pixel_labels = centers[labels.flatten()]
    print("FINAL IMAGE: ",pixel_labels)

    initial_centers = np.copy(centers)
    print("INITIAL CENTERS: ",initial_centers)
    initial_variances = np.zeros_like(initial_centers)
    print("INITIAL VARIANCES: ",initial_variances)
    # Mahalanobis uzaklığını hesaplama ve etiketleme
    for i in range(iteration):
        distances = np.zeros((len(image_vector), K))
        cluster_means = np.zeros_like(centers)
        cluster_variances = np.zeros_like(centers)
        threshold = 0.1
        for k in range(K):
            cluster_data = image_vector[labels == k]
            print("CLUSTER DATA: ",cluster_data)
            cluster_mean = np.round(np.mean(cluster_data,axis=0),6)
            cluster_means[k] = cluster_mean  # cluster_means'e ekleme
            print("CLUSTER MEAN: ",cluster_mean)
            cluster_variance = np.round(np.var(cluster_data,axis=0),6)
            # Varyans eşik değeri kontrolü
            if cluster_variance < threshold:
                cluster_variance = threshold
            cluster_variances[k] = cluster_variance  # cluster_variances'e ekleme
            print("CLUSTER VARIANCE: ",cluster_variance)
            distances[:, k] = np.squeeze(np.round(np.sqrt((np.square(image_vector - cluster_mean)) / cluster_variance), 6)) 
        #max_distance = np.max(distances[np.isfinite(distances)])  # NaN olmayan maksimum uzaklık değeri
        #distances[np.isnan(distances)] = max_distance 
        print("DISTANCES: ",distances) 
        labels = np.argmin(distances, axis=1)

        for k in range(K):
        # Burada her küme için etiketli pikselleri elde ediyoruz
            cluster_data = image_vector[labels == k]
            # Her küme için o kümenin etiketiyle etiketlenmiş en az bir piksel var mı kontrolünü sağlıyoruz
            if len(cluster_data) > 0:
                # Küme merkezini ortalamaya göre güncelliyoruz
                new_center = np.mean(cluster_data, axis=0)
                # Eğer yeni küme merkezi bir önceki değeriyle aynı değilse küme merkezini güncelliyoruz
                if not np.array_equal(new_center,centers[k]):
                    centers[k] = new_center

        print("KONTROLLER:     ", cluster_means,initial_centers,cluster_variances,initial_variances)
        if np.array_equal(cluster_means, initial_centers) and np.array_equal(cluster_variances, initial_variances):
            print("Algoritma optimal parametrelerine {}. dongude ulasmistir...".format(i+1))
            break
        
        initial_centers = np.copy(cluster_means)
        initial_variances = np.copy(cluster_variances)

    # Final_image'ı sütun vektörü olarak oluşturma
    pixel_labels = initial_centers[labels.flatten()]
    final_image = pixel_labels.reshape(image.shape).astype(np.uint8)

    # Segmentasyon yapılmış görüntümüz için kümelerin histogramlarını gösteren kodu yazıyoruz
    fig, ax = plt.subplots()
    cluster_counts = [np.sum(labels == i) for i in range(K)]
    ax.bar(range(1, K+1), cluster_counts, color=[f'C{i}' for i in range(K)], edgecolor='black', linewidth=1.2)
    ax.set_xlabel('Kümeler')
    ax.set_ylabel('Her Küme İçin Piksel Sayısı')
    ax.set_title('Kümelerin Histogram Grafiği')

    # Tablo oluştur
    centroid_table = pd.DataFrame({'Küme': [f'Küme {i+1}' for i in range(K)],
                                   'Merkez Noktası': centers.flatten(),
                                   'Piksel Sayısı': cluster_counts})
    centroid_table.set_index('Küme', inplace=True)
    print('\n' + '-'*50)
    print('Gri-Seviyeli Bir Görüntü İçin K-Means Algoritması')
    print('-'*50)
    print(centroid_table)

    # Görseli göster
    plt.show()
    
    # Görüntüyü gösterme
    plt.imshow(final_image, cmap='gray')
    plt.axis('off')
    plt.show()
    cv2.imshow("Olusan goruntu",final_image)

K = int(input("Kume sayisini giriniz: "))
iteration = int(input("İterasyon sayisini giriniz: "))
image = cv2.imread('rookie.jpg')
cv2.imshow('Kullanilan Goruntu',image)
image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
k_means_for_gray_m(image,K,iteration)
cv2.imshow('Gri-Seviyeli Goruntu',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
