import requests
import time
import random
from bs4 import BeautifulSoup

# headers to behave like a real browser
HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

# stable directory page
URLS = {
    "machinery": "https://dir.indiamart.com/impcat/air-compressors.html"
}

def fetch_page(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()
        time.sleep(random.uniform(2, 4))  # polite delay
        return response.text
    except Exception as e:
        print("Error fetching:", e)
        return None

def parse_products(html, category):
    soup = BeautifulSoup(html, "html.parser")
    products = []

    # collect product titles from links
    links = soup.find_all("a")

    for link in links:
        title = link.get_text(strip=True)

        # filter meaningful product titles
        if title and len(title) > 20 and "compressor" in title.lower():
            products.append({
                "product_name": title,
                "category": category,
                "supplier": None,
                "location": None,
                "price": None,
            })

    return products

def crawl():
    all_products = []

    for category, url in URLS.items():
        print(f"Scraping {category}...")
        html = fetch_page(url)

        if html:
            items = parse_products(html, category)
            all_products.extend(items)

    return all_products