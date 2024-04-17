# Brazillian E-Commerce Data Analysis

<p align='center'><img src="https://github.com/SyarifulMsth/Brazillian-E-Commerce-Data-Analysis/blob/main/image/image.jpg?raw=true"  width="1000"></p>
 
## 📌 Business Understanding

### Problem Statement

Rumusan masalah (*problem statements*) pada proyek ini di antaranya sebagai berikut :
1. Bagaimana segmentasi pelanggan berdasarkan wilayah?
2. Bagaimana segmentasi penjual berdasarkan wilayah?
3. Bagaimana performa pelayanan berdasarkan status pengiriman pesanan?
4. Bagaimana tingkat kepuasan pelanggan?
5. Apakah terdapat tren dalam metode pembayaran yang digunakan oleh pelanggan?
6. RFM Analysis?

### Goals

Berdasarkan rumusan masalah (*problems statement*) yang telah dirumuskan sebelumnya, maka berikut adalah tujuan (*goals*) dari proyek ini :

1. Mengetahui bagaimana segmentasi pelanggan berdasarkan wilayah
2. Mengetahui bagaimana segmentasi penjual berdasarkan wilayah
3. Mengetahui bagaimana performa pelayanan berdasarkan status pengiriman pesanan
4. Mengetahui bagaimana tingkat kepuasan pelanggan
5. Mengetahui apakah terdapat tren dalam metode pembayaran yang digunakan oleh pelanggan
6. Mengetahui penerapan dan hasil dari RFM Analysis

### Solution Statements

Berdasarkan *problem statements* dan *goals* yang telah disebutkan sebelumnya, maka berikut adalah *solution statements* pada proyek ini :
1. Melakukan tahapan *data wrangling* yang meliputi *gathering data*, *data assesing*, dam *data cleansing*.
2. Melakukan Exploratory Data Analysis untuk mendapatkan *insight* yang berguna dari data.
 

## 📚 Data Understanding 
Pada project ini *dataset* yang digunakan adalah [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) yang terdiri dari 9 tabel data, di antaranya yaitu :
  
- *olist_customers_dataset.csv*
- *olist_geolocation_dataset.csv*
- *olist_order_items_dataset.csv*
- *olist_order_payments_dataset.csv*
- *olist_order_reviews_dataset.csv*
- *olist_orders_dataset.csv*
- *olist_products_dataset.csv*
- *olist_sellers_dataset.csv*
- *product_category_name_translation.csv*

### Variabel Dataset

- **Tabel customers**: tabel ini menyimpan berbagai informasi terkait customer, meliputi customer_id, customer_unique_id, customer_zip_code_prefix, customer_city, dan customer_state.

- **Tabel geolocation** : tabel ini menyimpan berbagai informasi terkait zip code dan lat/lng coordinates, meliputi geolocation_zip_code_prefix, geolocation_lat, geolocation_lng,geolocation_city, dan geolocation_state.

- **Tabel order items** : tabel ini menyimpan berbagai informasi terkait barang/product yang dibeli untuk setiap pesanan, meliputi order_id, order_item_id, product_id, seller_id, shipping_limit_date, price, dan freight_value.

- **Tabel order payments** : tabel ini menyimpan berbagai informasi terkait opsi pembayaran pesanan, meliputi order_id, payment_sequential, payment_type, payment_installments, dan payment_value.

- **Tabel order reviews** : tabel ini menyimpan berbagai informasi terkait ulasan (*review*) yang dibuat oleh pelanggan, yang meliputi review_id, order_id, review_score, review_comment_title, review_comment_message, review_creation_date, dan review_answer_timestamp.

- **Tabel orders** : tabel ini menyimpan berbagai informasi terkait setiap pesanan (*order*), yang meliputi order_id, customer_id, order_status, order_purchase_timestamp, order_approved_at, order_delivered_carrier_date, order_delivered_customer_date, dan order_estimated_delivery_date.

- **Tabel products** : tabel ini menyimpan berbagai informasi terkait produk yang dijual, yang meliputi product_id, product_category_name, product_name_lenght, product_description_lenght, product_photos_qty, product_weight_g, product_length_cm, product_length_cm, dan product_width_cm.

