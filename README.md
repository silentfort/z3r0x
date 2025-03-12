z3r0x - Multi-URL Checker
Python
License

z3r0x is a lightweight Python-based tool designed to check the accessibility of multiple URLs. It verifies whether a given list of URLs is accessible or broken and provides a clear output with visual indicators (✅ for accessible, ❌ for broken). It’s perfect for developers, system administrators, and anyone who needs to monitor the status of multiple websites or endpoints.

Features
Multi-URL Support: Check the accessibility of multiple URLs in one go.

Visual Indicators: Green tick (✅) for accessible URLs and red cross (❌) for broken URLs.

Simple and Lightweight: Easy to use with minimal dependencies.

Customizable: Add or remove URLs from the list as needed.

Fast and Efficient: Uses Python's requests library for quick HTTP requests.

Documentation: Detailed documentation is available on GitBook.

Installation
Prerequisites
Python 3.6 or higher.

requests library (installed automatically if not present).

Steps
Clone the repository:

bash
Copy
git clone https://github.com/silentfort/z3r0x.git
cd z3r0x
Install the required dependencies:

bash
Copy
pip install requests
Run the script:

bash
Copy
python z3r0x.py
Usage
Add the URLs you want to check in the site_urls list inside the z3r0x.py file:

python
Copy
site_urls = [
    "https://www.google.com",
    "https://www.example.com",
    "https://www.nonexistentwebsite123.com",
    "https://www.github.com"
]
Run the script:

bash
Copy
python z3r0x.py
View the output:

Copy
OK https://www.google.com ✅
OK https://www.example.com ✅
BROKEN https://www.nonexistentwebsite123.com ❌
OK https://www.github.com ✅
Documentation
For detailed documentation, including advanced usage, configuration options, and troubleshooting, visit the z3r0x Documentation.

Contributing
Contributions are welcome! If you’d like to contribute to z3r0x, please follow these steps:

Fork the repository.

Create a new branch for your feature or bugfix.

Commit your changes.

Push your branch and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Support
If you encounter any issues or have questions, feel free to open an issue on the GitHub repository.

Acknowledgments
Thanks to the Python community for creating amazing tools and libraries.

Special thanks to the requests library for making HTTP requests simple and efficient.

Enjoy using z3r0x! 🚀
