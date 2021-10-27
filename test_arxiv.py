import arxiv
from genderize import Genderize

search = arxiv.Search(
    query =  "quantum",
    max_results = float('inf')
)

for result in search.results():
    authors = result.authors
    firstnames = [str(author).split(' ')[0] for author in authors]
    print(Genderize().get([firstnames]))

