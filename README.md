# Unadhi Scrapers: Contact Details and E-commerce Product Data (Apify)

Turn a list of company websites into one clean row of public contact details each, or turn any Shopify or WooCommerce shop into a product price feed.

- **Contact Details Scraper:** emails (role mailboxes only by default), E.164 phones, WhatsApp and Telegram links, and 14 social and messaging networks, one de-duplicated row per site. [Run it on Apify](https://apify.com/laudable_instrument/contact-details-scraper-half-price)
- **E-commerce Product Data Scraper:** title, brand, price, sale price, stock, SKU/GTIN, variants and images, one row per product. [Run it on Apify](https://apify.com/laudable_instrument/ecommerce-product-data-half-price)
- **Both** check robots.txt and each site's terms of service before fetching, use no proxies or logins, and don't charge for blocked or failed sites.

## Sample output

Contact Details Scraper (one row per site, shortened, from a real run):

```json
{
  "domain": "tanishq.co.in",
  "status": "ok",
  "pagesScraped": 4,
  "emails": [],
  "phones": [
    { "phone": "+9118002660123", "source": "tel-link", "valid": true, "country": "IN" },
    { "phone": "+918147349242", "source": "text", "whatsapp": "https://wa.me/918147349242" }
  ],
  "socials": { "instagram": [{ "url": "https://www.instagram.com/tanishqjewellery", "foundOn": "https://www.tanishq.co.in" }],
               "whatsapp": [{ "url": "https://api.whatsapp.com/send?phone=8147349242", "foundOn": "https://www.tanishq.co.in" }] },
  "counts": { "emails": 0, "phones": 3, "socialProfiles": 4, "whatsapp": 1, "telegram": 0 }
}
```

E-commerce Product Data Scraper (shortened, from a real run):

```json
{ "url": "https://nomadgoods.com/products/tracking-card-pro", "shop": "nomadgoods.com", "source": "json-ld",
  "title": "Tracking Card Pro", "brand": "Nomad Goods", "price": 45.0, "currency": "USD",
  "onSale": false, "availability": "InStock", "inStock": true, "gtin": "856504011109" }
```

## Run from code

Python (`pip install apify-client`), see [`examples/contact_details.py`](examples/contact_details.py):

```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")
run = client.actor("laudable_instrument/contact-details-scraper-half-price").call(
    run_input={"urls": ["zoho.com", "basecamp.com"], "maxPagesPerSite": 4}
)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["domain"], item["counts"])
```

curl (synchronous run that returns the product rows), see [`examples/products.sh`](examples/products.sh):

```bash
curl -X POST \
  "https://api.apify.com/v2/acts/laudable_instrument~ecommerce-product-data-half-price/run-sync-get-dataset-items?token=YOUR_APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"startUrls":[{"url":"https://scrapeme.live/shop/"}],"maxProductsPerShop":20}'
```

## Responsible use

Use the data lawfully (GDPR, India's DPDP Act, CAN-SPAM and local anti-spam rules). The contact scraper returns only shared role mailboxes unless you switch personal addresses on, and you are responsible for having a lawful basis to contact anyone.

Current pricing, full input options and our own test results are on each Apify page.

Unadhi · One mind
