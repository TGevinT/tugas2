# Tugas 4
## Nama  : Teuku Gevin Taufan
## NPM   : 2106750194
## Kelas : PBP F
## Asdos : DRY

[Heroku Link todolist](https://tugas2teukugevin.herokuapp.com/todolist/)
<br>
username1 : saitama    pass1: onepunchman
<br>
username2 : wibu       pass2 : baubawang
<br> 

## Apa kegunaan ```{% csrf_token %}``` pada elemen ```<form>```? 
CSRF(Cross Site Request Forgery) adalah sebuah serangan yang membuat pengguna internet  tanpa sadar mengirimkan request (permintaan) kepada suatu 
aplikasi website melalui aplikasi website yang sedang digunakan. Jadi kegunaan ```{% csrf_token %}``` untuk menghindari serangan tersebut didalam
form. Cara kerjanya ```{% csrf_token %}``` akan membuat token sesaat terhubung pada halaman/web yang token tersebut berguna untuk menentukan apakah
permintaan tersebut berasal dari pengguna yang memiliki otoritas atau bukan.

##  Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen ```<form>```?
Ketika di selesai input pada form akan keluar 403 error karena tidak menemukan csrf token.

## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? 
Bisa, jadi kita buat langsung secara manual dengan method input di .html yang memerlukan form

## jelaskan secara gambaran besar bagaimana cara membuat secara manual.
Andaikan pada tugas tersebut ```create-task.html``` form dibuat secara manual (tidak memerlukan forms.py) dan perlu diganti juga
views.py class create_task beberapa


create-task.html(manual form)
```
...
<form method="POST" action="">
    {% csrf_token %}
    <input type="text" placeholder="Title" name="title">
    <input type="text" placeholder="Description" name="description">
    <input type="submit" class="btn btn-primary" value="Create"></input>
</form>
...
```
di sini, ada input yang menyimpan nilainya dibuat secara manual

create_task class in views.py(manual form)
```
...
def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task.objects.create(title=title, description=description, user=request.user)
        task.save()
        return redirect('todolist:show_todolist')

    context = {}
    return render(request, 'create_task.html', context)
...
```
disini ditambahkan parameter title dan description untuk mengambil nilai d dapatkan dari input di ```create-task.html```

## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Sesudah user melakukan submisi atau perubahan dari html(web), data user tersebut akan ditranfer ke ```views.py``` menuju class mengeksekusi tugas perubahan yang diarahkan urls.py pattern.
Setelah itu, akan dibuat instance dari model baru dari hasil tranfer data user berdasarkan atribut yang tersimpan. Kemudian instance model tersebut akan di simpan di database. Dengan code khusu
instance-intance yang sudah ada akan diambil dari database dan ditampilkan ke html(web).

## Cara kamu mengimplementasikan checklist di atas
### Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya
buka cmd, cd ke alamat tugas tersebut, melakukan ```env\Scripts\activate.bat``` sesudah itu jalankan ```python manage.py startapp todolist```.

### Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.
di folder project_django, di settings.py, di INSTALLED_APPS tambahkan ```'todolist'```. Di urls.py di urlpatterns tambahkan ```path('todolist/', include('todolist.urls')),```

### Membuat sebuah model Task yang memiliki atribut sebagai berikut:
Bisa dilihat dari dari models.py di folder todolist atau klik [model.py](https://github.com/TGevinT/tugas2/blob/main/todolist/model.py) dengan penambahan ```is_finished``` (bonus)
dan tidak lupa di cmd tadi jalankan ```python manage.py makemigrations``` dan  ```python manage.py migrate``` jika menambahkan dan membuat
model karena perlu diterapkan juga di databasenya

### Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.
Bisa dilihat [views.py](https://github.com/TGevinT/tugas2/blob/main/todolist/views.py) untuk logiknya, html untuk [login](https://github.com/TGevinT/tugas2/blob/main/todolist/templates/login.html),
dan html untuk [register](https://github.com/TGevinT/tugas2/blob/main/todolist/templates/todolist.html) class di views.py untuk login adalah ```login_user```,
registrasi adalah ```register```, dan logout adalah ```logout_user```.


### Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
Bisa dilihat [todolist.html](https://github.com/TGevinT/tugas2/blob/main/todolist/templates/todolist.html) implementasi todolist beserta bonusnya 
dan logika untuk mengirim datanya [views.py](https://github.com/TGevinT/tugas2/blob/main/todolist/views.py), di class show_todolist

### Membuat halaman form untuk pembuatan task. Data yang perlu dimasukkan pengguna hanyalah judul task dan deskripsi task.
Bisa dilihat [create-task.html](https://github.com/TGevinT/tugas2/blob/main/todolist/templates/create-task.html) implementasi pembuatan task,
 ada ```{{ form.as_p }}``` dari html tersebut yang di hasilkan dari [form.py](https://github.com/TGevinT/tugas2/blob/main/todolist/forms.py)
dan logikan dari class create_task berada di [views.py](https://github.com/TGevinT/tugas2/blob/main/todolist/views.py). logika tersebut untuk 
membuat instance baru dari input user dan menambahkannya ke data base, forms untuk menampilkan input apa saja yang diperlukan user, 
dan create-task.html tempat user melihatnya input apa saja yang diperlukan dan menginputnya.

### Membuat routing sehingga beberapa fungsi dapat diakses melalui URL berikut
Bisa dilihat di [urls.py](https://github.com/TGevinT/tugas2/blob/main/todolist/urls.py) rooting semuanya yang bisa dibuka dari ```http://localhost:8000/todolist```

###  Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
Karena mengunakan repo sama dengan tugas-tugas sebelumnya jadi saya sudah melakukan deployment

### Membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.
Akun 1 (Username : saitama, Password : onepunchman) dan Akun 2 (Username : wibu, Password : baubawang)

## todolist.html akun 1 di web yang sudah di deployment di heroku
![alt text](./assets/todolist_saitama.png "todolist_saitama-image")

## todolist.html akun 2 di web yang sudah di deployment di heroku
![alt text](./assets/todolist_wibu.png "todolist_wibu-image")

# Tugas 5
## Perbedaan Inline, Internal, dan External CSS
### Inline
Inline adalah cara membuat style langsung dari atributnya, setiap atribut memilki style jadi dari situlah bisa langung kita style kan cssnya. Kekurangannya cara style ini
kurang efisien disebabkan ada style yang bisa digunakan berkali-kali tapi kita harus mendeskripsikan terus stylenya di atribut tersebut

### Internal
Internal dalam style css menggunkan tag ```<style>``` dan kode HTML dituliskan di bagian atas (header) file HTML. Cara style tersebut bagus jika ingin membuat halaman web yang unik
(kurang mirip dengan website lain) karena style tersebut hanya bisa digunkan di dalam HTML tersebut saja.

### External
Eksternal CSS adalah kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi
```.css```. File eksternal CSS biasanya diletakkan setelah bagian ```<head>``` pada halaman.
Cara ini lebih sederhana dan simpel daripada menambahkan kode CSS di setiap elemen HTML yang ingin Anda atur tampilannya. 

## Tag HTML5
- <p> - Menampilkan teks berukuran normal.
- <h1> ... <h6> - Menampilkan Teks dengan ukuran berbeda-beda, <h1> paling kecil, <h6> paling besar.
- <a> - Teks tersebut ketika ditekan bisa mengarahkan link yang di simpan di href.
- <div> - Tag ini dapat membungkus dan memisahkan elemen-elemen lain.
- <form> - Tag ini akan membuat form yang dapat mengirimkan request POST/UPDATE/DELETE.
- <input> - Tag ini digunakan di dalam tag <form> yang dapat menerima masukan dari pengguna. Atribut type menentukan jenisnya.
- <button> - Tag ini akan membuat sebuah kotak yang dapat ditekan layaknya tombol.
- <span> - Tag ini bekerja mirip dengan <div> tapi hanya dalam 1 baris teks.
- <br> - Tag ini akan membuat baris baru.
- <hr> - Tag ini akan membuat garis pemisah.
- <table> - Tag ini akan membuat tabel dengan <tr> sebagai baris dan <td> sebagai kolom/data.
- <nav> - Tag ini mendefinisikan sebuah navbar
- <tb> - Tag ini mendefinisikan kolom sebuah tabel (harus didalam tag <table>)
- <tr> - Tag ini mendefinisikan baris sebuah tabel (harus didalam tag <table>)
- <th> - Tag ini mendefinisikan baris pertama yang biasanya diisi hal yang mau kita input (harus didalam tag <table>)

## CSS selector
### Element selector
Ini mengubah atau mengedit content yang di dalam tag yang terdapat di HTML
formatnya ```p{...}```

### Class selector
Ini mengubah atau mengedit content dari tag yang mendefinisikan class di HTML
formatnya ```.content_table{...}```

### Id selector
Ini mengubah atau mengedit content dari tag yang mendefinisikan id di HTML
formatnya ```#myHeader{...}```

## To do
### Kustomisasi templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma)
Pada Tugas 5 kali ini saya memakai Tailwind, karena menurut saya penerapan css mengunakan class lumayan mudah dan banyak documentasinya.
Supaya HTML saya bisa menggunakan CSS framework Tailwind, Tambahkan ```<script src="https://cdn.tailwindcss.com"></script>``` pada
base.html bagian header (supaya bisa diakses frameworknya)

### Kustomisasi templat untuk halaman login, register, dan create-task semenarik mungkin.
Menurut saya sudah menarik dan saya bangga, dalam hal desain mungkin saya kurang bagus tapi saya menyukai karya edit html saya tersebut

### Kustomisasi halaman utama todo list menggunakan cards. (Satu card mengandung satu task).
```
...
{% for task in task_object%}
    <div class="card w-80 h-80 border-8 border-pink-600 divide-y-4 divide-pink-600 bg-indigo-500 p-2 backdrop-blur-sm transition ease-in-out hover:-translate-y-1 hover:scale-150 hover:bg-white duration-300">
...
``` 
dengan begini task yang dihasilkan akan berbentuk cards

### responsive design
Saya menggunakan dari documentasi Tailwind yaitu berdasarkan breakpoint prefix, jadi misal sudah saya beberapa pixel makan akan berubah bentuk webnya untuk menyuaikan
breakpoint prefix di pixel ada 5 yaitu sm:640px, md:768px, lg: 1024px, xl: 1280px, dan 2xl: 1536px. Sebenarnya bisa juga menggunakan @media (min-width: 1024px) { ... }
dengan min-widthnya bebas diatur(tidak berdasarkan 5 breakpoints itu saja) dan didalam kurung membuat style yang sesuai



# Sekian Terima Kasih 😊