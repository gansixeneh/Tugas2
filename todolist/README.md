# Link Heroku App

http://tugas2-gansixeneh-2106629963.herokuapp.com/todolist/

# Kegunaan {% csrf_token %} Pada Elemen \<form\>

Apabila tidak ada csrf_token pada elemen form, website-website yang tidak bertanggung jawab dapat memanfaatkan data-data yang dimiliki oleh seorang user yang sedang menggunakan website kita untuk melakukan pengisian form pada website kita dengan mengatasnamakan user tersebut. Dengan adanya ``csrf_token``, Django akan memastikan bahwa orang yang sedang mengisi form kita benar-benar user tersebut, bukan orang/pihak lain.

# Membuat \<form\> secara manual

Ya, kita dapat membuat form sendiri secara manual tanpa generator. Tetapi, apabila data yang ingin kita minta ke user sudah disediakan oleh class yang ada di Django, kita dapat menggunakan class tersebut, misalnya ``UserCreationForm()``.

Untuk membuat form kita sendiri, kita perlu membuat class baru di ``models.py``. Setelah itu, kita perlu menyediakan variabel-variabel untuk menyimpan data yang diberikan di form. Lalu, pada ``views.py``, kita dapat membuat instance dari class tersebut, serta meminta data-data yang kita perlukan dengan melakukan ``request.POST.get(nama_data)`` dan menyimpannya pada variabel-variabel tersebut, lalu melakukan ``save()``. 

Untuk menampilkan ``request.POST`` yang telah kita buat di ``views.py`` pada HTML, kita hanya perlu menambahkan kode berikut pada HTML yang akan kita tampilkan:

```HTML
<input type="text" name="nama_data" class="form-control">
```

Kita juga dapat mengganti value attribute ``type`` menjadi ``"password"`` ketika user menulis di form tersebut agar teks yang ditulis tidak akan ditampilkan.

# Proses Alur Data

Ketika user mensubmit data mereka melalui HTML form, ``views.py`` akan mengambil data tersebut dan melakukan ``save()``, sehingga data tersebut tersimpan di ``db.sqlite3``.

Apabila kita ingin menampilkan data yang sudah disimpan tadi, kita dapat mengakses data tersebut pada ``views.py``. Setelah itu, barulah kita dapat menampilkan data-data tersebut pada template HTML yang kita gunakan.

# Implementasi Checklist

Pertama-tama, kita perlu membuat app ``todolist`` dan mendaftarkannya di ``settings.py``. Setelah itu, kita perlu mengubah ``urls.py`` yang ada di ``project_django`` dan ``todolist`` agar dapat mengakses ``http://localhost:8000/todolist``. Kita juga perlu membuat class baru di ``models.py`` yang ada di app ``todolist`` yang bernama ``Task`` yang berisi atribut ``user``, ``date``, ``title``, dan ``description``. Setiap atribut memiliki jenis field masing-masing, dan untuk atribut ``user`` menggunakan ``models.ForeignKey``.

Untuk membuat form registrasi, kita akan menggunakan model ``UserCreationForm()`` yang sudah disediakan oleh Django dan menyimpan form tersebut dalam context untuk ditampilkan pada ``register.html`` dengan cara menuliskan ``{{ form.as_table }}`` pada HTML tersebut dalam bentuk tabel. Agar user bisa melakukan submit, kita perlu membuat tombol submit dengan menuliskan:
```HTML
<input type="submit" name="submit" value="Daftar"/>
```
Apabila registrasi berhasil, kita akan menyimpan data yang sudah dikirim user dengan melakukan ``form.save()`` dan mengirim message ``"Akun telah berhasil dibuat!"``.

Cara mengirimkan message tersebut adalah dengan menggunakan ``messages.success(request, 'Akun telah berhasil dibuat!')`` dan menuliskan kode berikut pada HTML yang kita gunakan:
```HTML
{% if messages %}
    <ul>
        {% for message in messages %}
            <li>{{ message }}</li>
        {% endfor %}
    </ul>
{% endif %}
```
Kode ini juga akan kita sertakan pada setiap HTML yang akan kita gunakan untuk menampilkan beragam message yang dapat muncul.

Untuk form login, sebenarnya mirip dengan form register, tetapi kita membuat form kita sendiri secara manual. Kita akan meminta username dan password user dengan ``request.POST.get('username')`` dan ``request.POST.get('password')``. Setelah menerima username dan password, kita akan menggunakan fungsi ``authenticate()`` untuk memastikan apakah data yang diberikan valid. Jika data valid, maka user akan login dan kita akan mengarahkan user ke path ``/todolist/`` dengan me-return response ``redirect('todolist:show_todolist')``. Sedangkan jika data salah, kita akan mengirim message untuk memberi tahu user, yaitu dengan ``messages.info(request, 'Username atau Password salah!')``.

Untuk form logout, kita hanya perlu memanggil fungsi ``logout()``, mengembalikan user ke halaman login, dan membersihkan cookie.

Pada halaman utama ``todolist``, kita dapat mengatur ``views.py`` untuk mengambil username dan daftar-daftar task yang ada. Data username diperoleh dari ``request.user``, sedangkan task diperoleh dari ``Task.objects.filter(user=request.user)`` agar seorang user tidak dapat melihat task user lain. Kita juga perlu membuat link yang menuju ke link logout dan link form untuk menambah task baru, yaitu dengan menggunakan:

```HTML
<button><a href="{% url 'todolist:create-task' %}">Tambah Task Baru</a></button>
<button><a href="{% url 'todolist:logout' %}">Logout</a></button>
```

Agar user dapat membuat task baru, kita akan membuat fungsi ``create_task`` pada ``views.py`` yang akan dipanggil ketika user mengakses link ``{% url 'todolist:create-task' %}``. Fungsi tersebut akan menampilkan ``create-task.html`` dan meminta ``title`` dan ``description`` dari task yang baru dengan melakukan ``request.POST.get('title')`` dan ``request.POST.get('description')``. Selain dari ``title`` dan ``description`` yang diberikan user, setiap task baru juga menyimpan ``user`` dan ``date``, tetapi kedua variabel ini diatur di dalam fungsi, bukan oleh user. Setelah semua data telah diperoleh, barulah kita dapat melakukan ``save()``. Setelah itu, data akan tersimpan di dalam database.

Lalu, kita perlu mengubah ``urls.py`` untuk dapat mengakses fungsi-fungsi ``views.py`` yang sudah kita buat sebelumnya. Setelah kita melakukan push ke GitHub, maka otomatis website baru kita akan ter-deploy, karena kita sudah pernah melakukan deploy menggunakan repo yang sama. Setelah website ter-deploy, kita dapat membuat akun dan dummy data layaknya seorang user biasa.