# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division
from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

from otree import widgets
from otree.common import Currency as c, currency_range
import random

# </standard imports>

doc = """
This is a one-period public goods game with 3 players. Assignment to groups is random.

"""


class Constants(BaseConstants):
    name_in_url = 'public_goods'
    players_per_group = 3
    num_rounds = 1

    """Amount allocated to each player"""
    endowment = 75
    efficiency_factor = 2

    guess_correct = 175

    GUESS_CHOICE = {
        1: [0],
        2: [list(range(1, 11))],
        3: [list(range(11, 21))],
        4: [list(range(21, 31))],
        5: [list(range(31, 41))],
        6: [list(range(41, 51))],
        7: [list(range(51, 61))],
        8: [list(range(61, 71))],
        9: [list(range(71, 75))],
        10: [75]
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()

    individual_share = models.CurrencyField()

    def set_payoffs(self):

        self.total_contribution = sum([p.contribution for p in self.get_players()])
        self.individual_share = self.total_contribution * Constants.efficiency_factor / Constants.players_per_group
        for p in self.get_players():
            if p.guess_correct():
                points = (Constants.endowment - p.contribution) + self.individual_share + Constants.guess_correct
                p.participant.vars["game_payoff"]["public_goods_game"] = points
                p.participant.vars["carrying_payoff"] += points
                p.payoff = points
            else:
                points = (Constants.endowment - p.contribution) + self.individual_share
                p.participant.vars["game_payoff"]["public_goods_game"] = points
                p.participant.vars["carrying_payoff"] += points
                p.payoff = points


class Player(BasePlayer):

    GUESS_CHOICES = [
        ("1", "Ksh. 0"),
        ("2", "Ksh. 1-10"),
        ("3", "Ksh. 11-20"),
        ("4", "Ksh. 21-30"),
        ("5", "Ksh. 31-40"),
        ("6", "Ksh. 41-49"),
        ("7", "Ksh. 50-59"),
        ("8", "Ksh. 60-69"),
        ("9", "Ksh. 70-74"),
        ("10", "Ksh. 75"),
    ]

    contribution = models.IntegerField(
        min=0, max=Constants.endowment,
        doc="""The amount contributed by the player""",
    )
    question = models.CurrencyField()

    guess_one = models.CharField(widget=widgets.RadioSelect(), choices=GUESS_CHOICES)
    guess_two = models.CharField(widget=widgets.RadioSelect(), choices=GUESS_CHOICES)

    def guess_correct(self):
        guess_choices = Constants.GUESS_CHOICE
        px, py = self.get_others_in_group()
        return px.contribution in guess_choices[int(self.guess_one)] and py.contribution in guess_choices[int(self.guess_two)]


