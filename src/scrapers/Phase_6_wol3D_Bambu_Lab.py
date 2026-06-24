from playwright.sync_api import sync_playwright
import json
import os
import requests
import re

BASE_URL = "https://wol3d.com/product-category/brand/bambu-lab/3d-printer/"
IMG_DIR = r"C:\Users\JAY LODHA\web-scraping-project\data\raw\Wol3D_Updated"
os.makedirs(IMG_DIR, exist_ok=True)

products_list = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(BASE_URL)
    page.wait_for_timeout(3000)

    # Get all product links from listing page
    product_links = page.eval_on_selector_all(
        "h3.heading-title.product-name a",
        "elements => elements.map(e => e.href)"
    )
    product_links = list(set(product_links))
    print(f"Total products found: {len(product_links)}")

    for i, link in enumerate(product_links):
        try:
            page.goto(link)
            page.wait_for_timeout(2000)

            product = {}

            # Title
            try:
                product["title"] = page.query_selector("h1.product_title").inner_text().strip()
            except:
                product["title"] = " "

            # Price
            try:
                product["price"] = page.query_selector("span.woocommerce-Price-amount.amount").inner_text().strip()
            except:
                product["price"] = " "

            # Rating
            try:
                rating_el = page.query_selector("div.woocommerce-product-rating strong.rating")
                if rating_el:
                    product["rating"] = rating_el.inner_text().strip()
                else:
                    product["rating"] = "N/A"
            except:
                product["rating"] = "N/A"

            #review count
            try:
                product["review count"]=page.query_selector("span.rating").inner_text()
            except:
                product["review count"]=" "

            # Features 
            try:
                features = page.query_selector_all("div.summary ul li")
                product["features"] = [f.inner_text().strip() for f in features]
            except:
                product["features"] = []

            # Description
            try:
                product["description"] = page.query_selector("div#tab-description").inner_text().strip()
            except:
                product["description"] = " "

            # Warranty
            try:
                # Click warranty tab
                warranty_tab = page.query_selector("a[href='#tab-warranty']")
                if warranty_tab:
                    warranty_tab.click()
                    page.wait_for_timeout(1500)

                # Extract warranty table rows
                warranty_rows = page.query_selector_all("#tab-warranty table tr")
                warranty_data = {}
                current_section = None

                for row in warranty_rows:
                    cells = [c.inner_text().strip() for c in row.query_selector_all("td") if c.inner_text().strip()]
                    if not cells:
                        continue
                    
                    # Detect section headers (e.g., "12 Months Warranty")
                    if any("Warranty" in c for c in cells):
                        current_section = cells[0]
                        warranty_data[current_section] = []
                    elif current_section:
                        warranty_data[current_section].extend(cells)

                product["warranty"] = warranty_data
            except Exception as e:
                product["warranty"] = {}
                print(f"Warranty scrape failed for {product['title']}: {e}")

            # Image - download and save
            try:
                # Create product directory
                safe_title = re.sub(r'[\\/*?:"<>|]', "", product["title"])
                product_dir = os.path.join(IMG_DIR, safe_title)
                os.makedirs(product_dir, exist_ok=True)
                # Scrape all images
                try:
                    img_elements = page.query_selector_all("div.woocommerce-product-gallery ol li img")
                    for idx, img_el in enumerate(img_elements):
                        img_url = img_el.get_attribute("src")
                        if img_url:
                            img_path = os.path.join(product_dir, f"image_{idx+1}.jpg")
                            response = requests.get(img_url)
                            if response.status_code == 200 and len(response.content) > 1000:
                                with open(img_path, "wb") as f:
                                    f.write(response.content)
                except Exception as e:
                    print(f"Image error for {product['title']}: {e}")

            except Exception as e:
                pass

            products_list.append(product)
            print(f"{i+1}. {product['title']} scraped")

        except Exception as e:
            print(f"{i+1}. failed {e}")
            continue

    browser.close()

with open(r"C:\Users\JAY LODHA\web-scraping-project\data\raw\Wol3d_bambu_products_updated.json", "w", encoding="utf-8-sig") as f:
    json.dump(products_list, f, ensure_ascii=False, indent=4)

print(f"Total saved: {len(products_list)}")