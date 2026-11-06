# Kuliah 5: Fungsi sebagai objek kelas pertama

[English](Lecture-5-First-Class-Functions) · [Dansk](Lecture-5-First-Class-Functions-da) · **Bahasa Malaysia**

![Kuliah 5: Fungsi sebagai objek kelas pertama](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-flask/raw/branch/main/docs/images/lecture-05.png)

## Apa yang dibincangkan dalam kuliah

Dalam Python, fungsi ialah objek seperti integer atau rentetan: ia boleh dihantar sebagai argumen, ditakrifkan di dalam fungsi lain dan dipulangkan daripadanya. Fungsi `calculate` menerima dua nombor dan satu fungsi lain (`add` atau `subtract`) lalu menggunakannya. Fungsi bersarang boleh dipanggil oleh fungsi induknya tetapi tidak dari luar. Sesebuah fungsi boleh memulangkan fungsi bersarang, dan pemanggil menyimpannya dalam pemboleh ubah serta memanggilnya kemudian. Alat Python Tutor menunjukkan langkah-langkahnya secara visual.

## Apa yang kita peroleh

- Idea di sebalik penghias (decorator): fungsi yang menerima fungsi dan memulangkan fungsi.
- Peraturan skop untuk fungsi bersarang, disahkan oleh ujian bahawa nama fungsi bersarang tidak boleh dicapai dari luar.
- Nama-nama dalam tugasan (`add`, `subtract`, `calculate`) dalam kod yang boleh dibaca dan dijalankan oleh peserta kursus yang lain.

## Dalam repositori ini

Kod: `src/flask_day_54/domain/first_class_functions.py`. Ujian: `tests/unit/test_first_class_functions.py`.
