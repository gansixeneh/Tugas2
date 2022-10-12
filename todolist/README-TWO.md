# Perbedaan Synchronous dan Asynchronous Programming

- Synchronous: Urutan operasi-operasi yang dijalankan harus terurut. Operasi selanjutnya belum dapat dijalankan jika operasi sedang dijalankan belum selesai.

- Asynchronous: Urutan operasi-operasi yang dijalankan tidak harus terurut, sehingga banyak operasi dapat berjalan sekaligus. Ini sangat menghemat waktu karena satu operasi tidak perlu menunggu operasi lain.

# Event-Driven Programming

Dalam paradigma Event-Driven Programming, jalannya program ditentukan oleh aksi yang dilakukan user, seperti melakukan klik atau menekan keyboard.

Pada tugas ini, contoh penerapannya adalah ketika user menekan tombol `Submit` pada modal yang dibuat, barulah program yang melakukan penambahan dan refresh pada todolist dijalankan.

# Penerapan Asynchronous Programming pada AJAX

Pada AJAX, ketika user mengirim atau meminta data dari server, user dapat tetap membuka halaman web sambil menunggu respon server, tidak perlu menunggu operasi yang sedang dijalankan server.

# Implementasi Checklist

- AJAX GET: Setelah membuat fungsi baru pada `views.py` dan path baru `/todolist/json`, kita perlu membuat fungsi yang `fetch` yang mengambil data json tersebut bila diperlukan.

- AJAX POST: Selain membuat view dan path, kita perlu membuat modal yang berisi form untuk menambahkan task baru. Modal ini akan dipanggil ketika user menekan tombol `Add Task`. Setelah itu, kita perlu membuat fungsi yang dijalankan ketika user menekan tombol `Submit` dengan menambahkan `onclick` pada script. Fungsi tersebut akan melakukan `fetch` pada `/todolist/add` dan melakukan refresh secara asinkronus menggunakan fungsi AJAX GET yang sudah dibuat sebelumnya.