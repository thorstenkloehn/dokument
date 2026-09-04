# Praxis-Guide: Rust & Python Bindings mit PyO3

Verbinde die Ausführungsgeschwindigkeit von Rust mit der Flexibilität von Python. Mit **PyO3** und **maturin** erstellst du native Python-C-Extensions in Rust.

---

## 🛠️ 1. Setup & Werkzeuge

```bash
# Rust Toolchain installieren (falls noch nicht vorhanden)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Maturin Build-Tool in Python venv installieren
pip install maturin
```

---

## 🦀 2. Rust-Projekt erstellen

```bash
mkdir my_fast_module && cd my_fast_module
maturin init --bindings pyo3
```

### `Cargo.toml`
```toml
[package]
name = "my_fast_module"
version = "0.1.0"
edition = "2021"

[lib]
name = "my_fast_module"
crate-type = ["cdylib"]

[dependencies]
pyo3 = { version = "0.20", features = ["extension-module"] }
```

### `src/lib.rs` (High-Performance Rust-Code)
```rust
use pyo3::prelude::*;

/// Berechnet die Summe von Quadraten in Rust
#[pyfunction]
fn sum_of_squares(numbers: Vec<i64>) -> PyResult<i64> {
    Ok(numbers.iter().map(|&x| x * x).sum())
}

#[pymodule]
fn my_fast_module(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(sum_of_squares, m)?)?;
    Ok(())
}
```

---

## ⚡ 3. Bauen & In Python nutzen

```bash
# Entwicklungs-Build im Python venv installieren
maturin develop --release
```

### Python-Testskript (`test.py`)
```python
import time
import my_fast_module

data = list(range(10_000_000))

start = time.time()
result = my_fast_module.sum_of_squares(data)
end = time.time()

print(f"Ergebnis: {result}")
print(f"Rust Zeit: {end - start:.4f} Sekunden")
```

---

## 🔗 Verwandte Themen
* [Rust, C & C++ Integration](rust-c-cpp-integration.md) – Systemprogrammierung
* [Compiler](compiler.md) – Compiler-Grundlagen
* [Linux-Systemprogrammierung](linux-systemprogrammierung.md) – Native Performance
