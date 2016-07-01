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
    players_per_group = 2
    num_rounds = 1
    efficiency_factor = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    def player_one_decision(self):
        # for p in self.get_players():
        #     if p.participant.vars["rank"] == "high":
        #         if p.id == 1:
        #             p.payoff = c(150) - p.keep
        #     elif p.participant.vars["rank"] == "low":
        #         p.payoff = c(50) - p.keep
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        if p2.participant.vars["rank"] == "high":
            p2.payoff = c(150) - p1.keep
            p1.payoff = c(150) - p1.keep
        elif p1.participant.vars["rank"] == "low":
            p2.payoff = c(50) - p1.keep
            p1.payoff = c(50) - p2.keep

    def player_two_decision(self):
        p1 = self.get_player_by_id(2)
        p2 = self.get_player_by_id(1)
        if p2.participant.vars["rank"] == "high":
            p2.payoff = c(150) - p1.keep
            p1.payoff = c(150) - p2.keep
        elif p1.participant.vars["rank"] == "low":
            p2.payoff = c(50) - p1.keep
            p1.payoff = c(50) - p2.keep

    def set_payoffs(self):
        choice([self.player_one_decision, self.player_two_decision])()
        for p in self.get_players():
            print("player id {} has payoff us {}".format(p.id, p.payoff))


class Player(BasePlayer):
    keep = models.CurrencyField()
    contribution = models.CurrencyField()

