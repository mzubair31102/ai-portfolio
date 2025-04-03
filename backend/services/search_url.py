# import time
# from random import randint
# from duckduckgo_search import DDGS

# def duckduckgo_search(query, max_results=10):
#     """
#     Searches DuckDuckGo and returns a list of URLs.

#     Parameters:
#         query (str): The search query to send to DuckDuckGo.
#         max_results (int): The maximum number of results to retrieve. Default is 10.

#     Returns:
#         list: A list of URLs returned by DuckDuckGo.
#     """
#     urls = []
#     with DDGS(headers={"User-Agent": "Mozilla/5.0"}) as ddgs:  # Add User-Agent
#         results = ddgs.text(query, max_results=max_results)  # Get the specified number of results
#         for result in results:
#             urls.append(result["href"])  # Extract URL

#     # Random delay (1-3 seconds) to prevent blocking or rate limiting
#     time.sleep(randint(1, 3))  
#     return urls

# # qury = "Blog posts about AI tools and their applications"
# # urls = duckduckgo_search(qury)
# # for url in urls:
# #     print(url)


def duckduckgo_search(query, max_results=10):
    return [
        "https://www.gadgets360.com/mobiles/reviews/iphone-16-pro-max-review-6702737",
        "https://www.91mobiles.com/hub/apple-iphone-16-pro-max-review/",
        "https://www.digit.in/reviews/mobile-phones/iphone-16-pro-max-review-an-iterative-upgrade-yet-a-premium-powerhouse.html",
        "https://www.stuffindia.in/reviews/apple-iphone-16-pro-max-review/546",
        "https://zeenews.india.com/technology/iphone-16-pro-max-review-maxing-out-perfection-2804901.html",
        "https://www.indiatoday.in/technology/reviews/story/iphone-16-pro-max-and-iphone-16-pro-review-kings-in-waiting-2607194-2024-09-27",
        "https://indianexpress.com/article/technology/tech-reviews/apple-iphone-16-review-9584824/",
        "https://www.deccanherald.com/technology/gadgets/apple-iphone-16-pro-max-review-powerful-mobile-with-meaningful-upgrades-3286130",
        "https://www.businesstoday.in/tech-today/unboxing-reviews/story/apple-iphone-16-pro-max-review-a-true-flagship-448111-2024-09-30",
        "https://www.business-standard.com/technology/tech-reviews/apple-iphone-16-pro-max-review-a-pro-grade-phone-set-to-get-better-with-ai-124102100509_1.html"
    ]