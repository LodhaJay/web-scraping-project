from playwright.sync_api import sync_playwright
import os
import re
import json
import requests
import traceback

base_url = "https://www.3idea.in/brand/bambulab"
Img_dir = r"C:\Users\JAY LODHA\web-scraping-project\data\raw\3idea_updated"
os.makedirs(Img_dir, exist_ok=True)

product_list = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(base_url)
    page.wait_for_timeout(3000)

    # Click load more button
    while True:
        load_more = page.locator("#loadMoreGridBtn")
        if load_more.is_visible():
            load_more.scroll_into_view_if_needed()
            load_more.click()
            page.wait_for_timeout(3000)
        else:
            break

    #access all product 
    product_links = page.eval_on_selector_all("div.card-product-wrapper a","elements => elements.map(e => e.href)")
    product_links = [link for link in product_links if "/product-detail/" in link]
    product_links = list(set(product_links))

    for i, link in enumerate(product_links):
        try:
            page.goto(link)
            page.wait_for_timeout(2000)

            product = {}

            # Title
            try:
                product["title"] = page.query_selector("h5.product-info-name.fw-medium").inner_text().strip()
            except:
                product["title"] = " "

            # Price
            try:
                product["current price"] = page.query_selector("div.display-sm.price-new.price-on-sale").inner_text().strip()
            except:
                product["current price"] = " "

            #discount
            try:
                product["discount"] = page.query_selector("h5.text-danger.ms-2").inner_text()
            except:
                product["discount"] = " "

            #actual price
            try:
                product["actual price"] = page.query_selector("div.display-sm.price-old").inner_text().strip()
            except:
                product["actual price"] = " "
            
            # Rating
            try:
                all_stars = page.query_selector_all("div.product-info-rate i.icon-star")
                filled_stars = page.query_selector_all("div.product-info-rate i.icon-star[style*='#98ab23']")
                half_stars = page.query_selector_all("div.product-info-rate span[style*='width: 50%']")

                rating_value = len(filled_stars) + (0.5 * len(half_stars))
                product["rating"] = f"{rating_value}/{len(all_stars)-1}"
            except:
                product["rating"] = "N/A"

            #Product features
            try:
                desc=page.locator(".desc.text-sm.text-main.text-line-clamp-2.text-align-last-end").all_inner_texts()
                product["Product features"]=desc
            except:
                product["Product features"]=" "

            # Accordion open karo pehle
            for accordion in page.query_selector_all("div.accordion-title.collapsed"):
                try:
                    accordion.click()
                    page.wait_for_timeout(500)
                except:
                    pass

            # Features
            try:
                feature_items = page.query_selector_all("#feature ul li")
                product["more features"] = [li.inner_text().strip() for li in feature_items if li.inner_text().strip()]
            except:
                product["more features"] = []

            # Description
            try:
                product["description"] = page.query_selector("#description div.item").inner_text().strip()
            except:
                product["description"] = " "

            # Specifications
            try:
                spec_items = page.query_selector_all("#specification ul li")
                product["specifications"] = [li.inner_text().strip() for li in spec_items if li.inner_text().strip()]
            except:
                product["specifications"] = []

            try:
                # Create product directory
                safe_title = re.sub(r'[\\/*?:"<>|]', "", product["title"])
                product_dir = os.path.join(Img_dir, safe_title)
                os.makedirs(product_dir, exist_ok=True)
                # Scrape all images
                try:
                    img_elements = page.query_selector_all("div.swiper-slide.stagger-item.stagger-finished img")
                    for idx, img_el in enumerate(img_elements):
                        img_url = img_el.get_attribute("src") or img_el.get_attribute("data-src")
                        if img_url:
                            img_path = os.path.join(product_dir, f"image_{idx+1}.jpg")
                            response = page.context.request.get(img_url)                            
                            if response.status == 200:
                                with open(img_path, "wb") as f:
                                    f.write(response.body())
                except Exception as e:
                    print(f"Image error for {product['title']}: {e}")

            except Exception as e:
                pass

            product_list.append(product)
            print(f"{i+1}. {product['title']} Scraped")

        except Exception as e:
            print(f"{i+1}. failed {e}")
            continue

    browser.close()

with open(r"C:\Users\JAY LODHA\web-scraping-project\data\raw\3idea_bambu_products_updated.json", "w", encoding="utf-8-sig") as f:
    json.dump(product_list, f, ensure_ascii=False, indent=4)

print(f"Total saved: {len(product_list)}")