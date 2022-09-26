# Link Heroku App

http://tugas2-gansixeneh-2106629963.herokuapp.com/mywatchlist/todolist/

# Kegunaan {% csrf_token %} Pada Elemen \<form\>

Apabila tidak ada csrf_token pada elemen form, website-website yang tidak bertanggung jawab dapat memanfaatkan data-data yang dimiliki oleh seorang user yang sedang menggunakan website kita untuk melakukan pengisian form pada website kita dengan mengatasnamakan user tersebut. Dengan adanya ``csrf_token``, django akan memastikan bahwa orang yang sedang mengisi form kita benar-benar user tersebut, bukan orang/pihak lain.

# Membuat \<form\> secara manual

Ya, kita dapat membuat form sendiri secara manual tanpa generator. Tetapi, apabila data yang ingin kita minta ke user sudah disediakan oleh class yang ada di ``django``, kita dapat menggunakan class tersebut, misalnya ``UserCreationForm()``.

Untuk membuat form kita sendiri, kita perlu membuat class baru di ``models.py``. Setelah itu, kita perlu menyediakan variabel-variabel untuk menyimpan data yang diberikan di form. Lalu, pada ``views.py``, kita dapat meminta data-data yang kita perlukan dengan melakukan ``request.POST.get(nama_data)``. 

Untuk menampilkan ``request.POST`` yang telah kita buat di ``views.py`` pada HTML, kita hanya perlu menambahkan tulisan berikut pada HTML yang akan kita tampilkan:

```HTML
<input type="text" name="nama_data" placeholder="Username" class="form-control">
```

Kita juga dapat mengganti value attribute ``type`` menjadi ``"password"`` ketika user menulis di form tersebut, teks yang ditulis tidak akan ditampilkan.