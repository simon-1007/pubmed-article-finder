import project


def test_search_pubmed():
    pmids = project.search_pubmed("crispr", 2020, 2)

    assert len(pmids) == 2

def test_fetch_articles():
    articles = project.fetch_articles(["42613199"])

    assert len(articles) == 1
    assert articles[0]["uid"] == "42613199"
    assert "title" in articles[0]


def test_fetch_articles_empty():
    assert project.fetch_articles([]) == []

def test_display_articles(capsys):
    articles = [
        {
            "uid": "111",
            "title": "CRISPR Test Article",
            "authors": [{"name": "Smith J"}],
            "fulljournalname": "Test Journal",
            "pubdate": "2025 Aug"
        }
    ]

    project.display_articles(articles)

    output = capsys.readouterr().out

    assert "1. CRISPR Test Article" in output
    assert "Authors: Smith J" in output
    assert "Journal: Test Journal" in output
    assert "Year: 2025" in output
    assert "PMID: 111" in output
