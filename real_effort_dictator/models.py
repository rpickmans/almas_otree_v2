# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division


from random import randrange as r_range, shuffle, choice
import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'Your name here'

doc = """
In this Game, Participants are matched in pairs and asked how much of the joint earnings they
want to transfer to the other participant.
"""


class Constants(BaseConstants):
    name_in_url = 'real_effort_dictator'
    endowment = c(50)
    players_per_group = 2
    num_rounds = 1
    efficiency_factor = 3
    answer = 25


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    def player_one_decision(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = p1.keep
        p2.payoff = Constants.endowment - p1.keep
        p1.contribution = Constants.endowment - p1.keep
        p2.contribution = Constants.endowment - p2.keep
        print("decision for player one, P1 Payoff: {}, P2 Payoff: {}".format(p1.payoff, p2.payoff))

    def player_two_decision(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p2.payoff = p2.keep
        p1.payoff = Constants.endowment - p2.keep
        p1.contribution = Constants.endowment - p1.keep
        p2.contribution = Constants.endowment - p2.keep
        print("decision for player two, P1 Payoff: {}, P2 Payoff: {}".format(p1.payoff, p2.payoff))

    def set_payoffs(self):
        choice([self.player_one_decision, self.player_two_decision])()


class Player(BasePlayer):
    keep = models.CurrencyField()
    contribution = models.CurrencyField()

