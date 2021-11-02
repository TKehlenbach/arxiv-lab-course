import gender_guesser.detector as gender
import arxiv

search = arxiv.Search(
    query='physics',
    max_results=1000
)
d = gender.Detector()
gender_results=[]
not_found=-1
for result in search.results():
    authors = result.authors
    firstnames = [str(author).split(' ')[0] for author in authors]
    for name in firstnames:
        if name.find('.') == not_found:
            gender_results.append(d.get_gender(name))
            print(name, d.get_gender(name))

print(d.get_gender("Janie"))