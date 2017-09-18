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
        menu = (random.choice(menus),)
        return menu[0]

    def select_menu_a_b(self, str_choice):
        menu_option = getattr(self, str(str_choice))
        if menu_option:
            now, future = str(menu_option).split('-')
            self.payment_today_ab = int(str(now).split("_")[0])
            self.payment_3weeks_ab = int(str(future).split("_")[0])
            self.participant.vars["menu_a_b_today"] = {"today": int(str(now).split("_")[0])}
            self.participant.vars["menu_a_b_3weeks"] = {"weeks3": int(str(future).split("_")[0])}

    def select_menu_c_d(self, str_choice):
        menu_option = getattr(self, str(str_choice))
        if menu_option:
            three_weeks, seven_weeks = str(menu_option).split('-')
            self.payment_3weeks_cd = int(str(three_weeks).split("_")[0])
            self.payment_7weeks_cd = int(str(seven_weeks).split("_")[0])
            self.participant.vars["menu_c_d_3weeks"] = {"weeks3": int(str(three_weeks).split("_")[0])}
            self.participant.vars["menu_c_d_7weeks"] = {"weeks7": int(str(seven_weeks).split("_")[0])}

    def set_preference(self):
        choice = self.set_choice()
        if choice in ["menu_a", "menu_b"]:
            self.select_menu_a_b(choice)

        elif choice in ["menu_c", "menu_d"]:
            self.select_menu_c_d(choice)

    def set_payoff(self):

        self.payoff = self.payment_today_ab
        self.participant.vars["carrying_payoff"] = self.payment_today_ab
        self.participant.vars["game_payoff"]["time_preference"] = self.payment_today_ab
        self.time_preference_points = self.payment_today_ab

    q1 = [
        ('840_now-0_3weeks', '840 Tokens Today AND 0 Tokens in 3 Weeks'),
        ('672_now-240_3weeks', '672 Tokens Today AND 240 Tokens in 3 Weeks'),
        ('504_now-480_3weeks', '504 Tokens Today AND 480 Tokens in 3 Weeks'),
        ('336_now-720_3weeks', '336 Tokens Today AND 720 Tokens in 3 Weeks'),
        ('168_now-960_3weeks', '168 Tokens Today AND 960 Tokens in 3 Weeks'),
        ('0_now-1200_3weeks', '0 Tokens Today AND 1200 Tokens in 3 Weeks'),
    ]

    q2 = [
        ('1020_now-0_3weeks', '1020 Tokens Today AND 0 Tokens in 3 Weeks'),
        ('836_now-184_3weeks', '836 Tokens Today AND 184 Tokens in 3 Weeks'),
        ('632_now-388_3weeks', '632 Tokens Today AND 388 Tokens in 3 Weeks'),
        ('428_now-592_3weeks', '428 Tokens Today AND 592 Tokens in 3 Weeks'),
        ('224_now-796_3weeks', '224 Tokens Today AND 796 Tokens in 3 Weeks'),
        ('0_now-1020_3weeks', '0 Tokens Today And 1020 Tokens in 3 Weeks'),
    ]

    q3 = [
        ('840_3weeks-0_7weeks', '840 Tokens in 3 Weeks AND 0 Tokens in 7 Weeks'),
        ('672_3weeks-240_7weeks', '672 Tokens in 3 Weeks AND 240 Tokens in 7 Weeks'),
        ('504_3weeks-480_7weeks', '504 Tokens in 3 Weeks AND 480 Tokens in 7 Weeks'),
        ('336_3weeks-720_7weeks', '336 Tokens in 3 Weeks AND 720 Tokens in 7 Weeks'),
        ('168_3weeks-960_7weeks', '168 Tokens in 3 Weeks AND 960 Tokens in 7 Weeks'),
        ('0_3weeks-1200_7weeks', '0 Tokens in 3 Weeks AND 1200 Tokens in 7 Weeks'),
    ]

    q4 = [
        ('1020_3weeks-0_7weeks', '1020 Tokens in 3 Weeks AND 0 Tokens in 7 Weeks'),
        ('836_3weeks-184_7weeks', '836 Tokens in 3 Weeks AND 184 Tokens in 7 Weeks'),
        ('632_3weeks-388_7weeks', '632 Tokens in 3 Weeks AND 388 Tokens in 7 Weeks'),
        ('428_3weeks-592_7weeks', '428 Tokens in 3 Weeks AND 592 Tokens in 7 Weeks'),
        ('224_3weeks-796_7weeks', '224 Tokens in 3 Weeks AND 796 Tokens in 7 Weeks'),
        ('0_3weeks-1020_7weeks', '0 Tokens in 3 Weeks AND 1020 Tokens in 7 Weeks'),
    ]

    menu_a = models.CharField(choices=q1, verbose_name="", widget=widgets.RadioSelect())

    menu_b = models.CharField(choices=q2, verbose_name="", widget=widgets.RadioSelect())

    menu_c = models.CharField(choices=q3, verbose_name="", widget=widgets.RadioSelect())

    menu_d = models.CharField(choices=q4, verbose_name="", widget=widgets.RadioSelect())

    payment_today_ab = models.IntegerField(initial=0)

    payment_3weeks_ab = models.IntegerField(initial=0)

    payment_3weeks_cd = models.IntegerField(initial=0)

    payment_7weeks_cd = models.IntegerField(initial=0)

    time_preference_points = models.IntegerField(initial=0)
