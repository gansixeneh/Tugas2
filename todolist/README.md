# Perbedaan Inline, Internal, dan External CSS

- Inline CSS: Menambahkan style sebagai atribut suatu elemen di HTML
- Internal CSS: Menambahkan style pada elemen <style> yang ada di bagian head.
- External CSS: Menambahkan style pada file CSS yang ada di luar HTML

Inline CSS adalah yang paling spesifik, sedangkan External CSS yang paling umum. Untuk style yang bersifat umum, yaitu External CSS, kita dapat menggunakan 1 file untuk keseluruhan atau sebagian besar website, tetapi sangat sulit untuk membuat style spesifik untuk suatu element/halaman. Sebaliknya, untuk Inline CSS, akan sangat mudah membuat style yang spesifik, tetapi apabila banyak element membutuhkan style yang sama, penggunaan Inline CSS tidak praktis karena harus menulis style yang sama pada banyak elemen.

# Tag HTML5

- <nav>: Navigasi link website
- <header>: Header suatu bagian dari suatu halaman
- <footer>: Footer suatu bagian dari suatu halaman
- <embed>: Untuk memasukkan file dari web/aplikasi lain ke HTML, biasanya video/audio
- <audio>: Audio/suara dalam HTML

# Tipe-tipe CSS Selector

- .class: Memilih semua elemen dengan nama class tertentu
- .class1.class2: Memilih semua elemen yang memiliki kedua nama class yang sudah dituliskan sebelumnya
- #id: Memilih semua elemen dengan id tertentu
- *: Memilih semua elemen
- element: Memilih semua elemen dengan nama tertentu

# Implementasi Checklist

- Memasukkan file CSS dan JS yang diperlukan ke dalam folder ``static/`` dan meng-import file-file tersebut pada ``base.html``
- Menggunakan card untuk form yang ada di setiap halaman dan setiap task di todolist
- Menentukan style width, top, dan left agar posisi card-card tersebut sesuai
- Memberikan navbar pada halaman todolist yang berisi button-button yang sudah ada sebelumnya
- Memperindah button-button yang ada menggunakan class ``btn``
- Memberikan warna untuk setiap elemen agar lebih menarik
- Memberikan class ``fw-bold`` untuk teks-teks yang ingin dijadikan bold
- Boostrap otomatis membuat halaman-halaman yang ada menjadi responsive, sehingga tidak perlu lagi dilakukan perubahan