# 🔐 Password Strength Checker

A Python-based tool that evaluates the strength of a password and categorizes it into:

- **Very Strong**
- **Strong**
- **Moderate**
- **Weak**

This project helps users understand how secure their password is based on certain rules like length, variety of characters, and complexity.

---

## 🚀 Features
- Checks for:
  - ✅ Minimum length of password
  - ✅ Mix of uppercase & lowercase letters
  - ✅ Presence of digits
  - ✅ Use of special characters (`@, #, $, %, !`, etc.)
- Categorizes strength into **4 levels**.
- Simple **command-line interface (CLI)** — no extra setup required.
- Lightweight & fast — runs with built-in Python libraries only.

---

## 📦 Requirements

- **Python 3.6+**  
- No third-party libraries are required.  
- Uses only built-in modules like:
  - `re` → for pattern matching (regex).
  - `string` → for handling character sets (optional).  

### Optional Enhancements
If you want advanced scoring:
- Install **zxcvbn** (Dropbox’s password strength estimator):
  ```bash
  pip install zxcvbn
