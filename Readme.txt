Note : Berikut ini merupakan beberapa hal yang perlu dilakukan 
       jika menggunakan google colab untuk menjalankan program

1. Terlebih dahulu upload semua file yang ada di dalam folder TSP ini ke directory google colab
   Adapun tutorial mengupload file ke google colab ada di link berikut : https://www.dqlab.id/belajar-python-dengan-google-colab pada poin nomer 3

2. Terlebih dahulu lakukan instalasi library menggunakan pip pada google colab
   Adapun beberapa library yang perlu di install terlebih dahulu adalah:
   a. sympy -> pip install sympy
   b. tsp-python -> pip install tsp-python
   c. folium -> pip install folium

3. Setelah melakukan instalasi semua library yang dibutuhkan, lakukan restart runtime pada google colab. 
   Adapun langkah restart runtime adalah sebagai berikut:
   a. Cari dan tekan panel "runtime" pada bagian kiri atas halaman google colab
   b. Dalam panel "runtime" akan terdapat pilihan "restart runtime", pilih opsi tersebut
      dan google colab automatis melakukan restart runtime

4. Copy kan semua syntax pada file tsp-mput.py pada suatu cell

5. Copy kan semua syntax pada file maps.py pada cell yang berbeda dengan cell dimana anda meng copy syntax
   dalam file tsp-mput.py

6. Kemudian jalankan semua cell yang ada di google colab

7. Tunggu proses berjalan. Ketika proses sudah selesai, maka akan muncul tambahan file bernama "peta.html"
   pada directory colab anda

8. Download file "peta.html" tersebut kemudian buka file tersebut menggunakan browser yang anda gunakan.
   Usahakan menggunakan browser google chrome

9. Dan voala, program telah selesai

Tambahan : Jika ada data kota baru yang ingin di inputkan pada data_kota, mohon data kota baru tersebut ditaruh di akhir setelah "Kotagede"