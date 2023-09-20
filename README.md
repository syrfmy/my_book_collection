
# my_book_collection

author: Muh. Syarief Mulyadi

Repo ini berisi tugas untuk mata kuliah Pemrograman Berbasis Platform 2023/2024

# Table Of Content:
1. [Tugas 2](#tugas-2)
2. [Tugas 3](#tugas-3)
3. [Tugas 4](#tugas-4)
4. [Tugas 5](#tugas-5)

## Tugas 2

**A. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

1. Membuat proyek Django baru.


    Untuk membuat projek django baru kita tinggal mengikuti langkah-langkah di tutorial 0 untuk membuat projek Django baru. Untuk projek ini saya akan membuatnya di direktori bernama my_book_collection
    Membuat aplikasi dengan nama main pada proyek tersebut

    Saya akan membuat aplikasi main dengan menjalankan perintah:

    
        python manage.py startapp main


    setelah itu saya akan menambahkan secara manual aplikasi main di file settings.py

2. Melakukan routing pada proyek agar dapat menjalankan aplikasi main.

    kita akan menambahkan routing url di dalam direktori projek utama kita yaitu my_book_collection. Berikut tampilannya setelah ditambahkan:
        
        '''
        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('main/', include('main.urls')),
        ]
        '''

3. Membuat model pada aplikasi main dengan nama Item dan atribut wajibnya.

    Untuk membuat model kita tinggal masuk ke dirktori main kita dan menambahkan class Buku yang merupakan item yang saya pilih. Selanjutnya saya kan menambahkan beberapa atribut untuk model tersebut.
        
        '''
        class Product(models.Model):
            name = models.CharField(max_length=255)
            amount = models.IntegerField()
            description = models.TextField()
        
        '''

4. Membuat sebuah fungsi pada views.py yang mengembalikan HTML yang berisi nama aplikasi dan nama kelas.

    Di dalam views.py saya akan membuat fungsi bernama show_main yang mana akan menampilkan HTML yang dipass bersama dengan variabel context yaitu nama dan kelas saya.

    Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py. Untuk melakukan routing aplikasi main kita, kita akan pertama-tama menambahkan berkas urls.py di dalam direktori main dan mengisinya dengan kode berikut:

        '''
        from django.urls import path
        from main.views import show_main

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
        ]
        '''

5. Melanjutkan deployment ke adaptable.

    Untuk melakukan deployment kita tinggal mengikuti langkah-langkah di tutorial 0 namun mengubahnya Start command Sebagai berikut:

        '''
        python manage.py migrate && gunicorn my_book_collection.wsgi
    '''

**B. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**

![Alt text](diagram/0001.jpg)
urls.py di direktori projek akan menghandle urls yang valid pada projek tersebut. 

views.py akan mendefinisikan fungsi menampilkan halaman html sebagai sebuah response. Dan mempass context ke template html kita

models.py berhubungan dengan data base kita. 


**C. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**
    
Kita menggunakan virtual environment untuk karena beberapa alasan berikut:

1. Isolasi Proyek: Virtual environment memungkinkan kita membuat lingkungan isolasi yang independen untuk setiap proyek.Ini berarti setiap proyek dapat memiliki dependensi Python (misalnya, paket atau library) yang berbeda tanpa interferensi dengan proyek lain. Ini menghindari masalah konflik versi dan memastikan proyek-proyek kita tetap bersih dan terpisah.


2. Manajemen Dependensi: Dengan venv, Anda dapat dengan mudah mengelola dan menginstal dependensi yang dibutuhkan untuk proyek kita. Kita dapat membuat file requirements.txt yang berisi daftar semua paket yang dibutuhkan, yang memungkinkan kita atau anggota tim lain untuk menginstalnya dengan mudah di lingkungan virtual yang sama.

    
**D. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.**

**MVC (Model-View-Controller):**

_Model_

Deskripsi: Model adalah komponen yang bertanggung jawab untuk mengelola data dan logika bisnis dalam aplikasi. Ini mencakup struktur data, operasi pada data, validasi, dan perubahan data.

Tugas: Model menghadirkan data kepada Controller, dan jika data berubah, Model memberi tahu Controller.

_View_

Deskripsi: View adalah antarmuka pengguna yang digunakan oleh pengguna untuk berinteraksi dengan aplikasi. Ini mencakup semua elemen tampilan seperti tombol, formulir, teks, dan tampilan lainnya.

Tugas: View menampilkan informasi dari Model kepada pengguna dan mengirim masukan pengguna ke Controller saat interaksi terjadi.
    
_Controller_

Deskripsi: Controller bertanggung jawab untuk mengontrol alur aplikasi. Ini menerima masukan dari pengguna melalui View, memprosesnya, dan mengkoordinasikan tindakan yang sesuai dengan Model.

Tugas: Controller mengambil tindakan berdasarkan masukan pengguna, memperbarui Model jika diperlukan, dan mengatur tampilan yang akan ditampilkan oleh View.
    
_Perbedaan utama MVC_:

MVC adalah pola desain arsitektur perangkat lunak yang memisahkan tanggung jawab antara Model, View, dan Controller. Memungkinkan pengembangan dan pemeliharaan aplikasi yang lebih mudah dan terstruktur dengan memisahkan logika bisnis, tampilan, dan kontrol.
    
**MVT (Model-View-Template):**

_Model_

Deskripsi: Mirip dengan Model dalam MVC, Model dalam MVT adalah komponen yang mengelola data dan logika bisnis aplikasi.

Tugas: Model mengelola data dan operasi pada data, serta menyediakan data untuk Template.
    
_View_

Deskripsi: View dalam MVT mirip dengan View dalam MVC. Ini adalah komponen yang bertanggung jawab untuk menampilkan data kepada pengguna.

Tugas: View menampilkan data yang diberikan oleh Model dan berinteraksi dengan Template.
    
_Template_

Deskripsi: Template adalah komponen yang unik untuk MVT. Ini adalah bagian dari sistem templating yang mengatur tampilan halaman web. Template berisi kode HTML dengan placeholder untuk data yang akan ditampilkan.

Tugas: Template mengambil data dari View dan menghasilkan halaman HTML yang akan ditampilkan kepada pengguna.
    
_Perbedaan utama MVT_

MVT adalah konsep yang digunakan dalam kerangka kerja Django, yang sering digunakan untuk pengembangan web. MVT menggabungkan Model, View, dan Template untuk menghasilkan halaman web dinamis.
    
**MVVM (Model-View-ViewModel):**

_Model_

Deskripsi: Seperti dalam MVC dan MVT, Model adalah komponen yang mengelola data dan logika bisnis aplikasi.

Tugas: Model mengelola data dan berkomunikasi dengan ViewModel saat data berubah.
    
_View_

Deskripsi: View adalah antarmuka pengguna yang digunakan oleh pengguna. Ini hanya menangani tampilan dan interaksi pengguna.
    
Tugas: View menampilkan data yang diberikan oleh ViewModel dan mengirim perubahan yang diberikan oleh pengguna ke ViewModel.
    
_ViewModel_

Deskripsi: ViewModel adalah perantara antara Model dan View. Ini mengelola presentasi data yang akan ditampilkan di View dan berfungsi untuk memisahkan logika tampilan dari Model.
    
Tugas: ViewModel mengambil data dari Model, memformatnya agar sesuai untuk ditampilkan di View, dan menerima masukan pengguna untuk kemudian diteruskan ke Model.
    
_Perbedaan utama MVVM_:

MVVM adalah pola desain arsitektur yang dirancang khusus untuk aplikasi berbasis antarmuka pengguna kompleks, seperti aplikasi mobile dan aplikasi desktop. Memungkinkan pengembang untuk memisahkan logika tampilan (View) dari Model, sehingga memudahkan pengujian dan pemeliharaan kode.

## Tugas 3

### Apa perbedaan antara form POST dan form GET dalam Django?

Dalam Django form POST dan GET adalah dua method HTTP request yang disupport. Perbedaan utama antara POST dan GET terletak pada caranya menghandle form request. Untuk POST, Browser menggabungkan data form, mengkodekannya untuk transmisi, mengirimkannya ke server, dan kemudian menerima kembali responsnya. Sedangkan untuk GET, sebaliknya, menggabungkan data yang dikirimkan ke dalam string, dan menggunakannya untuk menulis URL. URL berisi alamat tempat data harus dikirim, serta key dan value data.

Akibat properti ini, POST cocok digunakan untuk form yang bersifat sensitif seperti form login, sedangkan GET lebih cocok untuk form yang tidak sensitif seperti _search bar_

### Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?

XML sering digunakan dalam situasi di mana data perlu memiliki struktur yang baik, dapat menjelaskan dirinya sendiri, dan mudah dibaca oleh manusia. Ini umumnya digunakan dalam berkas konfigurasi, format pertukaran data seperti RSS dan Atom, dan sebagai dasar untuk bahasa markup lainnya.

JSON banyak digunakan untuk pertukaran data dalam API web, berkas konfigurasi, dan sebagai format penyimpanan data. Ini disukai karena kesederhanaan dan kemudahannya dalam aplikasi JavaScript.

HTML digunakan untuk membuat halaman web dan mendefinisikan struktur, konten, dan presentasinya. Biasanya tidak digunakan untuk pertukaran data, meskipun dapat mengangkut data dalam form web.

### Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?

JSON banyak digunakan dalam pertukaran data dalam aplikasi web modern karena hal-hal berikut:
1. Dibanding XML dan HTML, JSON memiliki format yang lebih ringan. Hal ini membuat beban data yang harus di transfer menjadi lebih kecil sehingga data dapat di transfer lebih cepat.
2. JSON yang merupakan kepanjangan dari Javascript Object Notation, memiliki format yang sama dengan Object model Javascript, hal ini membuat manipulasi data dari JSON cukup mudah. Dan ditambah dengan penggunaan Javascript di berbagai macam web app membuatnya mudah untuk di tangani.

### Langkah-langkah mengerjakan checkpoint

**1. Mengubah model sesuai dengan kebutuhan.**

Untuk tugas 3 saya akan menambahkan beberapa atribut baru untuk model saya. Atribut yang saya tambahkan adalah sebagai berikut:
    
1. author : Penulis atau pengarang dari buku
2. progress : Berapa persen bagian dari buku yang telah saya baca
3. description : Synopsis dari buku

jadi, sekarang model Product saya akan menjadi seperti berikut:

    '''

    class Product(models.Model):
        name = models.CharField(max_length=255, default="", blank=True)
        author = models.CharField(max_length=255, default="", blank=True)
        date_added = models.DateField(auto_now_add=True)
        progress = models.CharField(max_length=255, default="",blank=True)
        amount = models.IntegerField(default="", blank=True)
        description = models.TextField(default="", blank=True)
    
    '''

**2. Membuat input form untuk menambahkan objek model pada aplikasi**

Untuk membuat input form pertama-tama saya membuat file baru yang bernama direktori main bernama _forms.py_. File ini akan menghandle form untuk aplikasi kita. Selanjutnya saya akan membuat file html baru di folder templates di direktori main  yang bernama _create_product.html_. File ini akan berisi template halaman untuk menambahkan product.Selanjutnya saya menambahkan fungsi tambahan bernama create_product di file _views.py_ serta menambahkan urlpattern dari halaman untuk menambahkan product tersebut di file _urls.py_. Fungsi ini akan bertugas menampilkan halaman untuk menambahkan product ke database.

 berikut code dari fungsi create_product dan urlpattern halamannya:
    
    '''

        def create_product(request):
            form = ProductForm(request.POST or None)

            if form.is_valid() and request.method == "POST":
                form.save()
                return HttpResponseRedirect(reverse('main:show_main'))

            context = {'form': form}
            return render(request, "create_product.html", context)

    '''

        path('create-product', create_product, name='create_product'),

    '''

**3. Memodifikasi template lain untuk menampilkan product dan tombol untuk menambahkan product.**

Untuk menampilkan list product sebagai sebuah table saya akan membuat file html tambahan bernama  _book_table.html_ yang berisi bentuk komponen html dari table tersebut. Kemudian saya tinggal menambahkan komponen tersebut ke template html lain di mana table tersebut akan ditampilkan menggunakan keyword include. Selain itu, saya juga akan menambahkan tombol untuk menambahkan product ke halaman main. Tombol ini akan memiliki tautan yang terhubung dengan halaman create_product.

berikut kode dari file _book_table.html_:

'''

    <p>Number of book entry in my collection: {{products|length}}</p>
    <table>
        <tr>
            <th>Name</th>
            <th>Author</th>
            <th>Amount</th>
            <th>Description</th>
            <th>Reading Progress</th>
            <th>Date Added</th>
        </tr>

        {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

        {% for product in products %}
            <tr>
                <td>{{product.name}}</td>
                <td>{{product.author}}</td>
                <td>{{product.amount}}</td>
                <td>{{product.description}}</td>
                <td>{{product.progress}}</td>
                <td>{{product.date_added}}</td>
            </tr>
        {% endfor %}
    </table>

'''

Berikut tampilan file _main.html_ dimana komponen tersebut akan ditampilkan:

'''

    {% extends 'base.html' %}

    {% block content %}
    <h1>My Book Collection</h1>

    <h2>Name:</h2>
    <p>{{name}}</p>

    <h2>Class:</h2>
    <p>{{class}}</p>

    ...

    {% include 'book_table.html' %}

    <br />

    <a href="{% url 'main:create_product' %}">
        <button>
            Add New Product
        </button>
    </a>

    {% endblock content %}

'''

**4. Menambahkan 5 fungsi dalam format HTML, XML, JSON, XML by ID, dan JSON by ID**

Selanjutnya kita akan menambahkan fungsi untuk mengakses inventory dalam berbagai format dan method. Untuk fungsinya tidak beda dari yang diajarkan di tutorial. Untuk fungsi yang menampilkan HTML sendiri saya membuat file baru di folder templates direktori main. Yang mana file html ini bernama _show_book.html_. File ini yang akan ditampilkan pada pemanggilan fungsi show_book.

Berikut fungsi-fungsi yang ditambahkan di file views:

'''
    
    def show_book(request):
        context = {
            'products':Product.objects.all()
        }
        return render(request, "show_book.html", context)

    def show_xml(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type= "application/xml")

    def show_json(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    def show_xml_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

'''

Berikut isi file dari _show_book.html_:

'''

    {% extends 'base.html' %}

    {% block content %}

        {% include 'book_table.html' %}
        
    {% endblock %}

'''

**5. Melakukan routing url untuk berbagai fungsi yang telah ditambahkan dan menggunakan post man untuk mengakses url tersebut.**

Kelima fungsi tersebut akan ditambahkan ke urlpattern di file _urls.py_ dan mengaksesnya menggunakan Postman

Berikut url tambahan di urlpattern:

'''

    path('show_book', show_book, name='show_book'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 

'''

Berikut tampilan pengaksesan url tersebut menggunakan postman:

_show_book_

![Alt text](diagram/0002.png)

_XML_

![Alt text](diagram/0003.png)

_JSON_

![Alt text](diagram/0004.png)

_XML by ID_

![Alt text](diagram/0005.png)

_JSON by ID_

![Alt text](diagram/0006.png)

**6. Menambahkan indikator jumlah entry yang terdapat di dalam database.**

Untuk menambahkan indikator yang memperlihatkan berapa banyak product dalam hal ini buku yang terdapat di dalam database, Saya akan menambahkan satu line tambahan untuk di file _book_table.html_. Code ini akan berfungsi memperlihatkan berapa banyak entry yang terdapat di dalam database.

Berikut codenya:

'''

    <p>Number of book entry in my collection: {{products|length}}</p>

'''

{{products|length}} akan menampilkan berapa banyak entry yang terdapat di dalam database kita.

## Tugas 4

## Tugas 5