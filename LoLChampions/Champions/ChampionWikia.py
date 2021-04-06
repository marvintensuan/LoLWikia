import requests
from .ChampionAbility import ChampionAbility

class ChampionWikia:
    def __init__(self, champion_name):
        self.champion_name = champion_name.capitalize()
        self.url = f"https://leagueoflegends.fandom.com/wiki/{champion_name.lower()}/LoL"
        
        # base stats id
        base_stats = [
            'Health', 'HealthRegen', 'ResourceBar', 'ResourceRegen',
            'Armor', 'AttackDamage', 'MagicResist', 'MovementSpeed',
            'AttackRange'
        ]
        self.base_stats = {
            "_".join([stat, self.champion_name]): 0.0
            for stat in base_stats
        }

        self.base_stats_lvl = {
            "_".join([stat, self.champion_name, 'lvl']): 0.0
            for stat in base_stats
        }

    def get(self):
        response = requests.get(self.url)
        self.status_code = response.status_code
        self.html = response.text
        return self.status_code

    def stat_resource_cost_percentage(self, skill, level = 1):
        '''
        Returns the rate of an ability cost over the Champion's total resource.
        '''
        if not isinstance(level, int):
            raise TypeError('Assigned level should be an int')
        if isinstance(skill, ChampionAbility):
            _resource_bar_id = 'ResourceBar' + '_' + self.champion_name
            _resource_bar_lvl_id = _resource_bar_id + '_lvl'
            _total_resource = self.base_stats[_resource_bar_id] \
                + ((level - 1)* self.base_stats[_resource_bar_lvl_id])
            return skill.ability_cost/_total_resource