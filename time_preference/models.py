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
    def before_session_starts(self):
        for p in self.get_players():
            p.participant.vars["chosen_future"] = list()


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    def set_choice(self):
        menus = ["menu_a", "menu_b", "menu_c", "menu_d"]
        return random.choice(menus)

    def select_payoff(self):
        points = 0
        menu_option = getattr(self, str(self.set_choice()))

        now, future = str(menu_option).split('-')
        if "now" in now:
            self.payment_now = int(str(now).split("_")[0])
            points += int(str(now).split("_")[0])
        else:
            points = 0
            self.payment_future = int(str(future).split("_")[0])
            self.participant.vars["chosen_future"].append(menu_option)

        self.payoff = points
        self.participant.vars["carrying_payoff"] = points
        self.participant.vars["game_payoff"]["time_preference"] = points
        self.time_preference_points = points

    q1 = [
        ('840_now-0_future', 'A: 840 Tokens B: 0 Tokens'),
        ('672_now-240_future', 'A: 672 Tokens B: 240 Tokes'),
        ('504_now-504_future', 'A: 504 Tokens B: 480 Tokens'),
        ('336_now-720_future', 'A: 336 Tokens B: 720 Tokens'),
        ('168_now-960_future', 'A: 168 Tokens B: 960 Tokens'),
        ('0_now-1200_future', 'A: 0 Tokens B: 1200 Tokens'),
    ]

    q2 = [
        ('1020_now-0_future', 'A: 1020 Tokens B: 0 Tokens'),
        ('836_now-184_future', 'A: 836 Tokens B: 184 Tokens'),
        ('632_now-388_future', 'A: 632 Tokens B: 388 Tokens'),
        ('428_now-592_future', 'A: 428 Tokens B: 592 Tokens'),
        ('224_now-796_future', 'A: 224 Tokens B: 796 Tokens'),
        ('0_now-1020_future', 'A: 0 Tokens B: 1020 Tokens'),
    ]

    q3 = [
        ('840_now-0_future', 'A: 840 Tokens B: 0 Tokens'),
        ('672_now-240_future', 'A: 672 Tokens B: 240 Tokes'),
        ('504_now-480_future', 'A: 504 Tokens B: 480 Tokens'),
        ('336_now-720_future', 'A: 336 Tokens B: 720 Tokens'),
        ('168_now-960_future', 'A: 168 Tokens B: 960 Tokens'),
        ('0_now-1200_future', 'A: 0 Tokens B: 1200 Tokens'),
    ]

    q4 = [
        ('1020_now-0_future', 'A: 1020 Tokens B: 0 Tokens'),
        ('836_now-184_future', 'A: 836 Tokens B: 184 Tokens'),
        ('632_now-388_future', 'A: 632 Tokens B: 388 Tokens'),
        ('428_now-592_future', 'A: 428 Tokens B: 592 Tokens'),
        ('224_now-796_future', 'A: 224 Tokens B: 796 Tokens'),
        ('0_now-1020_future', 'A: 0 Tokens B: 1020 Tokens'),
    ]

    menu_a = models.CharField(choices=q1, verbose_name="", widget=widgets.RadioSelect())

    menu_b = models.CharField(choices=q2, verbose_name="", widget=widgets.RadioSelect())

    menu_c = models.CharField(choices=q3, verbose_name="", widget=widgets.RadioSelect())

    menu_d = models.CharField(choices=q4, verbose_name="", widget=widgets.RadioSelect())

    payment_future = models.IntegerField(initial=0)

    payment_now = models.IntegerField(initial=0)

    time_preference_points = models.IntegerField(initial=0)
