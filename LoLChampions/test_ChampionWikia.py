from Champions import ChampionWikia

def test_champion_name_string_case():
    test = ChampionWikia('rEnEkToN')
    assert test.champion_name == 'Renekton'

def test_url_string_case():
    test = ChampionWikia('rEnEkToN')
    assert test.url == "https://leagueoflegends.fandom.com/wiki/renekton/LoL"
