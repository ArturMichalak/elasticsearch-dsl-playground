from copy import deepcopy
from datetime import datetime
from pytz import timezone, utc

from elasticsearch_dsl import Text, Keyword, Date, Integer, Document
from elasticsearch_dsl.exceptions import IllegalOperation
from elasticsearch_dsl.connections import connections, add_connection

from pytest import fixture


class Article(Document):
    title = Text(analyzer='snowball', fields={'raw': Keyword()})
    author = Text(analyzer='snowball')
    body = Text(analyzer='snowball')
    tags = Keyword()
    published_from = Date()
    lines = Integer()

    def to_dict(self, include_meta=False, skip_empty=True):
        self.title = ' '.join(self.title.split())\
            if self.title else self.title
        self.author = ' '.join(self.author.split())\
            if self.author else self.author
        self.body = ' '.join(self.body.strip().split(' '))\
            if self.body else self.body
        self.published_from = self.published_from.isoformat()\
            .replace('+00:00', 'Z')\
            if self.published_from else self.published_from
        self.lines = len(self.body.strip().split('\n')) if self.body else 0
        return super(Article, self).to_dict(include_meta, skip_empty)

    class Index:
        name = 'blog'
        settings = {
          'number_of_shards': 2,
        }

    def save(self, ** kwargs):
        return super(Article, self).save(** kwargs)

    def is_published(self):
        return datetime.now(utc) >= self.published_from
