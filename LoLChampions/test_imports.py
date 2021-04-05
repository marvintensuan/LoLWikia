from bs4 import BeautifulSoup as bs
from Champions import ChampionWikia
from Champions import ChampionAbility

def test_import_bs():
    assert 'bs' in globals()

def test_import_ChampionWikia():
    assert 'ChampionWikia' in globals()

def test_import_ChampionAbility():
    assert 'ChampionAbility' in globals()