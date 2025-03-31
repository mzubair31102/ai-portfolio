import time
from random import randint
from duckduckgo_search import DDGS

def duckduckgo_search(query, max_results=10):
    """
    Searches DuckDuckGo and returns a list of URLs.

    Parameters:
        query (str): The search query to send to DuckDuckGo.
        max_results (int): The maximum number of results to retrieve. Default is 10.

    Returns:
        list: A list of URLs returned by DuckDuckGo.
    """
    urls = []
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=max_results)  # Get the specified number of results
        for result in results:
            urls.append(result["href"])  # Extract URL

    # Random delay (1-3 seconds) to prevent blocking or rate limiting
    time.sleep(randint(1, 3))  

    return urls
