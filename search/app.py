"""import os
import string
import random
from datetime import datetime, timedelta
from elasticsearch_dsl.connections import connections
from search.doc_app import Article

connections.create_connection(hosts=[os.getenv('ELASTIC7', 'localhost:9200')])

Article.init()

idindex = 0
for i in range(0, 20):
    for j in range(0, 500):
        title = ''.join(
            random.choice(string.ascii_uppercase) for x in range(8))
        body = ''.join(
            random.choice(string.ascii_uppercase) for x in range(999))
        article = Article(
            meta={'id': idindex},
            title=f'{title}-{i}-{j}',
            body=body,
            published_from=datetime.now() + timedelta(days=int(f'{i}{j}')),
            tags=[
                random.choice(['g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8'])
            ])
        idindex = idindex + 1
        article.save()

print('-id-43-article-')

article = Article.get(id=43)
print(article.is_published())
print(article.toJson())
"""
