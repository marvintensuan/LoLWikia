import requests

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
            stat: "_".join([stat, self.champion_name])
            for stat in base_stats
        } 

        self.base_stats_lvl = {
            stat: "_".join([stat, self.champion_name, 'lvl'])
            for stat in base_stats
        } 

    def get(self):
        response = requests.get(self.url)
        self.status_code = response.status_code
        self.html = response.text
        return self.status_code