- **Tabel sellers** : tabel ini menyimpan berbagai informasi terkait penjual yang memenuhi pesanan, yang meliputi seller_id, seller_zip_code_prefix, seller_city, dan seller_state.

- **Tabel product category name translation** : tabel ini menyimpan berbagai informasi untuk menerjemahkan nama kategori produk ke bahasa Inggris.

## 📚 Data Preparation
*Data preparation* adalah proses mempersiapkan data mentah menjadi format yang sesuai untuk analisis atau pemrosesan lebih lanjut. Berikut adalah beberapa teknik atau metode yang digunakan dalam persiapan data pada proyek ini:

1. **Handling missing value** 
	- *Missing value* merupakan salah satu masalah yang paling sering dijumpai dalam proyek analisis data di industri. Masalah ini muncul karena adanya nilai yang hilang dari sebuah data dan biasanya direpresentasikan sebagai nilai NaN dalam library pandas. Hal ini biasanya terjadi karena adanya *human error*, masalah privasi, proses *merging/join*, dll. 
	- Tujuan dari langkah ini adalah untuk memastikan keakuratan dan keandalan data yang digunakan untuk analisis. *Missing value* dapat menyebabkan bias dan kesalahan dalam analisis data, sehingga penting untuk mengidentifikasi dan mengatasi nilai yang hilang ini agar hasil analisis menjadi lebih akurat dan dapat diandalkan.
	- Terdapat beberapa cara atau metode yang dapat digunakan  untuk menangani *missing value*, yaitu *Dropping*, *Imputation*, *Interpolation*, dan lainnya. 
		
2. **Handling duplicated data**
	- *Duplicated data* adalah masalah lain yang umum dijumpai di industri. Ia terjadi ketika terdapat sebuah observasi (semua nilai dalam satu unit baris) yang memiliki nilai yang sama persis pada setiap kolomnya. 
	-  Tujuan dari langkah ini adalah untuk memastikan integritas data. *Duplicated data* dapat mempengaruhi analisis data dan membuat hasil yang tidak akurat. Oleh karena itu, dengan mengidentifikasi dan menghapus data yang terduplikat, dapat memastikan bahwa data yang digunakan untuk analisis adalah data yang valid dan representatif.
	-  Salah satu teknik yang dapat digunakan dalam mengatasi *duplicated data* adalah dengan menghapus data yang terduplikat (*dropping*).		

3. **Feature Engineering**
<br> *Feature Engineering* merupakan sebuah proses untuk mengembangkan dan memilih suatu fitur atau atribut (features) yang akan digunakan untuk melakukan analisis data.

### Visualization & Analysis 

<p align='center'><img src ="https://github.com/SyarifulMsth/Spotify-Music-Recommendation-System-/blob/main/images/artist.png?raw=true"  width="500"></p>
<p align='center'>Gambar 1. Top 10 Artist dengan Popularity Tertinggi</p> Berdasarkan visualisasi grafik pada gambar 1 di atas menunjukkan 10 Artist dengan *popularity* tertinggi di dataset. 
 
<p align='center'><img src ="https://github.com/SyarifulMsth/Spotify-Music-Recommendation-System-/blob/main/images/years.png?raw=true"  width="500"></p>
<p align='center'>Gambar 2. Jumlah Lagu atau Musik Berdasarkan Tahun</p> Berdasarkan visualisasi pada gambar 2 di atas, ditunjukkan jumlah lagu untuk setiap tahunnya yang ada di dataset.

<p align='center'><img src ="https://github.com/SyarifulMsth/Spotify-Music-Recommendation-System-/blob/main/images/genres.png?raw=true"  width="500"></p>
<p align='center'>Gambar 3. Jumlah Lagu atau Musik Berdasarkan Genre</p> Berdasarkan visualisasi pada gambar 3 di atas, ditunjukkan jumlah lagu berdasarkan genre yang ada di dataset.


## Conclusion

