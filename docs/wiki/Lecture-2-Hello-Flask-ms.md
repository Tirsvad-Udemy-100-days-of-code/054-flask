# Kuliah 2: Pelayan Flask yang pertama

[English](Lecture-2-Hello-Flask) · [Dansk](Lecture-2-Hello-Flask-da) · **Bahasa Malaysia**

![Kuliah 2: Pelayan Flask yang pertama](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-flask/raw/branch/main/docs/images/lecture-02.png)

## Apa yang dibincangkan dalam kuliah

Sebuah pustaka dipanggil oleh kod anda, tetapi sebuah rangka kerja (framework) memanggil kod anda dan menentukan strukturnya. Kuliah ini mencipta aplikasi Flask yang paling kecil dalam fail bernama `hello.py` (jangan sekali-kali `flask.py`, kerana ia akan menyembunyikan pustaka itu), memasang Flask dengan `pip`, menunjukkan fail itu melalui `FLASK_APP` dan memulakan pelayan dengan `flask run`. Pelayar kemudian memaparkan "Hello, World!" daripada alamat setempat. `Ctrl+C` menghentikan pelayan supaya dua aplikasi tidak berebut port yang sama.

## Apa yang kita peroleh

- Perbezaan antara pustaka dan rangka kerja.
- Pelayan web yang berfungsi dalam enam baris: `app = Flask(__name__)`, satu laluan (route) untuk `/` dan satu fungsi yang memulangkan teks.
- Cara `FLASK_APP` memberitahu Flask fail mana yang hendak dijalankan.
- Tabiat menguji laluan dengan klien ujian Flask dan bukannya pelayar.

## Dalam repositori ini

Kod: `src/flask_day_54/presentation/hello.py` (laluan `hello_world`), kes guna `application/get_greeting.py` dan pemalar `GREETING`. Ujian: `tests/e2e/test_hello_app.py`.
