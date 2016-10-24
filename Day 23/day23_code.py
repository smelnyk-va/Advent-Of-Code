class WizardSimulator20XX:

    def __init__(self, player_health, player_mana, player_armor, player_spellbook):
        self.player_health = player_health
        self.player_mana = player_mana
        self.player_armor = player_armor
        self.player_spellbook = player_spellbook
        self.boss_health = 51  # from input file
        self.boss_damage = 9  # from input file

    player_spellbook = {
        'magic_missle':
            {
                'mana_cost': 53,
                'is_an_effect': False,
                'turn_duration': 1,  #instant
                'damage': 4,
                'heals_player': 0,
                'mana_regen': 0,
                'armor_boost': 0,
            },
        'drain':
            {
                'mana_cost': 73,
                'is_an_effect': False,
                'turn_duration': 1,  #instant
                'damage': 2,
                'heals_player': 2,
                'mana_regen': 0,
                'armor_boost': 0,
            },
        'shield':
            {
                'mana_cost': 113,
                'is_an_effect': True,
                'turn_duration': 6,  # Each turn your armor is increased by 7 (for a total of 36 after 6 turns)
                'damage': 0,
                'heals_player': 0,
                'mana_regen': 0,
                'armor_boost': 7,
            },
        'poison':
            {
                'mana_cost': 173,
                'is_an_effect': True,
                'turn_duration': 6,  # Each turn deals 3 damage (for a total of 18 after 6 turns)
                'damage': 3,
                'heals_player': 0,
                'mana_regen': 0,
                'armor_boost': 0,
            },
        'recharge':
            {
                'mana_cost': 229,
                'is_an_effect': True,
                'turn_duration': 5,  # Each turn recovers 101 mana (for a total of 505 after 5 turns)
                'damage': 0,
                'heals_player': 0,
                'mana_regen': 101,
                'armor_boost': 0,
            }
    }