### Segmentasi pelanggan berdasarkan wilayah
Dari hasil analisis data, terlihat bahwa **Sao Paulo** memiliki jumlah pelanggan terbesar, diikuti oleh **Rio De Janeiro** dan **Belo Horizonte** berdasarkan kota tempat tinggal pelanggan. Sementara itu, jika kita melihat berdasarkan negara bagian (State), pelanggan terbanyak ada di **SP** (Sao Paulo), **RJ** (Rio de Janeiro), dan **MG**(Minas Gerais).

Informasi ini dapat memberikan wawasan berharga kepada para pemangku kepentingan (*stakeholder*) dalam proses pengambilan keputusan. Dengan melihat tingginya jumlah pelanggan di Sao Paulo, Rio de Janeiro, dan Belo Horizonte, stakeholder dapat menyadari bahwa wilayah-wilayah ini memiliki potensi besar untuk pengembangan bisnis atau peningkatan pelayanan. Hal ini bisa mencakup upaya seperti meningkatkan strategi promosi, pemasaran yang lebih intensif, atau menyediakan layanan khusus guna mengakomodasi permintaan yang signifikan di wilayah tersebut.

### Segmentasi penjual berdasarkan wilayah
Dari hasil  analisis data, terlihat bahwa **Sao Paulo** memiliki jumlah penjual terbesar, diikuti oleh **Curitiba** dan **Rio De Janeiro** berdasarkan kota tempat tinggal penjual. Sementara itu, jika kita melihat berdasarkan negara bagian (State), penjual terbanyak ada di **SP** (Sao Paulo), **PR** (Paraná), dan **MG**(Minas Gerais).

### Performa atau kinerja berdasarkan status pesanan dari pelanggan
Berdasarkan analisis data, diperoleh beberapa *insights* terkait performa atau kinerja berdasarkan status pesanan dari pelanggan, yaitu sebanyak **96478** tercatat dalam status ***delivered***, **1107** dalam status ***shipped***, **625** dalam status ***canceled***, dan seterusnya. Hal tersebut dapat diartikan bahwa performa atau kinerja status pesanan dari pelanggan tergolong dalam kategori baik.

### Tren metode pembayaran
Berdasarkan analisis data, terdapat beberapa variasi dalam metode pembayaran yang digunakan oleh pelanggan, termasuk Boleto, Kartu Kredit, Kartu Debit, Voucher, dan metode "not_defined." Dari berbagai pilihan ini, metode pembayaran paling umum yang dipilih oleh pelanggan adalah **Kartu Kredit (*Credit Card*)**, dan rata-rata nilai pembayaran yang dilakukan dengan metode ini lebih tinggi dibandingkan dengan metode pembayaran lainnya.

Informasi ini dapat menjadi dasar bagi pihak yang berkepentingan (*stakeholder*) untuk mengambil keputusan, seperti memberikan promosi atau diskon kepada pelanggan yang menggunakan Kartu Kredit sebagai metode pembayaran.

### Tingkat kepuasan pelanggan
Berdasarkan hasil analisis data dan *insights* yang telah diperoleh, diketahui bahwa:
- 66343 pelanggan memberikan 5 bintang *review score*
- 22319 pelanggan memberikan 4 bintang *review score*
- 15425 pelanggan memberikan 3 bintang *review score*
- 9894 pelanggan memberikan 2 bintang *review score*
- 4162 pelanggan memberikan 1 bintang *review score*
 
Dengan demikian, dapat disimpulkan bahwa sebagian besar pelanggan mengungkapkan kepuasan mereka dengan memberikan penilaian tinggi, terutama dengan pemberian 4 dan 5 bintang dalam *review score*.

### RFM Analysis
Berdasarkan hasil RFM Analysis dan visualisasi data di atas, dapat diketahui beberapa pelanggan terbaik berdasarkan parameter *Recency*, *Frequency* dan *Monetary*.

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://syarifulmsth.github.io) [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/syariful-musthofa/) [![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/)

## Feedback
*If you have any feedback, please reach out at* syarifulm007@gmail.com
