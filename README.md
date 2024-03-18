# Tucil1_13522148 - Cyberpunk 2077 Breach Protocol Solver
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
This program is a simple implementation in Python that constructs a quadratic Bézier curve using two algorithmic approaches: the divide and conquer midpoint algorithm and the brute force algorithm. The divide and conquer algorithm works by dividing the curve into line segments and breaking it down into smaller subproblems until the curve is considered smooth enough. On the other hand, the brute force algorithm directly computes the points on the Bézier curve without breaking it down into subproblems. This program prompts user input of N control points that determine the shape of the Bézier curve. Upon receiving input, the program constructs the Bézier curve using both implemented algorithms. Subsequently, the program displays the resulting Bézier curves from both algorithms to allow users to compare the outcomes of the two approaches. Thus, this program provides users with an opportunity to understand and compare the efficiency and accuracy of the two algorithms in constructing Bézier curves.

## Contributor
13522140 Yasmin Farisah Salma
13522148 Auralea Alvinia Syaikha

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
