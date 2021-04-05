from dataclasses import dataclass, field

@dataclass
class ChampionAbility:
    ability_name: str
    base_damage: list = field(init=False, default=[0,0,0,0,0])
    base_damage_type: str = field(init=False, default='')
    scale_damage: float = field(init=False, repr=False)
    scale_damage_attr: str = field(init=False, repr=False)
    ability_cost: int = field(init=False, repr=False)
    ability_cooldown: list = field(init=False, repr=False)

