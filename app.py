import requests
from bs4 import BeautifulSoup
import csv
import time

# Define the target URL and headers for the scraper
TARGET_URL = "https://example.com"  # Replace with your target URL
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

# Define the scraper function
def scrape_data():
    try:
        # Send an HTTP request to the target URL
        response = requests.get(TARGET_URL, headers=HEADERS)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Example: Extract specific data (e.g., articles or products)
        # Modify the selectors based on the website's structure
        items = soup.find_all("div", class_="item-class")  # Replace with actual HTML structure

        # Collect data into a list
        scraped_data = []
        for item in items:
            title = item.find("h2").get_text(strip=True)  # Example: Extract title
            link = item.find("a")["href"]  # Extract link
            date = item.find("span", class_="date-class").get_text(strip=True)  # Extract date
            scraped_data.append({"title": title, "link": link, "date": date})

        return scraped_data

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

# Save the scraped data to a CSV file
def save_to_csv(data, filename="scraped_data.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "link", "date"])
        writer.writeheader()
        writer.writerows(data)

# Main execution
if __name__ == "__main__":
    print("Starting the scraper...")
    scraped_data = scrape_data()

    if scraped_data:
        print(f"Scraped {len(scraped_data)} items. Saving to CSV...")
        save_to_csv(scraped_data)
        print("Data saved successfully.")
    else:
        print("No data scraped.")
