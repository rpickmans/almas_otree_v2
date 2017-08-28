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
    def player_one_decides(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        if p1.participant.vars["rank"] == "high":
            p1.payoff = p1.keep
            p2.payoff = 2400 - p1.keep
            p1.participant.vars["dictator_payoff"] = p1.payoff
            p2.participant.vars["dictator_payoff"] = p2.payoff
            p1.participant.vars["game_payoff"]["dictator"] = p1.payoff
            p2.participant.vars["game_payoff"]["dictator"] = p2.payoff

        elif p1.participant.vars["rank"] == "low":
            p1.payoff = p1.keep
            p2.payoff = 1200 - p1.keep
            p1.participant.vars["dictator_payoff"] = p1.payoff
            p2.participant.vars["dictator_payoff"] = p2.payoff
            p1.participant.vars["game_payoff"]["dictator"] = p1.payoff
            p2.participant.vars["game_payoff"]["dictator"] = p2.payoff

    def player_two_decides(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        if p2.participant.vars["rank"] == "high":
            p2.payoff = p2.keep
            p1.payoff = 2400 - p2.keep
            p1.participant.vars["dictator_payoff"] = p1.payoff
            p2.participant.vars["dictator_payoff"] = p2.payoff
            p1.participant.vars["game_payoff"]["dictator"] = p1.payoff
            p2.participant.vars["game_payoff"]["dictator"] = p2.payoff

        elif p2.participant.vars["rank"] == "low":
            p2.payoff = p2.keep
            p1.payoff = 1200 - p2.keep
            p1.participant.vars["dictator_payoff"] = p1.payoff
            p2.participant.vars["dictator_payoff"] = p2.payoff

            p1.participant.vars["game_payoff"]["dictator"] = p1.payoff
            p2.participant.vars["game_payoff"]["dictator"] = p2.payoff

    def set_payoffs(self):
        choice([self.player_one_decides, self.player_two_decides])()

    def total_carrying_payoff(self):
        for p in self.get_players():
            if p.id_in_group == 1:
                p.participant.vars["main_carrying_payoff"] += p.participant.vars["dictator_payoff"]
            elif p.id_in_group == 2:
                p.participant.vars["main_carrying_payoff"] += p.participant.vars["dictator_payoff"]


class Player(BasePlayer):
    keep = models.IntegerField()
    real_effort_dictator_endowment = models.IntegerField(initial=0)
