from goose import Goose
# url = 'http://edition.cnn.com/2012/02/22/world/europe/uk-occupy-london/index.html?hpt=ieu_c2'
url = 'https://www.cricbuzz.com/cricket-news/117676/nkrumah-bonner-adept-at-the-waiting-game'
g = Goose()
article = g.extract(url=url)
print(article.cleaned_text)
