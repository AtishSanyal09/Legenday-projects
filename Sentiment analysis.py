from textblob import TextBlob
from newspaper import Article

url ="https://timesofindia.indiatimes.com/city/bengaluru/how-3-bengalureans-helped-sc-script-history-with-technology-tool/articleshow/98241338.cms?from=mdr"
article = Article(url)
article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob =TextBlob(text)
sentiment = blob.sentiment.polarity # -1 to 1
print(sentiment)
