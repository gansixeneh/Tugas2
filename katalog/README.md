# Link Heroku App

http://tugas2-gansixeneh-2106629963.herokuapp.com/katalog/

# Penjelasan Request Client

![Bagan MVT](https://drive.google.com/file/d/1P39K85siMCp_wO9gY-2Toql1UXIH4kCD/view?usp=sharing)

Ketika client melakukan request, ``urls.py`` akan memanggil ``views.py`` yang sesuai dengan permintaan user. Jika memerlukan data yang ada pada database, ``views.py`` akan memanggil ``models.py`` untuk memberikan data yang sesuai. Ketika data sudah diperoleh, ``views.py`` akan memberikan berkas ``html`` kepada user yang sudah berisi data-data yang diperlukan.

# Alasan Menggunakan Virtual Environment

Ketika banyak orang mengerjakan suatu project yang sama, mereka memerlukan framework-framework dengan versi yang sama agar project mereka tetap konsisten. Masalahnya, jika satu orang mengerjakan banyak project yang memerlukan suatu framework yang sama, tetapi dengan versi yang berbeda-beda, dia harus meng-install ulang framework tersebut setiap kali berpindah project. Virtual Environment menjadi solusi bagi kita agar kita tidak perlu meng-install ulang framework yang ada, karena kita bisa menyimpan versi yang berbeda untuk project yang berbeda.

# Implementasi Poin 1-4

## Poin 1

Pertama-tama, ``views.py`` yang ada di app ``katalog`` perlu meng-import Class ``CatalogItem`` yang ada di ``models.py`` app ``katalog``. Kita akan menyimpan data yang kita ambil dalam ``list_barang`` dan menyimpan nama kita dalam ``nama`` untuk nanti ditampilkan di HTML menggunakan template ``base.html``.

## Poin 2

Untuk memanggil fungsi yang ada di ``views.py``, kita menggunakan ``urls.py`` di app ``katalog``. Setelah itu, kita juga akan menambahkan path di ``urls.py`` di ``project_django`` agar dapat memanggil ``urls.py`` di app ``katalog``.

## Poin 3

Kita akan menampilkan ``nama`` dan ``list_barang`` yang sudah kita peroleh di Poin 1. Pada ``base.html``, kita hanya perlu menuliskan ``{{nama}}`` dan menampilkan data-data yang ada di ``list_barang`` pada suatu tabel dengan melakukan for loop yang menampilkan semua barang yang ada di ``list_barang`` tersebut.

## Poin 4

Seperti yang sudah pernah dilakukan sebelumnya, kita perlu menyediakan app Heroku yang akan digunakan melalui https://dashboard.heroku.com/apps. Setelah itu, kita akan menghubungkan app yang sudah kita buat dengan repo GitHub kita dengan cara menambahkan ``Action secrets`` di repo GitHub kita. Kita perlu menambahkan ``HEROKU_APP_NAME``, yaitu nama app Heroku kita dan ``HEROKU_API_KEY``, yaitu API Key yang dimiliki akun Heroku kita. Setelah itu, kita dapat me-refresh proses deployment yang ada di GitHub kita. Sekarang, aplikasi yang kita buat sudah ter-deploy.