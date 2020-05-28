import os

from elasticsearch_dsl.connections import connections, add_connection

from pytest import fixture
from unittest.mock import MagicMock


@fixture
def mock_client(dummy_response):
    client = MagicMock()
    client.search.return_value = dummy_response
    add_connection('mock', client)
    yield client
    connections._conn = {}
    connections._kwargs = {}


@fixture
def dummy_response():
    return {
        '_shards': {
            'failed': 0,
            'successful': 10,
            'total': 10
        },
        'hits': {
            'hits': [
                {
                    '_index': 'blog',
                    '_type': '_doc',
                    '_id': '1',
                    '_score': '10.114',
                    '_source': {
                        'title': 'Test elasticsearch',
                        'body': '''
Litwo! Ojczyzno moja! Ty jesteś jak zdrowie. Ile cię stracił.
Dziś człowieka nie policzę.
Opuszczali rodziców i jeszcze dobrze
na kozłach niemczysko chude na Ojczyzny łono.
Tymczasem na nim się zdawał małpą lub ławę przeskoczyć.
Zręcznie między dwie strony: Uciszcie się! woła.
Marząc i krwi tonęła,
gdy przysięgał na krzaki fijołkowe skłonił oczyma ciekawymi
po kryjomu kazał stoły z Paryża a czuł choroby zaród.
Krzyczano na waszych polowaniach łowił?
Piękna byłaby sława, ażeby nie było gorąca).
wachlarz pozłocist powiewając rozlewał deszcz iskier rzęsisty.
Głowa do Twych świątyń progi iść
za zającami nie został pośmiewiska celem i niesrogi.
Odgadnęła sąsiadka powód jego lata
wleką w kota się nagle, stronnicy Sokół na kształt deski.
Nogi miał głos miły: Witaj nam,
że spod ramion wytknął palce i Asesor, razem, jakoby zlewa.
I też co się przyciągnąć do dworu
uprawne dobrze zachowana sklepienie całe wesoło, lecz w rozmowę lecz lekki.
odgadniesz, że jacyś Francuzi wymowny
zrobili wynalazek: iż ludzie są architektury.
Choć Sędzia jego bok usiadła
owa piękność zda się Gorecki, Pac i opisuję,
bo tak nas reformować cywilizować
będzie wojna u nas starych więcej godni
Wojewody względów doszli potem się teraz
wzrostem dorodniejsza bo tak pan Wojski na nim ją w ulicę się tajemnie,
Ścigany od płaczącej matki pod
Turka czy wstydzić, czy na lewo,
on rodaków zbiera się w domu dostatek mieszka i panien
nie w nieczynności! a Suwarów w posiadłość.
                        ''',
                        'published_from': '2013-02-10T10:31:07.851688',
                        'tags': [
                            'g1',
                            'g2'
                        ],
                        'lines': '1'
                    },
                    'highlight': {
                        'title': ['<em>Test</em> elasticsearch']
                    }
                },
                {
                    '_index': 'blog',
                    '_type': '_doc',
                    '_id': '2',
                    '_score': '12.0',
                    '_source': {
                        'title': 'Test elasticsearch numer 2',
                        'body': '''
Litwo! Ojczyzno moja! Ty jesteś jak zdrowie. Ile cię stracił.
Dziś człowieka nie policzę.
Opuszczali rodziców i jeszcze dobrze
na kozłach niemczysko chude na Ojczyzny łono.
Tymczasem na nim się zdawał małpą lub ławę przeskoczyć.
Zręcznie między dwie strony: Uciszcie się! woła.
Marząc i krwi tonęła,
gdy przysięgał na krzaki fijołkowe skłonił oczyma ciekawymi
po kryjomu kazał stoły z Paryża a czuł choroby zaród.
Krzyczano na waszych polowaniach łowił?
Piękna byłaby sława, ażeby nie było gorąca).
wachlarz pozłocist powiewając rozlewał deszcz iskier rzęsisty.
Głowa do Twych świątyń progi iść
za zającami nie został pośmiewiska celem i niesrogi.
Odgadnęła sąsiadka powód jego lata
wleką w kota się nagle, stronnicy Sokół na kształt deski.
Nogi miał głos miły: Witaj nam,
że spod ramion wytknął palce i Asesor, razem, jakoby zlewa.
I też co się przyciągnąć do dworu
uprawne dobrze zachowana sklepienie całe wesoło, lecz w rozmowę lecz lekki.
odgadniesz, że jacyś Francuzi wymowny
zrobili wynalazek: iż ludzie są architektury.
Choć Sędzia jego bok usiadła
owa piękność zda się Gorecki, Pac i opisuję,
bo tak nas reformować cywilizować
będzie wojna u nas starych więcej godni
Wojewody względów doszli potem się teraz
wzrostem dorodniejsza bo tak pan Wojski na nim ją w ulicę się tajemnie,
Ścigany od płaczącej matki pod
Turka czy wstydzić, czy na lewo,
on rodaków zbiera się w domu dostatek mieszka i panien
nie w nieczynności! a Suwarów w posiadłość.
                        ''',
                        'published_from': '2014-02-10T10:31:07.851688',
                        'tags': [
                            'g1',
                            'g2'
                        ],
                        'lines': '1'
                    },
                    'highlight': {
                        'title': ['<em>Test</em> elasticsearch numer 2']
                    }
                },
            ]
        },
        "timed_out": False,
        "took": 123
    }
