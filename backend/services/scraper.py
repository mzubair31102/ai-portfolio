import requests
from bs4 import BeautifulSoup

def get_text_from_url(url):
    """
    Fetches the HTML content of a given URL and extracts the body content as plain text.

    Parameters:
        url (str): The URL of the page to scrape.

    Returns:
        str: The plain text extracted from the body of the page.
    """
    try:
        # Send a GET request to fetch the content of the URL
        response = requests.get(url)

        # If the response status is OK (200), proceed
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.content, "html.parser")

            # Extract the body text (all text inside the <body> tag)
            body = soup.find("body")
            if body:
                return body.get_text(strip=True)  # Get plain text from the body and remove extra whitespace
            else:
                return "No body content found"
        else:
            return f"Failed to retrieve content. Status code: {response.status_code}"
    
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
