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

    def set_choices(self):
        choices = []
        menu_a = ["menu_a_q1", "menu_a_q2", "menu_a_q3", "menu_a_q4", "menu_a_q5", "menu_a_q6"]
        menu_b = ["menu_b_q1", "menu_b_q2", "menu_b_q3", "menu_b_q4", "menu_b_q5", "menu_b_q6"]
        menu_c = ["menu_c_q1", "menu_c_q2", "menu_c_q3", "menu_c_q4", "menu_c_q5", "menu_c_q6"]
        menu_d = ["menu_d_q1", "menu_d_q2", "menu_d_q3", "menu_d_q4", "menu_d_q5", "menu_d_q6"]

        choice_a = random.choice(menu_a)
        choice_b = random.choice(menu_b)
        choice_c = random.choice(menu_c)
        choice_d = random.choice(menu_d)

        choices.append(choice_a)
        choices.append(choice_b)
        choices.append(choice_c)
        choices.append(choice_d)

        return choices

    def select_payoff(self):
        points = 0
        for choice in self.set_choices():
            menu_option = getattr(self, str(choice))
            if "now" in menu_option:
                now_option = int(str(menu_option).split("_")[0])
                points += now_option
                # self.participant.vars["game_payoff"]["time_preference"] = now_option
            else:
                points = 0
                self.participant.vars["chosen_future"].append(menu_option)
        self.payoff = points
        self.participant.vars["carrying_payoff"] = points
        self.participant.vars["game_payoff"]["time_preference"] = points


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

    menu_a_q1 = models.CharField(choices=q1_a, verbose_name="", widget=widgets.RadioSelect())
    menu_a_q2 = models.CharField(choices=q2_a, verbose_name="", widget=widgets.RadioSelect())
    menu_a_q3 = models.CharField(choices=q3_a, verbose_name="", widget=widgets.RadioSelect())
    menu_a_q4 = models.CharField(choices=q4_a, verbose_name="", widget=widgets.RadioSelect())
    menu_a_q5 = models.CharField(choices=q5_a, verbose_name="", widget=widgets.RadioSelect())
    menu_a_q6 = models.CharField(choices=q6_a, verbose_name="", widget=widgets.RadioSelect())

    menu_b_q1 = models.CharField(choices=q1_b, verbose_name="", widget=widgets.RadioSelect())
    menu_b_q2 = models.CharField(choices=q2_b, verbose_name="", widget=widgets.RadioSelect())
    menu_b_q3 = models.CharField(choices=q3_b, verbose_name="", widget=widgets.RadioSelect())
    menu_b_q4 = models.CharField(choices=q4_b, verbose_name="", widget=widgets.RadioSelect())
    menu_b_q5 = models.CharField(choices=q5_b, verbose_name="", widget=widgets.RadioSelect())
    menu_b_q6 = models.CharField(choices=q6_b, verbose_name="", widget=widgets.RadioSelect())

    menu_c_q1 = models.CharField(choices=q1_c, verbose_name="", widget=widgets.RadioSelect())
    menu_c_q2 = models.CharField(choices=q2_c, verbose_name="", widget=widgets.RadioSelect())
    menu_c_q3 = models.CharField(choices=q3_c, verbose_name="", widget=widgets.RadioSelect())
    menu_c_q4 = models.CharField(choices=q4_c, verbose_name="", widget=widgets.RadioSelect())
    menu_c_q5 = models.CharField(choices=q5_c, verbose_name="", widget=widgets.RadioSelect())
    menu_c_q6 = models.CharField(choices=q6_c, verbose_name="", widget=widgets.RadioSelect())

    menu_d_q1 = models.CharField(choices=q1_d, verbose_name="", widget=widgets.RadioSelect())
    menu_d_q2 = models.CharField(choices=q2_d, verbose_name="", widget=widgets.RadioSelect())
    menu_d_q3 = models.CharField(choices=q3_d, verbose_name="", widget=widgets.RadioSelect())
    menu_d_q4 = models.CharField(choices=q4_d, verbose_name="", widget=widgets.RadioSelect())
    menu_d_q5 = models.CharField(choices=q5_d, verbose_name="", widget=widgets.RadioSelect())
    menu_d_q6 = models.CharField(choices=q6_d, verbose_name="", widget=widgets.RadioSelect())
