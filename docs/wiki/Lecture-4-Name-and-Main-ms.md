# Kuliah 4: __name__ dan __main__

[English](Lecture-4-Name-and-Main) · [Dansk](Lecture-4-Name-and-Main-da) · **Bahasa Malaysia**

![Kuliah 4: __name__ dan __main__](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-flask/raw/branch/main/docs/images/lecture-04.png)

## Apa yang dibincangkan dalam kuliah

`__name__` ialah pemboleh ubah terbina dalam yang menyimpan nama modul semasa. Apabila sesebuah fail dijalankan terus, Python menetapkannya kepada `"__main__"`; apabila fail itu diimport, ia menyimpan nama modul. Semakan `if __name__ == "__main__":` membolehkan sesebuah fail menentukan apa yang dijalankan hanya apabila ia ialah atur cara utama, contohnya `app.run()`. Ini memberi cara kedua untuk memulakan pelayan Flask, selain `flask run`, dan memudahkan memulakan serta menghentikan pelayan semasa pembangunan.

## Apa yang kita peroleh

- Peraturan bahawa kod berjalan dengan betul sama ada fail dijalankan atau diimport.
- Fungsi `main()` dalam `hello.py` yang hanya dipanggil di bawah semakan `__main__`, jadi mengimportnya tidak akan memulakan pelayan.
- Contoh yang telah diuji (`describe_name`) yang menerangkan kedua-dua kes dengan kata-kata.

## Dalam repositori ini

Kod: `src/flask_day_54/presentation/hello.py` (`main`) dan `src/flask_day_54/domain/name_demo.py`. Ujian: `tests/unit/test_name_demo.py` dan `tests/e2e/test_hello_main.py`.
