from bs4 import BeautifulSoup as bs
from Champions import ChampionWikia

def test_import_bs():
    assert 'bs' in globals()

def test_import_ChampionWikia():
    assert 'ChampionWikia' in globals()
