import requests
from bs4 import BeautifulSoup  # bs4 is the package name

# setup
URL_LINK = "https://en.wikipedia.org/wiki/"

# get the page
def get_wikipedia_page(topic):
    url=f"{URL_LINK}{topic}"
    response = requests.get(url)
    if response.status_code ==200:
        return response.text
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}. Click the topic and try again.")
        return None    

# Step 2: Extract Articl Title
def get_article_title(soup):
    return soup.find('h1').text

# step 3 extract the article summary
def get_article_summary(soup, min_length=50):
    """
    Extracts the first meaningful paragraph from BeautifulSoup HTML.
    Args:
        soup: BeautifulSoup object.
        min_length: Minimum character length to qualify as a summary.
    Returns:
        str: Summary text or fallback message.
    """
    # Priority: <article>, <main>, or direct <p> tags
    containers = soup.find_all(['article', 'main']) or [soup]    
    for container in containers:
        paragraphs = container.find_all('p')
        for p in paragraphs:
            text = p.get_text().strip()
            if len(text) >= min_length:
                return text
    
    return "No summary found (all paragraphs too short or empty)"    

# step 4 extract headings
def get_article_headings(soup):
    headings = [heading.text.strip() for heading in soup.find_all(['h2','h3','h4','h5','h6'])]
    return headings

# step 5. extract related links
def get_related_links(soup):
    links = []
    for a_tag in soup.find_all('a',href=True):
        href = a_tag['href']
        if href.startswith('/wiki/') and ":" not in href:
            links.append(f"https://en.wikipedia.org{href}")
    return list(set(links))[:5]


# step 6: main program
def main():
    topic=input("Enter Topic to search in wikipedia:").strip()
    page_content = get_wikipedia_page(topic)
    if page_content:
        soup = BeautifulSoup(page_content, 'html.parser')
        title = get_article_title(soup)
        summary = get_article_summary(soup)
        headings = get_article_headings(soup)
        related_links = get_related_links(soup)
        print("\n--- Wikipedia Article Details----")
        print(f"\nTitle: {title}")
        print(f"\nSummary: {summary}")
        print("\nHeadings:")
        for heading in headings[:5]:
            print(f"- {heading}")
        print("\nRelated Links: ")
        for link in related_links:
            print(f"-{link}")

# Run the program
if __name__ == "__main__":
    main()