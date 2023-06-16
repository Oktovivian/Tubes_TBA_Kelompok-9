# Tubes_TBA_Kelompok-9

## 1. Rancangan CFG
![image](https://github.com/Oktovivian/Tubes_TBA_Kelompok-9/assets/68942070/d5eb8013-6b00-408e-8145-d29b572b0b63)

## 2. Rancangan Finite Auotama
* FA untuk for
![image](https://github.com/Oktovivian/Tubes_TBA_Kelompok-9/assets/68942070/2cafef72-e961-4dee-9487-64066ab0d571)

* FA untuk aksi (berupa increment dan assignment
![image](https://github.com/Oktovivian/Tubes_TBA_Kelompok-9/assets/68942070/20c2c9cc-63de-48f1-87c9-0672e08a4621)

* FA untuk comparison (>,>=, <,<=
![image](https://github.com/Oktovivian/Tubes_TBA_Kelompok-9/assets/68942070/c45f958b-a4b2-4d93-8261-fcb82f49dcaa)

* FA untuk kurung kurawal awal
![image](https://github.com/Oktovivian/Tubes_TBA_Kelompok-9/assets/68942070/9a311f18-fef7-4ec7-95e0-546212d1db8e)

* FA untuk kurung kurawal akhir
![image](https://github.com/Oktovivian/Tubes_TBA_Kelompok-9/assets/68942070/b7b784da-bff0-45bb-9c4d-d81173a3f155)

## 3. Parse Table dan LEXICAL ANALYZER
![image](https://github.com/Oktovivian/Tubes_TBA_Kelompok-9/assets/68942070/82e46b44-46dc-42b7-ab21-cd3f7499db6f)
![image](https://github.com/Oktovivian/Tubes_TBA_Kelompok-9/assets/68942070/58ec6bac-02f8-42bd-a6e6-dd1ecc0a486f)
![image](https://github.com/Oktovivian/Tubes_TBA_Kelompok-9/assets/68942070/3be1e0a7-72cb-4bda-a814-dd3c07e840bb)


## 4. Panduan Penggunaan Program

* Program hanya dapat menerima input dalam bentuk jenis string.
* Program hanya dapat menerima aturan `statement -> for <kondisi> { <aksi> }`.
* Pada <kondisi> hanya dapat membandingkan variabel a | b dengan operasi perbandingan `<, <=, >, >=`.
* Program dapat menerima <aksi> lebih dari satu dengan penulisan `{ <aksi> ; <aksi> ; … }`.
* Pada <aksi> dapat menerima `<var><assignment><aritmatika> | <var><increment>` (tidak bisa memiliki aksi kosong).
* Pada <aritmatika> hanya dapat menerima `<angka> | <variabel> | <aritmatika> + <aritmatika>`.
* Pada <assignment> hanya dapat menerima `= | :=`.
* Pada <increment> hanya dapat menerima `++ | –`.
* Program hanya dapat menerima input perulangan while - do sebanyak satu kali (tidak dapat menerima input nested loop).
* Program hanya dapat menerima input dengan memasukkan input ke dalam file `test.txt`.
* Program dapat menyatakan input valid jika contoh input sebagai berikut : 
for a<b { 
    a++
}

for a>b { 
    a++ ; b:=1
}

for a>=b { 
    a=a+2+3 ; a--
}

for b<=a { 
    a=b 
}
* Program akan mengeluarkan error jika input tidak memenuhi `for <kondisi> { <aksi> }` dengan penggunaan spasi yang benar.
* Program akan mengeluarkan error jika tidak menggunakan terminal yang tersedia.
* Program akan dinyatakan valid jika memenuhi semua kriteria yang tersedia pada panduan.

## 5. Link Docs
https://docs.google.com/document/d/1ZN51UWHL95ZcP5k75WJIQ1uZyn3C0osanOq6Dtb0XJ0/edit?usp=sharing
