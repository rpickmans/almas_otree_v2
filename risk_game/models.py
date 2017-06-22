# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'Benson'

doc = """
In this Game, six different coins with different amounts for heads and tails.
Subjects can choose which coin they want to ip and then get the money that's associated with either heads or tails.
"""


class Constants(BaseConstants):
    name_in_url = 'risk_game'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    def make_random_toss(self):
        for p in self.get_players():
            p.random_coin_toss = random.choice(["Heads", "Tails"])

    def set_payoffs(self):
        for p in self.get_players():
            if p.decision == "Coin 1":
                p.payoff = 80
                p.participant.vars["carrying_payoff"] += p.payoff
                p.participant.vars["main_carrying_payoff"] += p.payoff

            elif p.decision == "Coin 2":
                if p.random_coin_toss == "Heads":
                    p.payoff = 70
                    p.participant.vars["carrying_payoff"] += p.payoff
                    p.participant.vars["main_carrying_payoff"] += p.payoff
                else:
                    p.payoff = 110
                    p.participant.vars["carrying_payoff"] += p.payoff
                    p.participant.vars["main_carrying_payoff"] += p.payoff

            elif p.decision == "Coin 3":
                if p.random_coin_toss == "Heads":
                    p.payoff = 60
                    p.participant.vars["carrying_payoff"] += p.payoff
                    p.participant.vars["main_carrying_payoff"] += p.payoff
                else:
                    p.payoff = 140
                    p.participant.vars["carrying_payoff"] += p.payoff
                    p.participant.vars["main_carrying_payoff"] += p.payoff

            elif p.decision == "Coin 4":
                if p.random_coin_toss == "Heads":
                    p.payoff = 50
                    p.participant.vars["carrying_payoff"] += p.payoff
                    p.participant.vars["main_carrying_payoff"] += p.payoff
                else:
                    p.payoff = 170
                    p.participant.vars["carrying_payoff"] += p.payoff
                    p.participant.vars["main_carrying_payoff"] += p.payoff

            elif p.decision == "Coin 5":
                if p.random_coin_toss == "Heads":
                    p.payoff = 40
                    p.participant.vars["carrying_payoff"] += p.payoff
                    p.participant.vars["main_carrying_payoff"] += p.payoff
                else:
                    p.payoff = 200
                    p.participant.vars["carrying_payoff"] += p.payoff
                    p.participant.vars["main_carrying_payoff"] += p.payoff

            elif p.decision == "Coin 6":
                if p.random_coin_toss == "Heads":
                    p.payoff = 30
                    p.participant.vars["carrying_payoff"] += p.payoff
                    p.participant.vars["main_carrying_payoff"] += p.payoff
                else:
                    p.payoff = 210
                    p.participant.vars["carrying_payoff"] += p.payoff
                    p.participant.vars["main_carrying_payoff"] += p.payoff


class Player(BasePlayer):
    decision_choices = (
            ("Coin 1", "Coin 1: KSH 80 if heads and KSH 80 if tails"),
            ("Coin 2", "Coin 2: KSH 70 if heads and KSH 110 if tails"),
            ("Coin 3", "Coin 3: KSH 60 if heads and KSH 140 if tails"),
            ("Coin 4", "Coin 4: KSH 50 if heads and KSH 170 if tails"),
            ("Coin 5", "Coin 5: KSH 40 if heads and KSH 200 if tails"),
            ("Coin 6", "Coin 6: KSH 30 if heads and KSH 210 if tails"),
        )
    decision = models.CharField(choices=decision_choices, widget=widgets.RadioSelect())
    random_coin_toss = models.CharField()
