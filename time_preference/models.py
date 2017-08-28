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
            p.participant.vars["chosen_future"] = None


class Group(BaseGroup):
    def set_payoffs(self):
        for p in self.get_players():
            q1_or_q2_q3_q4 = random.choice(['q1', 'q2', 'q3', 'q4'])
            if q1_or_q2_q3_q4 == 'q1':
                x = random.choice([p.q11, p.q12, p.q13, p.q14, p.q15, p.q16])
                select_payoff(p, x)
                p.participant.vars["carrying_payoff"] += p.payoff

            elif q1_or_q2_q3_q4 == 'q2':
                x = random.choice([p.q21, p.q22, p.q23, p.q24, p.q25, p.q26])
                select_payoff(p, x)
                p.participant.vars["carrying_payoff"] += p.payoff

            elif q1_or_q2_q3_q4 == 'q3':
                x = random.choice([p.q31, p.q32, p.q33, p.q34, p.q35, p.q36])
                select_payoff(p, x)
                p.participant.vars["carrying_payoff"] += p.payoff

            elif q1_or_q2_q3_q4 == 'q4':
                x = random.choice([p.q41, p.q42, p.q43, p.q44, p.q45, p.q46])
                select_payoff(p, x)
                p.participant.vars["carrying_payoff"] += p.payoff

            else:
                p.payoff = 0


def select_payoff(player, x):
    if "now" in str(x):
        x = int(str(x).split("_")[0])
        player.payoff = x
        player.participant.vars["game_payoff"]["time_preference"] = x
    else:
        x = int(str(x).split("_")[0])
        player.payoff = 0
        player.chosen_future = x
        player.participant.vars["chosen_future"] = x


class Player(BasePlayer):
    q1_a = (('840_now', 'A: 840 Tokens'), ('0_future', 'B: 0 Tokens'),)
    q2_a = (('672_now', 'A: 672 Tokens'), ('240_future', 'B: 240 Tokes'),)
    q3_a = (('504_now', 'A: 504 Tokens'), ('480_future', 'B: 480 Tokens'),)
    q4_a = (('336_now', 'A: 336 Tokens'), ('720_future', 'B: 720 Tokens'),)
    q5_a = (('168_now', 'A: 168 Tokens'), ('960_future', 'B: 960 Tokens'),)
    q6_a = (('0_now', 'A: 0 Tokens'), ('1200_future', 'B: 1200 Tokens'),)

    q1_b = (('1020_now', 'A: 1020 Tokens'), ('0_future', 'B: 0 Tokens'),)
    q2_b = (('836_now', 'A: 836 Tokens'), ('184_future', 'B: 184 Tokens'),)
    q3_b = (('632_now', 'A: 632 Tokens'), ('388_future', 'B: 388 Tokens'),)
    q4_b = (('428_now', 'A: 428 Tokens'), ('592_future', 'B: 592 Tokens'),)
    q5_b = (('224_now', 'A: 224 Tokens'), ('796_future', 'B: 796 Tokens'),)
    q6_b = (('0_now', 'A: 0 Tokens'), ('1020_future', 'B: 1020 Tokens'),)

    q1_c = (('840_now', 'A: 840 Tokens'), ('0_future', 'B: 0 Tokens'),)
    q2_c = (('672_now', 'A: 672 Tokens'), ('240_future', 'B: 240 Tokes'),)
    q3_c = (('504_now', 'A: 504 Tokens'), ('480_future', 'B: 480 Tokens'),)
    q4_c = (('336_now', 'A: 336 Tokens'), ('720_future', 'B: 720 Tokens'),)
    q5_c = (('168_now', 'A: 168 Tokens'), ('960_future', 'B: 960 Tokens'),)
    q6_c = (('0_now', 'A: 0 Tokens'), ('1200_future', 'B: 1200 Tokens'),)

    q1_d = (('1020_now', 'A: 1020 Tokens'), ('0_future', 'B: 0 Tokens'),)
    q2_d = (('836_now', 'A: 836 Tokens'), ('184_future', 'B: 184 Tokens'),)
    q3_d = (('632_now', 'A: 632 Tokens'), ('388_future', 'B: 388 Tokens'),)
    q4_d = (('428_now', 'A: 428 Tokens'), ('592_future', 'B: 592 Tokens'),)
    q5_d = (('224_now', 'A: 224 Tokens'), ('796_future', 'B: 796 Tokens'),)
    q6_d = (('0_now', 'A: 0 Tokens'), ('1020_future', 'B: 1020 Tokens'),)

    q11 = models.CharField(choices=q1_a, verbose_name="", widget=widgets.RadioSelectHorizontal())
    q12 = models.CharField(choices=q2_a, verbose_name="", widget=widgets.RadioSelectHorizontal())
    q13 = models.CharField(choices=q3_a, verbose_name="", widget=widgets.RadioSelectHorizontal())
    q14 = models.CharField(choices=q4_a, verbose_name="", widget=widgets.RadioSelectHorizontal())
    q15 = models.CharField(choices=q5_a, verbose_name="", widget=widgets.RadioSelectHorizontal())
    q16 = models.CharField(choices=q6_a, verbose_name="", widget=widgets.RadioSelectHorizontal())

    q21 = models.CharField(choices=q1_b, verbose_name="", widget=widgets.RadioSelectHorizontal())
    q22 = models.CharField(choices=q2_b, verbose_name="", widget=widgets.RadioSelectHorizontal())
    q23 = models.CharField(choices=q3_b, verbose_name="", widget=widgets.RadioSelectHorizontal())
    q24 = models.CharField(choices=q4_b, verbose_name="", widget=widgets.RadioSelectHorizontal())
    q25 = models.CharField(choices=q5_b, verbose_name="", widget=widgets.RadioSelectHorizontal())
    q26 = models.CharField(choices=q6_b, verbose_name="", widget=widgets.RadioSelectHorizontal())

    q31 = models.CharField(choices=q1_c, verbose_name="", widget=widgets.RadioSelectHorizontal())
    q32 = models.CharField(choices=q2_c, verbose_name="", widget=widgets.RadioSelectHorizontal())
    q33 = models.CharField(choices=q3_c, verbose_name="", widget=widgets.RadioSelectHorizontal())
    q34 = models.CharField(choices=q4_c, verbose_name="", widget=widgets.RadioSelectHorizontal())
    q35 = models.CharField(choices=q5_c, verbose_name="", widget=widgets.RadioSelectHorizontal())
    q36 = models.CharField(choices=q6_c, verbose_name="", widget=widgets.RadioSelectHorizontal())

    q41 = models.CharField(choices=q1_d, verbose_name="", widget=widgets.RadioSelectHorizontal())
    q42 = models.CharField(choices=q2_d, verbose_name="", widget=widgets.RadioSelectHorizontal())
    q43 = models.CharField(choices=q3_d, verbose_name="", widget=widgets.RadioSelectHorizontal())
    q44 = models.CharField(choices=q4_d, verbose_name="", widget=widgets.RadioSelectHorizontal())
    q45 = models.CharField(choices=q5_d, verbose_name="", widget=widgets.RadioSelectHorizontal())
    q46 = models.CharField(choices=q6_d, verbose_name="", widget=widgets.RadioSelectHorizontal())

    chosen_future = models.IntegerField()
