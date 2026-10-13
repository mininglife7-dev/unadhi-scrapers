#!/usr/bin/env bash
# Product price feed from a Shopify/WooCommerce shop. Set APIFY_TOKEN first.
curl -s -X POST \
  "https://api.apify.com/v2/acts/laudable_instrument~ecommerce-product-data-half-price/run-sync-get-dataset-items?token=${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"startUrls":[{"url":"https://scrapeme.live/shop/"}],"maxProductsPerShop":20}'
