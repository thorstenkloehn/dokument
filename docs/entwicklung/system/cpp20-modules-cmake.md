# Praxis-Guide: C++20 Modules & Modern CMake

C++20 Module ersetzen klassische `#include`-Header-Dateien durch echte kompilierte Modulschnittstellen, was Kompilierzeiten drastisch verkürzt und Makro-Verschmutzungen verhindert.

---

## 💻 1. C++20 Modul-Schnittstelle (`math.ixx` / `math.cppm`)

```cpp
export module math;

export namespace Math {
    export int add(int a, int b) {
        return a + b;
    }

    export int multiply(int a, int b) {
        return a * b;
    }
}
```

---

## 💻 2. Modul verwenden (`main.cpp`)

```cpp
import math;
import <iostream>;

int main() {
    std::cout << "Summe: " << Math::add(5, 7) << std::endl;
    return 0;
}
```

---

## ⚙️ 3. CMake Build Configuration (`CMakeLists.txt`)

```cmake
cmake_minimum_required(VERSION 3.28)
project(Cpp20ModulesDemo CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(app main.cpp)
target_sources(app PUBLIC FILE_SET CXX_MODULES FILES math.cppm)
```

---

## 🔗 Verwandte Themen
* [Rust, C & C++ Integration](rust-c-cpp-integration.md) – C/C++ & Rust
* [Compiler](compiler.md) – Compiler-Grundlagen
* [Linux-Systemprogrammierung](linux-systemprogrammierung.md) – Systemebene
