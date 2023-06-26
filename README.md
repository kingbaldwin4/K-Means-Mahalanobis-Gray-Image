# K-Means-Mahalanobis-Gray-Image
K-Means Algorithm For Gray-Scale Image Segmentation Using Mahalanobis Distance(Mahalanobis Uzaklığını Kullanarak K-Means Algoritmasıyla Gri-Seviyeli Bir Görüntüde Segmentasyon Yapıyoruz)

Türkçe:

K-Means Algoritmasının Mahalanobis Uzaklığını kullanarak gri-seviyeli bir görüntüde segmentasyonunu kodlamaya çalıştım

Öncelikle K-Means algoritması eğer mahalanobis uzaklığını kullanırsa, bu durumda biz bir kümedeki tüm pikselleri dikkate alıyoruz demektir. Yani kümelerimizin modellenişi eliptik olmaktadır.

Dolayısıyla kümelerimizin bir merkez noktasının yanısıra bir de varyansı bulunmaktadır.

Gri-Seviyeli görüntüler tek renk kanalı içerdikleri için kanal bazında 1-boyutludurlar. Dolayısıyla her piksel için hesaplanacak olan Mahalanobis Uzaklığı da 1-boyutlu olacaktır.

Bu durumda uzaklık hesabı: (pixel - center) / variance şeklinde gerçekleştirilecektir. Bu formül Gauss dağılımındaki üstel ifadede bulunan (x - u) / sigma'dan gelmektedir.

Mahalanobis, kümelerdeki tüm pikselleri baz aldığı için bizim elimizde kümelenmiş bir görüntü olması gerekiyor. 

Bu yüzden ilk başta görüntüyü, Mahalanobis iterasyonunda kullanabilmek için Öklid uzaklığıyla basitçe segmente ettim.

Algoritmanın sonlandırılması sadece küme merkezlerinin değişmemesine değil aynı zamanda kümelerin varyans değerlerinin de değişmemesine bağlıdır.

NOT: Bu tarz algoritmalarda kullanılan görüntü ve girilecek küme sayısı çok önemlidir. Bu algoritmalar her görüntü için iyi bir performans gösteremeyebilir.

NOT 2: Ayrıca girilen küme sayısı da belirli değeri aşarsa yine iyi sonuçlar elde edilemeyebilir.

NOT 3: Kümeler için gelecek varyans değerlerinin çok küçük olması, algoritmada istenmeyen sonuçlar doğurabileceğinden koduma varyans değerleri minimum 0.1 olacak şekilde bir if şartı ekledim.

Bu yüzden örnek bir görüntüyü de kodumla beraber ekledim. Küme sayısını 3-4-5-6 gibi değerler girerek verimli sonuçlar alabilirsiniz.

English:

I tried to code the segmentation of a grayscale image using the K-Means algorithm with Mahalanobis Distance.

Firstly, if the K-Means algorithm uses Mahalanobis Distance, it means that we are considering all the pixels in a cluster. So, the modeling of our clusters will be elliptical. Therefore, in addition to a center point, each cluster will also have a variance.

Grayscale images contain only one color channel, so they are 1-dimensional per channel. Thus, the Mahalanobis Distance to be calculated for each pixel will also be 1-dimensional. The distance calculation will be performed as (pixel - center) / variance. This formula comes from the exponential expression in the Gaussian distribution, (x - u) / sigma.

Since Mahalanobis considers all pixels in the clusters, we need to have a clustered image to be able to use it in the Mahalanobis iteration. Therefore, I initially segmented the image simply using Euclidean distance for the Mahalanobis iteration.

The termination of the algorithm depends not only on the centers of the clusters not changing but also on the variance values of the clusters not changing.

NOTE: The image and the number of clusters entered are crucial in these types of algorithms. These algorithms may not perform well for every image.<

NOTE 2: Additionally, if the number of clusters entered exceeds a certain value, efficient results may not be obtained.<

NOTE 3: Since having very small variance values for the clusters can lead to undesirable results in the algorithm, I have added a conditional statement to ensure that the variance values in my code are a minimum of 0.1.

Therefore, I also provided a sample image along with the code. You can enter values like 3, 4, 5, 6 for the number of clusters to obtain meaningful results.
