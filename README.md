# Tucil2_13522140_13522148 - Membangun Kurva Bézier dengan Algoritma Titik Tengah berbasis Divide and Conquer
This repository is an archive of files for Tugas Kecil 2 IF2211 Strategi Algoritma.

## Table of Contents
  - [Table of Contents](#table-of-contents)
  - [General Information](#general-information)
  - [Contributor](#contributor)
  - [Technologies Used](#technologies-used)
  - [Structure](#structure)
  - [How to Use](#how-to-use)
    - [Installation](#installation)
    - [Program Execution](#program-execution)

## General Information
Program ini adalah sebuah implementasi sederhana dalam bahasa Python yang membangun sebuah kurva Bézier kuadratik menggunakan dua pendekatan algoritma: algoritma titik tengah berbasis divide and conquer dan algoritma brute force. Algoritma divide and conquer bekerja dengan membagi kurva menjadi segmen-segmen garis dan memecahnya menjadi submasalah yang lebih kecil hingga kurva dianggap cukup halus. Di sisi lain, algoritma brute force secara langsung menghitung titik-titik pada kurva Bézier tanpa membaginya menjadi submasalah. Program ini meminta input dari pengguna berupa N titik kontrol yang menentukan bentuk kurva Bézier. Setelah menerima input, program akan membangun kurva Bézier menggunakan kedua algoritma yang diimplementasikan. Selanjutnya, program akan menampilkan kurva Bézier hasil dari kedua algoritma tersebut untuk memungkinkan pengguna membandingkan hasil dari kedua pendekatan. Dengan demikian, program ini memberikan kesempatan bagi pengguna untuk memahami dan membandingkan efisiensi serta akurasi kedua algoritma dalam pembentukan kurva Bézier.

<p align = "center">
  <img width = "250" src="https://i.stack.imgur.com/QOZ6J.png">
</p>

## Contributor
- 13522140 Yasmin Farisah Salma
- 13522148 Auralea Alvinia Syaikha

## Technologies Used
- Python
- Matplotlib

## Structure

```
├── bin
│   └── bin.txt
│
├── doc
│   └── Tucil2_13522140_13522148.pdf
│
├── src
│   ├── main.py
│   ├── divide_and_conquer.py
│   └── bruteforce.py
│ 
└── test
    ├── test1.txt
    ├── test2.txt
    ├── test3.txt
    ├── test4.txt
    ├── test5.txt
    └── test6.txt
    
```

---

## How to Use

### Installation
- Download and install [Python](https://www.python.org/downloads/)
- Download all folder and files on this repository or simply clone this repo!

### Program Execution
    git clone https://github.com/caernations/Tucil2_13522140_13522148
    cd Tucil2_13522140_13522148
    cd src
    pip install matplotlib
    python main.py
