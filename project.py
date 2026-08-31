import requests

def main():
    keywords = input("Search term: ").strip()

    if not keywords:
        print("Search term cannot be empty.")
        return

    try:
        minimum_year = int(input("Minimum year: "))
        result_count = int(input("Number of results: "))
    except ValueError:
        print("Year and number of results must be integers.")
        return

    if minimum_year < 1 or minimum_year > 3000:
        print("Minimum year must be between 1 and 3000.")
        return

    if result_count < 1 or result_count > 20:
        print("Number of results must be between 1 and 20.")
        return

    try:
        pmids = search_pubmed(keywords, minimum_year, result_count)
        articles = fetch_articles(pmids)
        display_articles(articles)
    except requests.RequestException:
        print("Could not connect to Pubmed.")


def search_pubmed(keywords, minimum_year, result_count):
    response = requests.get(
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi",
        params={
            "db": "pubmed",
            "term": f"{keywords} AND {minimum_year}:3000[dp]",
            "retmax": result_count,
            "retmode": "json"
        }
    )
    data = response.json()



    return data["esearchresult"]["idlist"]


def fetch_articles(pmids):
    if not pmids:
        return []
    ids = ','.join(pmids)

    response = requests.get(
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi",
        params= {
            "db": "pubmed",
            "id": ids,
            "retmode": "json"
        }
    )
    data = response.json()

    articles = []
    for pmid in data["result"]["uids"]:
        article = data["result"][pmid]
        articles.append(article)
    return articles


def display_articles(articles):
    if not articles:
        print("No articles founds. ")
        return

    for number, article in enumerate(articles, start=1):
        author_names = []

        for author in article.get("authors", []):
            author_names.append(author["name"])

        authors = ", ".join(author_names)

        title = article.get("title", "Unknown title")
        journal = article.get("fulljournalname", "Unknown journal")
        pubdate = article.get("pubdate", "")
        pmid = article.get("uid", "Unknown PMID")

        if pubdate:
            year = pubdate.split()[0]
        else:
            year = "Unknown year"

        print()
        print(f"{number}. {title}")
        print(f"Authors: {authors}")
        print(f"Journal: {journal}")
        print(f"Year: {year}")
        print(f"PMID: {pmid}")
        print(f"URL: https://pubmed.ncbi.nlm.nih.gov/{pmid}/")


if __name__ == "__main__":
    main()
