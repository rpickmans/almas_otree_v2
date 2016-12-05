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

    def player_two_decision(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)

        if p2.participant.vars["rank"] == "high":
<<<<<<< HEAD
            p1.payoff = p1.keep
            p2.payoff = c(150) - p1.keep
            p1.real_effort_dictator_endowment = 150
            p1.participant.vars["dictator_payoff_p1"] = p1.keep
            p2.participant.vars["dictator_payoff_p2"] = c(150) - p1.keep
        elif p2.participant.vars["rank"] == "low":
            p1.payoff = p1.keep
            p2.payoff = c(50) - p1.keep
            p1.real_effort_dictator_endowment = 50
            p1.participant.vars["dictator_payoff_p1"] = p1.keep
            p2.participant.vars["dictator_payoff_p2"] = c(50) - p1.keep
=======
            p2.payoff = p2.keep
            p1.payoff = c(150) - p2.keep

        elif p2.participant.vars["rank"] == "low":
            p2.payoff = p2.keep
            p1.payoff = c(50) - p2.keep

    def player_one_decision(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
>>>>>>> 4558e396b173f8d09e5d466b7772b527ed0fbc3a

        if p1.participant.vars["rank"] == "high":
<<<<<<< HEAD
            p2.payoff = p1.keep
            p1.payoff = c(150) - p2.keep
            p2.real_effort_dictator_endowment = 150
            p2.participant.vars["dictator_payoff_p2"] = p1.keep
            p1.participant.vars["dictator_payoff_p1"] = c(50) - p2.keep
        elif p1.participant.vars["rank"] == "low":
            p2.payoff = p2.keep
            p1.payoff = c(50) - p2.keep
            p2.real_effort_dictator_endowment = 50
            p2.participant.vars["dictator_payoff_p2"] = p1.keep
            p1.participant.vars["dictator_payoff_p1"] = c(50) - p2.keep
=======
            p1.payoff = p1.keep
            p2.payoff = c(150) - p2.keep

        elif p1.participant.vars["rank"] == "low":
            p1.payoff = p1.keep
            p2.payoff = c(50) - p1.keep
>>>>>>> 4558e396b173f8d09e5d466b7772b527ed0fbc3a

    def set_payoffs(self):
        choice([self.player_one_decision, self.player_two_decision])()

    def total_carrying_payoff(self):
        for p in self.get_players():
            if p.id_in_group == 1:
                p.participant.vars["main_carrying_payoff"] += p.participant.vars["dictator_payoff_p1"]
            elif p.id_in_group == 2:
                p.participant.vars["main_carrying_payoff"] += p.participant.vars["dictator_payoff_p2"]


class Player(BasePlayer):
    keep = models.CurrencyField()
    real_effort_dictator_endowment = models.IntegerField(initial=0)

