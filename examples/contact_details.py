"""Find public contact details for a list of company websites.
pip install apify-client ; set APIFY_TOKEN in your environment."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("laudable_instrument/contact-details-scraper-half-price").call(
    run_input={"urls": ["zoho.com", "basecamp.com"], "maxPagesPerSite": 4}
)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item["domain"], item["status"], item["counts"])
