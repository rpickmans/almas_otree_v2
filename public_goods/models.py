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
    endowment = c(75)
    efficiency_factor = 2

    guess_correct = c(30)
    #
    # question_answer = c(100)


class Subsession(BaseSubsession):
    def before_session_starts(self):
        for p in self.get_players():
            p.participant.vars["carrying_payoff"] = 0


class Group(BaseGroup):

    total_contribution = models.CurrencyField()

    individual_share = models.CurrencyField()

    def set_payoffs(self):

        self.total_contribution = sum([p.contribution for p in self.get_players()])
        self.individual_share = self.total_contribution * Constants.efficiency_factor / Constants.players_per_group
        for p in self.get_players():
            if p.guess_correct():
                p.payoff = (Constants.endowment - p.contribution) + self.individual_share + Constants.guess_correct
                p.participant.vars["carrying_payoff"] += p.payoff
                p.participant.vars["main_carrying_payoff"] += p.payoff
            else:
                p.payoff = (Constants.endowment - p.contribution) + self.individual_share
                p.participant.vars["carrying_payoff"] += p.payoff
                p.participant.vars["main_carrying_payoff"] += p.payoff


class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0, max=Constants.endowment,
        doc="""The amount contributed by the player""",
    )
    question = models.CurrencyField()

    guess_one = models.CurrencyField()
    guess_two = models.CurrencyField()

    def guess_correct(self):
            p1, p2 = self.get_others_in_group()[0], self.get_others_in_group()[1]
            return self.guess_one == p1.contribution and self.guess_two == p2.contribution
