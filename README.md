# PubMed Paper Finder

A command-line Python tool that searches PubMed and shows matching articles directly in the terminal.

**Video Demo:** https://youtu.be/1i4oO6B47Bw?si=8aaayCkr46ro7vSF

## What it does

- Search PubMed by keyword and minimum publication year.
- Choose how many articles to display (1–20).
- For each article, show the title, authors, journal, year, PMID, and a PubMed link.

No need to build API URLs by hand or read raw JSON.

## Example

```
$ python project.py
Search term: single-cell RNA sequencing drug discovery
Minimum year: 2025
Number of results: 2

1. Integrative Identification of Candidate Protein Targets and Compounds for Dystonia Using Mendelian Randomization, Single-Cell RNA Sequencing, and Network Pharmacology.
Authors: Chen L, Fang MJ, Cheng N, Xu Y
Journal: Genes
Year: 2026
PMID: 42792961
URL: https://pubmed.ncbi.nlm.nih.gov/42792961/

2. From Glycan Biology to Drug Candidates: An Integrated Sialylation Niche Index and AI-Guided Therapeutic Framework for Head and Neck Squamous Cell Carcinoma.
Authors: Gu W, Liu C, Li J, Wang J
Journal: Biomedicines
Year: 2026
PMID: 42792842
URL: https://pubmed.ncbi.nlm.nih.gov/42792842/
```

Results come from live PubMed data, so they change over time.

## Getting started

Requires Python 3 and an internet connection.

```bash
git clone https://github.com/simon-1007/pubmed-article-finder.git
cd pubmed-article-finder
pip install -r requirements.txt
python project.py
```

Run the tests with:

```bash
pytest test_project.py
```

## How it works

The program uses two services from the [NCBI E-utilities API](https://www.ncbi.nlm.nih.gov/books/NBK25501/):

```
search term + minimum year
        │
        ▼
   ESearch  ──►  list of PMIDs
        │
        ▼
   ESummary ──►  article details (title, authors, journal, date)
        │
        ▼
   formatted output in the terminal
```

## Implementation details (CS50P Final Project)

This project was built as my final project for Harvard's CS50's Introduction to Programming with Python.

### Search flow

First, the program uses ESearch to find articles that match the user's search term and publication-year requirement. ESearch returns a list of PubMed identifiers, or PMIDs. The program includes the minimum publication year directly in the PubMed search query, so articles are filtered before the requested number of results is selected.

Second, the program sends the returned PMIDs to ESummary. ESummary returns information about each article, including its title, authors, journal, and publication date. The JSON response is converted into Python dictionaries and lists using the `json()` method provided by the Requests library.

### Files

- `project.py` contains the main program. Its `main` function collects and validates user input, calls the PubMed search functions, and displays the results.
- `test_project.py` contains tests for the program's main custom functions. The tests check that ESearch returns the requested number of numeric PMIDs, that ESummary returns the expected article information, and that the display function prints the required fields.
- `requirements.txt` lists `requests`, the external Python package required to send HTTP requests to the PubMed API.

### Functions

- `search_pubmed` sends the keyword, minimum year, and result count to ESearch and returns a list of PMIDs.
- `fetch_articles` joins those PMIDs into a comma-separated string, sends them to ESummary, and returns a list of article dictionaries.
- `display_articles` extracts the relevant fields from each dictionary and formats them for terminal output.

### Input validation and error handling

The program validates user input before connecting to PubMed. The search term cannot be empty, the minimum year must be a valid integer, and the number of results must be between 1 and 20. Limiting the number of results prevents the terminal output from becoming unnecessarily large. The program also handles connection failures and HTTP errors by displaying a readable error message instead of a Python traceback.

### Design decisions

One design decision was to use ESummary rather than EFetch. ESummary provides all the information required by this project while keeping the returned data relatively small. EFetch could provide abstracts and more detailed article records, but parsing that additional data would make the program significantly more complicated.

Because this program retrieves current information from PubMed, an internet connection is required both to run the program and to execute the API-related tests.
