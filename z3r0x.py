import requests

def check_site_accessibility(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return True, url  # URL is accessible
        else:
            return False, url  # URL is broken
    except requests.RequestException:
        return False, url  # URL is broken

# List of URLs to check (your provided URLs)
site_urls = [
    "https://www.google.com"
    "https://www.example.com,
]

# Lists to store results
accessible_urls = []
broken_urls = []

# Total number of URLs to check
total_urls = len(site_urls)

# Check accessibility of each URL
for index, url in enumerate(site_urls, start=1):
    print(f"Checking URL {index}/{total_urls}...", end="\r")
    is_accessible, url = check_site_accessibility(url)
    if is_accessible:
        accessible_urls.append(url)
    else:
        broken_urls.append(url)

# Display results
print("\n=== ACCESSIBLE URLs ===")
for url in accessible_urls:
    print(f"OK {url} ✅")

print("\n=== BROKEN URLs ===")
for url in broken_urls:
    print(f"BROKEN {url} ❌")

# Summary
print("\n=== SUMMARY ===")
print(f"Total URLs checked: {total_urls}")
print(f"Accessible URLs: {len(accessible_urls)}")
print(f"Broken URLs: {len(broken_urls)}") 
