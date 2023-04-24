import requests
from bs4 import BeautifulSoup
import os

def url_to_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return ""

    soup = BeautifulSoup(response.text, "html.parser")
    text = ' '.join(s.get_text(strip=True) for s in soup.find_all('p'))
    return text

def save_to_file(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

def main():
    urls = [
        "https://learn.microsoft.com/en-us/azure/container-registry/container-registry-helm-repos",
        "https://learn.microsoft.com/en-us/azure/container-registry/container-registry-oci-artifacts"
        # Add more URLs here
    ]

    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for url in urls:
        print(f"Fetching text from {url}")
        text = url_to_text(url)

        filename = os.path.join(output_dir, f"{url.split('/')[-1]}.txt")
        save_to_file(filename, text)
        print(f"Saved text from {url} to {filename}")

if __name__ == "__main__":
    main()