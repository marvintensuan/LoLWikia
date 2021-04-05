from Champions import ChampionAbility

def test_repr():
    test = ChampionAbility(ability_name='Super Mega Death Rocket')
    assert repr(test) == "ChampionAbility(ability_name='Super Mega Death Rocket', base_damage=[], base_damage_type='')"