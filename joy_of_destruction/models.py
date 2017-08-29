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

author = 'Your name here'

doc = """
Two participants are paired and both completed the Raven's matrices
and earned some airtime vouchers. They are given opportunity to destroy some of
your partner's vouchers. This will happen anonymously, so that your choices will never be
revealed to any other participant.
"""


class Constants(BaseConstants):
    name_in_url = 'joy_of_destruction'
    players_per_group = 2
    num_rounds = 1
    vouchers = 6
    points = 0


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    def set_payoffs(self):
        p1, p2 = self.get_player_by_id(1), self.get_player_by_id(2)
        p1.points = Constants.vouchers - p1.destroyed
        p2.points = Constants.vouchers - p2.destroyed

        p1.participant.vars["ravens_points"] += p1.points
        p2.participant.vars["ravens_points"] += p2.points


class Player(BasePlayer):

    def set_player_destroyed(self):

        points = self.get_others_in_group()[0].participant.vars["ravens_points"]
        if points <= self.amount_to_destroy:
            self.destroyed = self.amount_to_destroy
        else:
            self.destroyed = self.amount_to_destroy + random.randrange(1, points - self.amount_to_destroy + 1)

    amount_to_destroy = models.IntegerField(min=0)

    destroyed = models.IntegerField(default=0)

    points = models.IntegerField(default=0)

