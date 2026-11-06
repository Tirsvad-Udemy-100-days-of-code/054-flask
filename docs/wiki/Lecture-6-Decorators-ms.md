# Kuliah 6: Penghias (decorator) dan sintaks @

[English](Lecture-6-Decorators) · [Dansk](Lecture-6-Decorators-da) · **Bahasa Malaysia**

![Kuliah 6: Penghias (decorator) dan sintaks @](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/054-flask/raw/branch/main/docs/images/lecture-06.png)

## Apa yang dibincangkan dalam kuliah

Penghias (decorator) menambah tingkah laku pada fungsi sedia ada tanpa mengubah suai fungsi itu. Kuliah ini mula-mula mengulang kaji fungsi kelas pertama, fungsi bersarang dan pemulangan fungsi, kemudian memperkenalkan sintaks `@`: menulis `@make_bold` di atas sesebuah fungsi sama dengan `say_hello = make_bold(say_hello)`. Flask menggunakan idea yang sama untuk laluan (route)nya: `@app.route("/")`. Dengan `functools.wraps`, fungsi yang dibalut mengekalkan namanya.

## Apa yang kita peroleh

- Sintaks `@` sebagai jalan pintas untuk menghantar fungsi kepada pembalut.
- Penghias bertindan: yang paling hampir dengan fungsi dijalankan dahulu, maka `@make_bold @make_emphasis @make_underlined` menghasilkan `<b><em><u>...</u></em></b>`.
- Kefahaman tentang apa yang dilakukan oleh `@app.route("/")` dalam kuliah-kuliah seterusnya.

## Dalam repositori ini

Kod: `src/flask_day_54/domain/decorators.py`. Ujian: `tests/unit/test_decorators.py`.
