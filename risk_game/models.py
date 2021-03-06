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
        points = 0
        for p in self.get_players():
            if p.decision == "Coin 1":
                if p.random_coin_toss == "Heads":
                    p.payoff = 0
                    points = 0
                else:
                    p.payoff = 2880
                    points = 2880

            elif p.decision == "Coin 2":
                if p.random_coin_toss == "Heads":
                    p.payoff = 240
                    points = 240
                else:
                    p.payoff = 2400
                    points = 2400

            elif p.decision == "Coin 3":
                if p.random_coin_toss == "Heads":
                    p.payoff = 480
                    points = 480
                else:
                    p.payoff = 1920
                    points = 1920

            elif p.decision == "Coin 4":
                if p.random_coin_toss == "Heads":
                    p.payoff = 720
                    points = 720
                else:
                    p.payoff = 1440
                    points = 1440

            elif p.decision == "Coin 5":
                if p.random_coin_toss == "Heads":
                    p.payoff = 840
                    points = 840
                else:
                    p.payoff = 1200
                    points = 1200

            elif p.decision == "Coin 6":
                if p.random_coin_toss == "Heads":
                    p.payoff = 960
                    points = 960
                else:
                    p.payoff = 960
                    points = 960

            elif p.decision == "Coin 7":
                if p.random_coin_toss == "Heads":
                    p.payoff = 1080
                    points = 1080
                else:
                    p.payoff = 720
                    points = 720

            p.participant.vars["game_payoff"]["risk_game"] = points
            p.participant.vars["carrying_payoff"] += points



class Player(BasePlayer):
    decision_choices = (
            ("Coin 1", "Coin 1: 0 Tokens if heads and 2880 Tokens if tails"),
            ("Coin 2", "Coin 2: 240 Tokens if heads and 2400 Tokens if tails"),
            ("Coin 3", "Coin 3: 480 Tokens if heads and 1920 Tokens if tails"),
            ("Coin 4", "Coin 4: 720 Tokens if heads and 1440 Tokens if tails"),
            ("Coin 5", "Coin 5: 840 Tokens if heads and 1200 Tokens if tails"),
            ("Coin 6", "Coin 6: 960 Tokens if heads and 960 Tokens if tails"),
            ("Coin 7", "Coin 6: 1080 Tokens if heads and 720 Tokens if tails"),
        )
    decision = models.CharField(choices=decision_choices, widget=widgets.RadioSelect())
    random_coin_toss = models.CharField()
