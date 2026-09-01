PubMed Paper Finder
Video Demo:https://youtu.be/1i4oO6B47Bw?si=8aaayCkr46ro7vSF
Description
PubMed Paper Finder is a command-line program written in Python that allows users to search for medical and scientific journal articles from PubMed. The user enters a search term, a minimum publication year, and the desired number of results. The program then connects to the PubMed API and displays information about matching articles directly in the terminal.
For each article, the program displays its title, authors, journal name, publication year, PMID, and PubMed URL. The URL allows the user to open the article’s PubMed page for further reading. The program is intended to provide a simple way to search PubMed without manually constructing API URLs or reading raw JSON data.
The project uses two services from the NCBI E-utilities API. First, it uses ESearch to find articles that match the user’s search term and publication-year requirement. ESearch returns a list of PubMed identifiers, or PMIDs. The program includes the minimum publication year directly in the PubMed search query, so articles are filtered before the requested number of results is selected.
Second, the program sends the returned PMIDs to ESummary. ESummary returns information about each article, including its title, authors, journal, and publication date. The JSON response is converted into Python dictionaries and lists using the json() method provided by the Requests library.
The project contains the following files:
* project.py contains the main program. Its main function collects and validates user input, calls the PubMed search functions, and displays the results.
* test_project.py contains tests for the program’s main custom functions. The tests check that ESearch returns the requested number of numeric PMIDs, that ESummary returns the expected article information, and that the display function prints the required fields.
* requirements.txt lists requests, the external Python package required to send HTTP requests to the PubMed API.
* README.md explains the purpose, structure, implementation, and design decisions of the project.
The search_pubmed function sends the keyword, minimum year, and result count to ESearch and returns a list of PMIDs. The fetch_articles function joins those PMIDs into a comma-separated string, sends them to ESummary, and returns a list of article dictionaries. The display_articles function extracts the relevant fields from each dictionary and formats them for terminal output.
The program validates user input before connecting to PubMed. The search term cannot be empty, the minimum year must be a valid integer, and the number of results must be between 1 and 20. Limiting the number of results prevents the terminal output from becoming unnecessarily large. The program also handles connection failures and HTTP errors by displaying a readable error message instead of a Python traceback.
One design decision was to use ESummary rather than EFetch. ESummary provides all the information required by this project while keeping the returned data relatively small. EFetch could provide abstracts and more detailed article records, but parsing that additional data would make the program significantly more complicated.
Because this program retrieves current information from PubMed, an internet connection is required both to run the program and to execute the API-related tests.


- Search PubMed by keyword and publication year.
- Choose how many articles to display.
