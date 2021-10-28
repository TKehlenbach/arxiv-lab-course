import arxiv
from genderize import Genderize

search = arxiv.Search(
    query='physics',
    max_results=1000
)

gender_results=[]

for result in search.results():
    authors = result.authors
    firstnames = [str(author).split(' ')[0] for author in authors]
    gender_results.append(Genderize().get([firstnames]))
    print(Genderize().get([firstnames]))
