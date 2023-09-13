# my_book_collection
Repo untuk tugas 1 PBP

1. Membuat proyek Django baru
    Untuk membuat projek django baru kita tinggal mengikuti langkah-langkah di tutorial 0 untuk membuat projek Django baru. Untuk projek ini saya akan membuatnya di direktori bernama my_book_collection
2. Membuat aplikasi dengan nama main pada proyek tersebut
    Saya akan membuat aplikasi main dengan menjalankan perintah:
    "python manage.py startapp main"

    setelah itu saya akan menambahkan secara manual aplikasi main di file settings.py
3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main
    kita akan menambahkan routing url di dalam direktori projek utama kita yaitu my_book_collection. Berikut tampilannya setelah ditambahkan:
    "
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('main/', include('main.urls')),
    ]
    "

4. Membuat model pada aplikasi main dengan nama Item dan atribut wajibnya

    Untuk membuat model kita tinggal masuk ke dirktori main kita dan menambahkan class Buku yang merupakan item yang saya pilih. Selanjutnya saya kan menambahkan beberapa atribut untuk model tersebut.
    
    class Product(models.Model):
        name = models.CharField(max_length=255)
        amount = models.IntegerField()
        description = models.TextField()

5. Membuat sebuah fungsi pada views.py yang mengembalikan HTML yang berisi nama aplikasi dan nama dan kelas
    Di dalam views.py saya akan membuat fungsi bernama show_main yang mana akan menampilkan HTML yang dipass bersama dengan variabel context yaitu nama dan kelas saya.

6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
    
    Untuk melakukan routing aplikasi main kita, kita akan pertama-tama menambahkan berkas urls.py di dalam direktori main dan mengisinya dengan kode berikut:
    "
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    "

7. Melanjutkan deployment ke adaptable
    Untuk melakukan deployment kita tinggal mengikuti langkah-langkah di tutorial 0 namun mengubahnya Start command Sebagai berikut:

    "
    python manage.py migrate && gunicorn my_book_collection.wsgi.
    " 
