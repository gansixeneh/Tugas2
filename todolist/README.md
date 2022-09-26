# Link Heroku App

http://tugas2-gansixeneh-2106629963.herokuapp.com/mywatchlist/todolist/

# Kegunaan {% csrf_token %} Pada Elemen \<form\>

Apabila tidak ada csrf_token pada elemen form, website-website yang tidak bertanggung jawab dapat memanfaatkan data-data yang dimiliki oleh seorang user yang sedang menggunakan website kita untuk melakukan pengisian form pada website kita dengan mengatasnamakan user tersebut. Dengan adanya ``csrf_token``, django akan memastikan bahwa orang yang sedang mengisi form kita benar-benar user tersebut, bukan orang/pihak lain.

# Membuat \<form\> secara manual

Ya, kita dapat membuat form sendiri secara manual tanpa generator. Tetapi, apabila data yang ingin kita minta ke user sudah disediakan oleh class yang ada di ``django``, kita dapat menggunakan class tersebut, misalnya ``UserCreationForm()``.

Untuk membuat form kita sendiri, kita perlu membuat class baru di ``models.py``. Setelah itu, kita perlu menyediakan variabel-variabel untuk menyimpan data yang diberikan di form. Lalu, pada ``views.py``, kita dapat membuat instance dari class tersebut, serta meminta data-data yang kita perlukan dengan melakukan ``request.POST.get(nama_data)`` dan menyimpannya pada variabel-variabel tersebut, lalu melakukan ``save()``. 

Untuk menampilkan ``request.POST`` yang telah kita buat di ``views.py`` pada HTML, kita hanya perlu menambahkan tulisan berikut pada HTML yang akan kita tampilkan:

```HTML
<input type="text" name="nama_data" class="form-control">
```

Kita juga dapat mengganti value attribute ``type`` menjadi ``"password"`` ketika user menulis di form tersebut, teks yang ditulis tidak akan ditampilkan.

# Proses Alur Data

Ketika user mensubmit data mereka melalui HTML form, ``views.py`` akan mengambil data tersebut dan melakukan ``save()``, sehingga data tersebut tersimpan di ``db.sqlite3``.

Apabila kita ingin menampilkan data yang sudah disimpan tadi, kita dapat mengakses data tersebut pada ``views.py``. Setelah itu, barulah kita dapat menampilkan data-data tersebut pada template HTML yang kita gunakan.

# Implementasi Checklist

Agar user dapat membuat task baru, kita akan menyediakan form ``create-task.html`` yang berisi tabel untuk menuliskan ``title`` dan ``description`` untuk task tersebut menggunakan tag input. Kita juga menyediakan tombol submit agar user dapat melakukan submit. Form tersebut dapat diakses menggunakan button yang tersedia di ``todolist.html``, yaitu:

```HTML
<button><a href="{% url 'todolist:create-task' %}">Tambah Task Baru</a></button>
```

Ketika user mengakses ``todolist/create-task``, maka ``views.py`` akan menampilkan HTML tersebut dan menyimpan data yang diberikan oleh user dengan melakukan ``request.POST.get('title')`` dan ``request.POST.get('description')``. Selain dari ``title`` dan ``description`` yang diberikan user, setiap task baru juga menyimpan ``user`` dan ``date``, tetapi kedua variabel ini diatur oleh ``views.py``, bukan user. Setelah semua data telah diperoleh, barulah kita dapat melakukan ``save()``.

Untuk menampilkan kembali task-task yang sudah disimpan, kita dapat mengakses data-data tersebut menggunakan ``Task.objects.filter(user=request.user)``. Di sini, kita menggunakan method ``filter()``, bukan ``all()``, karena seorang user tidak boleh melihat task-task yang dimiliki user lain. Lalu, kita akan menampilkan data-data tersebut melalui ``todolist.html``.