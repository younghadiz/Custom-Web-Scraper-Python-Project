# Custom-Web-Scraper-Python-Project
Python code for a custom web scraper to collect data on things that are interested in.

# How it works

You need to replace `TARGET_URL` with the URL of the website you would like to scrape and inspect the website’s HTML structure to determine the classes or tags of the elements you want to scrape. Then, update the selectors in the `scrape_data` function (e.g., `soup.find_all("div", class_="item-class"`)).

# Notes:

Ensure you always check the website’s robots.txt file and their terms to ensure scraping is allowed on the website and also ensure you use delays or rate-limiting to avoid overwhelming the server. You can add `time.sleep()` between requests for politeness and abide to their terms.
