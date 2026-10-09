# My Calculator (`my_calculator`)

Proyek ini adalah contoh pembuatan **Python Package** modern menggunakan standar PEP 517/518/621 (`pyproject.toml`) dan struktur `src-layout`, yang didistribusikan langsung melalui **Git Repository** (GitHub) tanpa perlu dipublikasikan ke PyPI.

Implementasi dan pengujian penggunaan package ini terdapat pada direktori \[`examplepackagetest`\].

---

## Daftar Isi

1. [Arsitektur & Struktur Proyek](#arsitektur--struktur-proyek)
2. [Penjelasan Teknis Komponen Package](#penjelasan-teknis-komponen-package)
3. [Mekanisme Distribusi via Git](#mekanisme-distribusi-via-git)
4. [Cara Implementasi (Direktori ](#cara-implementasi-direktori-examplepackagetest)`examplepackagetest`[)](#cara-implementasi-direktori-examplepackagetest)
5. [Contoh Kode & Output](#contoh-kode--output)
6. [Pengembangan Lokal (Development Workflow)](#pengembangan-lokal-development-workflow)

---

## Arsitektur & Struktur Proyek

Struktur repositori dan proyek pengujian diatur sebagai berikut:

```text
pythonpackage/
│
├── my-calculator/                      # Repositori Git Package Python
│   ├── .git/                           # Git Version Control
│   ├── pyproject.toml                  # Konfigurasi build & metadata package (PEP 621)
│   ├── README.md                       # Dokumentasi teknis package
│   └── src/                            # Source code directory (src-layout)
│       └── my_calculator/              # Package utama
│           ├── __init__.py             # Entry point package (expose public API)
│           └── core.py                 # Implementasi fungsi matematika
│
└── examplepackagetest/                 # Direktori aplikasi konsumen / implementasi
    ├── requirements.txt                # Dependensi proyek (merujuk ke repo Git)
    └── main.py                         # Skrip pengujian & demonstrasi package
```

### Mengapa Menggunakan `src-layout`?

Struktur `src/my_calculator/` direkomendasikan oleh [PyPA (Python Packaging Authority)](https://packaging.python.org/) karena:

- **Mencegah Import Parity Bug**: Menghindari Python mengimpor modul langsung dari direktori kerja lokal saat menjalankan unit test, sehingga memastikan bahwa modul yang diuji adalah package yang benar-benar telah diinstal.
- **Isolasi Berkas**: Memisahkan kode sumber aplikasi dari file pendukung seperti konfigurasi tooling, test runner, dan dokumentasi.

---

## Penjelasan Teknis Komponen Package

### 1. Konfigurasi Build: \[`pyproject.toml`\]

File ini menggantikan `setup.py` dan `setup.cfg` tradisional, mengikuti spesifikasi modern Python:

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "my_calculator"
version = "1.0.0"
description = "Modul kalkulator sederhana untuk example repositori"
readme = "README.md"
requires-python = ">=3.8"
authors = [
    { name = "Alfin", email = "halovinaofficial@gmail.com" }
]

[tool.setuptools.packages.find]
where = ["src"]
```

- `build-system`: Menentukan tools yang bertugas membangun package (`setuptools`).
- `project`: Berisi metadata inti seperti nama package, versi, deskripsi, versi Python minimal, serta author.
- `tool.setuptools.packages.find`: Menginstruksikan `setuptools` untuk mencari modul Python di dalam folder `src/`.

### 2. Logika Inti: \[`core.py`\]

Menyediakan operasi aritmatika dasar dengan type hinting dan penanganan error:

- `add(a, b)`: Menjumlahkan dua bilangan.
- `subtract(a, b)`: Mengurangkan dua bilangan.
- `multiply(a, b)`: Mengalikan dua bilangan.
- `divide(a, b)`: Membagi dua bilangan, dengan validasi `ValueError("Tidak dapat membagi dengan nol.")` jika pembagi bernilai `0`.

### 3. Expose Public API: \[`__init__.py`\]

```python
from .core import add, subtract, multiply, divide
```

Dengan mengimpor fungsi-fungsi dari `.core` ke `__init__.py`, pengguna dapat langsung memanggil:

```python
import my_calculator
my_calculator.add(5, 3)
```

tanpa harus mengakses modul internal seperti `my_calculator.core.add(5, 3)`.

---

## Mekanisme Distribusi via Git

Package ini didistribusikan langsung dari repository GitHub tanpa perlu di-upload ke PyPI. `pip` mendukung instalasi langsung dari protokol VCS (Version Control System).

Sintaks URL Git untuk `pip`:

```text
git+https://github.com/<username>/<repository-name>[@<commit_or_tag_or_branch>]
```

Contoh variasi instalasi:

- **Default (branch utama)**:

  ```bash
  pip install git+https://github.com/halovina/my-calculator
  ```

- **Berdasarkan Tag / Rilis Versi Spesifik**:

  ```bash
  pip install git+https://github.com/halovina/my-calculator@v1.0.0
  ```

- **Berdasarkan Branch Tertentu**:

  ```bash
  pip install git+https://github.com/halovina/my-calculator@main
  ```

- **Berdasarkan Commit Hash**:

  ```bash
  pip install git+https://github.com/halovina/my-calculator@a1b2c3d
  ```

---

## Cara Implementasi (Direktori `examplepackagetest`)

Direktori \[`examplepackagetest`\]bertindak sebagai proyek klien yang mengonsumsi package `my_calculator`.

### 1. Menentukan Dependensi (\[`requirements.txt`\]

Isi berkas `requirements.txt`:

```text
git+https://github.com/halovina/my-calculator
```

### 2. Instalasi Dependensi

Jalankan perintah berikut di terminal (disarankan dalam virtual environment aktif):

```bash
cd examplepackagetest
pip install -r requirements.txt
```

> `pip` akan meng-clone repository secara otomatis, membaca `pyproject.toml`, dan mengompilasi package ke dalam environment Python lokal.

### 3. Menjalankan Kode (\[`main.py`\]

File `main.py` menguji operasi penambahan, pembagian normal, dan penanganan error pembagian dengan nol:

```python
# main.py
import my_calculator

try:
    # Menggunakan fungsi penjumlahan
    hasil_tambah = my_calculator.add(10, 5)
    print(f"Hasil 10 + 5 = {hasil_tambah}")

    # Menggunakan fungsi pembagian
    hasil_bagi = my_calculator.divide(20, 4)
    print(f"Hasil 20 / 4 = {hasil_bagi}")
    
    # Uji coba pembagian dengan nol
    my_calculator.divide(10, 0)

except ValueError as e:
    print(f"Error terdeteksi: {e}")
```

Eksekusi file:

```bash
python main.py
```

---

## Contoh Kode & Output

Hasil keluaran di terminal saat `main.py` dijalankan:

```text
Hasil 10 + 5 = 15
Hasil 20 / 4 = 5.0
Error terdeteksi: Tidak dapat membagi dengan nol.
```

---

## Pengembangan Lokal (Development Workflow)

Jika Anda ingin mengembangkan atau mengubah kode di `my-calculator` secara lokal dan langsung melihat dampaknya di `examplepackagetest` tanpa harus commit & push setiap kali ke GitHub:

1. **Gunakan Mode Editable (**`-e`**)**:

   ```bash
   pip install -e /path/to/my-calculator
   ```

   Atau dari direktori `examplepackagetest`:

   ```bash
   pip install -e ../my-calculator
   ```

2. **Alur Update Package ke Git**: Setelah selesai melakukan perubahan lokal:

   ```bash
   cd my-calculator
   git add .
   git commit -m "feat: tambah fitur baru"
   git push origin main
   ```

3. **Update di Proyek Klien**: Untuk memperbarui package yang sudah diinstal via git ke versi terbaru dari remote:

   ```bash
   pip install --upgrade --force-reinstall git+https://github.com/halovina/my-calculator
   ```