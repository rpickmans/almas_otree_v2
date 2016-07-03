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
This game will serve two purposes. First, it enables us to identify patience, and the effect
of temperature on patience. Second, it enables us to identify time inconsistency. We
will use the traditional protocol for eliciting so-called beta-delta preferences, namely
a price list with ditterent choices about timing of payments.
"""


class Constants(BaseConstants):
    name_in_url = 'time_preference'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def set_payoffs(self):
        for p in self.get_players():
            q1_or_q2 = random.choice(['q1', 'q2'])
            if q1_or_q2 == 'q1':
                p.payoff = random.choice([p.q11, p.q12, p.q13, p.q14, p.q15])
                p.participant.vars["carrying_payoff"] += p.payoff
            elif q1_or_q2 == 'q2':
                p.payoff = random.choice([p.q21, p.q22, p.q23, p.q24, p.q25, p.q26])
                p.participant.vars["carrying_payoff"] += p.payoff
            else:
                p.payoff = 0


class Player(BasePlayer):
    q11c = ((100, 'A: 100'),(100, 'B: 100'),)
    q12c = ((100, 'A: 100'),(120, 'B: 120'),)
    q13c = ((100, 'A: 100'),(140, 'B: 140'),)
    q14c = ((100, 'A: 100'),(160, 'B: 160'),)
    q15c = ((100, 'A: 100'),(180, 'B: 180'),)
    q16c = ((100, 'A: 100'),(200, 'B: 200'),)

    q11 = models.IntegerField(choices = q11c, verbose_name = "", widget = widgets.RadioSelectHorizontal())
    q12 = models.IntegerField(choices = q12c, verbose_name = "", widget = widgets.RadioSelectHorizontal())
    q13 = models.IntegerField(choices = q13c, verbose_name = "", widget = widgets.RadioSelectHorizontal())
    q14 = models.IntegerField(choices = q14c, verbose_name = "", widget = widgets.RadioSelectHorizontal())
    q15 = models.IntegerField(choices = q15c, verbose_name = "", widget = widgets.RadioSelectHorizontal())
    q16 = models.IntegerField(choices = q16c, verbose_name = "", widget = widgets.RadioSelectHorizontal())

    q21 = models.IntegerField(choices = q11c, verbose_name = "", widget = widgets.RadioSelectHorizontal())
    q22 = models.IntegerField(choices = q12c, verbose_name = "", widget = widgets.RadioSelectHorizontal())
    q23 = models.IntegerField(choices = q13c, verbose_name = "", widget = widgets.RadioSelectHorizontal())
    q24 = models.IntegerField(choices = q14c, verbose_name = "", widget = widgets.RadioSelectHorizontal())
    q25 = models.IntegerField(choices = q15c, verbose_name = "", widget = widgets.RadioSelectHorizontal())
    q26 = models.IntegerField(choices = q16c, verbose_name = "", widget = widgets.RadioSelectHorizontal())


