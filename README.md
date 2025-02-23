# z3r0x - Multi-URL Checker

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

**z3r0x** is a lightweight Python-based tool designed to check the accessibility of multiple URLs. It verifies whether a given list of URLs is accessible or broken and provides a clear output with visual indicators (✅ for accessible, ❌ for broken). It’s perfect for developers, system administrators, and anyone who needs to monitor the status of multiple websites or endpoints.

---

## Features

- **Multi-URL Support**: Check the accessibility of multiple URLs in one go.
- **Visual Indicators**: Green tick (✅) for accessible URLs and red cross (❌) for broken URLs.
- **Simple and Lightweight**: Easy to use with minimal dependencies.
- **Customizable**: Add or remove URLs from the list as needed.
- **Fast and Efficient**: Uses Python's `requests` library for quick HTTP requests.

---

## Installation

### Prerequisites

- Python 3.6 or higher.
- `requests` library (installed automatically if not present).

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/z3r0x.git
   cd z3r0x
   ```

2. Install the required dependencies:
   ```bash
   pip install requests
   ```

3. Run the script:
   ```bash
   python z3r0x.py
   ```

---

## Usage

1. Add the URLs you want to check in the `site_urls` list inside the `z3r0x.py` file:
   ```python
   site_urls = [
       "https://www.google.com",
       "https://www.example.com",
       "https://www.nonexistentwebsite123.com",
       "https://www.github.com"
   ]
   ```

2. Run the script:
   ```bash
   python z3r0x.py
   ```

3. View the output:
   ```
   OK https://www.google.com ✅
   OK https://www.example.com ✅
   BROKEN https://www.nonexistentwebsite123.com ❌
   OK https://www.github.com ✅
   ```

---

## Example

Here’s an example of how to use **z3r0x**:

```python
# z3r0x.py

import requests

def check_site_accessibility(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"OK {url} ✅")
        else:
            print(f"BROKEN {url} ❌")
    except requests.RequestException:
        print(f"BROKEN {url} ❌")

# List of URLs to check
site_urls = [
    "https://www.google.com",
    "https://www.example.com",
    "https://www.nonexistentwebsite123.com",
    "https://www.github.com"
]

# Check accessibility of each URL
for url in site_urls:
    check_site_accessibility(url)
```

---

## Contributing

Contributions are welcome! If you’d like to contribute to **z3r0x**, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes.
4. Push your branch and submit a pull request.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Support

If you encounter any issues or have questions, feel free to open an issue on the [GitHub repository](https://github.com/your-username/z3r0x/issues).

---

## Author

**z3r0x** is developed and maintained by [Your Name](https://github.com/your-username).

---

## Acknowledgments

- Thanks to the Python community for creating amazing tools and libraries.
- Special thanks to the `requests` library for making HTTP requests simple and efficient.

---

Enjoy using **z3r0x**! 🚀
