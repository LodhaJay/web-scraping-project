from playwright.sync_api import sync_playwright
import json
import re
import os
import requests
import traceback

page=1
Base_url=f"https://ideal3d.in/collections/bambulab-printers?page={page}"
Img_dir=r"C:\Users\JAY LODHA\web-scraping-project\data\raw\Ideal3d"
os.makedirs(Img_dir, exist_ok=True)

product_list=[]

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page = browser.new_page()
    all_product_links=[]
    for i in range(2):
        page.goto(f"https://ideal3d.in/collections/bambulab-printers?page={i+1}")
        page.wait_for_timeout(3000)

        product_links = page.eval_on_selector_all(
            "h3.card__heading.h5 a",
            "elements => elements.map(e => e.href)"
        )
        all_product_links.extend(product_links)
        print(f"Page {i+1}: {len(product_links)} products")

    product_links = list(set(product_links))
    print(f"Total products found: {len(all_product_links)}")

    for i,link in enumerate(all_product_links):
        try:
            page.goto(link)
            page.wait_for_timeout(2000)
            product={}
            #title
            try:
                product['Title']=page.query_selector("div.product__title").inner_text()
            except:
                product['Title']=" "

            #price
            try:
                product['Price']=page.query_selector("span.price-item.price-item--regular").inner_text().strip()
            except:
                product['Price']=" "

            tabs=page.query_selector_all("li.tab__list")
            for tab in tabs:
                section = tab.inner_text().strip()

                content_div = tab.query_selector("h6")
                if content_div:
                    content_id = content_div.get_attribute("data-content-id")

                    if content_id:
                        content = page.query_selector(f"div#{content_id}")

                        if content:
                            product[section] = content.inner_text().strip()

            # Features 
            try:
                desc = page.locator("div.product__description").inner_text().strip()
                product["features"] = desc
            except:
                product["features"] = ""

            #Image
            # Image extraction fix
            try:
                img_el = page.query_selector("div.product__media img")
                img_url = img_el.get_attribute("src") or img_el.get_attribute("data-src") or img_el.get_attribute("srcset")

                if img_url:
                    # If srcset has multiple URLs, take the first one
                    if "," in img_url:
                        img_url = img_url.split(",")[0].strip().split(" ")[0]

                    # Add scheme if missing
                    if img_url.startswith("//"):
                        img_url = "https:" + img_url
                    elif img_url.startswith("/"):
                        img_url = "https://ideal3d.in" + img_url

                    session = requests.Session()
                    img_data = session.get(img_url).content
                    safe_title = re.sub(r'[\\/*?:"<>|]', "", product["Title"])
                    img_path = os.path.join(Img_dir, f"{safe_title}.jpg")
                    with open(img_path, "wb") as f:
                        f.write(img_data)
                else:
                    pass
            except Exception as e:
                product["image_path"] = " "
                traceback.print_exc()


            product_list.append(product)
            print(f"{i+1}. {product['Title']} scraped")
        
        except Exception as e:
            print(f"{i+1}. failed {e}")
            continue

    browser.close()

with open(r"C:\Users\JAY LODHA\web-scraping-project\data\raw\Ideal_3d_bambu_products.json", "w", encoding="utf-8-sig") as f:
    json.dump(product_list, f, ensure_ascii=False, indent=4)

print(f"Total saved: {len(product_list)}")