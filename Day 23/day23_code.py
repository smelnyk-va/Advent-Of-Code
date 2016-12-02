class WizardSimulator20XX:

    def __init__(self, player_health, player_mana, player_armor, active_spells):
        self.player_health = player_health
        self.player_mana = player_mana
        self.player_armor = player_armor
        self.boss_health = 51  # from input file
        self.boss_damage = 9  # from input file
        self.active_spells = active_spells
        self.player_spellbook = {
            'magic_missile':
                {
                    'mana_cost': 53, 'is_an_effect': False, 'turn_duration': 1,
                    'damage': 4,     'heals_player': 0,     'mana_regen': 0,
                    'armor_boost': 0,
                },
            'drain':
                {
                    'mana_cost': 73, 'is_an_effect': False, 'turn_duration': 1,
                    'damage': 2,     'heals_player': 2,     'mana_regen': 0,
                    'armor_boost': 0,
                },
            'shield':
                {
                    'mana_cost': 113, 'is_an_effect': True, 'turn_duration': 6,
                    'damage': 0,      'heals_player': 0,    'mana_regen': 0,
                    'armor_boost': 7,
                },
            'poison':
                {
                    'mana_cost': 173, 'is_an_effect': True, 'turn_duration': 6,
                    'damage': 3,      'heals_player': 0,    'mana_regen': 0,
                    'armor_boost': 0,
                },
            'recharge':
                {
                    'mana_cost': 229, 'is_an_effect': True, 'turn_duration': 5,
                    'damage': 0,      'heals_player': 0,    'mana_regen': 101,
                    'armor_boost': 0,
                }
        }

    def play_game(self):

        turn = 0;


    # player turn

    # boss turn

    # effects are dealt on the next round?
