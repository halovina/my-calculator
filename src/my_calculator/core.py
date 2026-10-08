def add(a: float, b: float) -> float:
    """Menjumlahkan dua angka."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Mengurangi dua angka."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Mengalikan dua angka."""
    return a * b

def divide(a: float, b: float) -> float:
    """Membagi dua angka. Mengembalikan ValueError jika dibagi nol."""
    if b == 0:
        raise ValueError("Tidak dapat membagi dengan nol.")
    return a / b
