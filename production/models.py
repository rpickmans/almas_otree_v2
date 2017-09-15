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
In this Game, You will earn money from conducting a task.
"""


class Constants(BaseConstants):
    name_in_url = 'production'
    players_per_group = 3
    num_rounds = 1


class Subsession(BaseSubsession):
    def before_session_starts(self):
        for g in self.get_players():
            g.participant.vars["game_payoff"] = dict()
            g.participant.vars["carrying_payoff"] = 0
            g.pr_rsv_1 = random.randint(1, 100)
            g.pr_rsv_2 = random.randint(1, 100)

            g.rsv_1 = random.randint(1, 100)
            g.rsv_2 = random.randint(1, 100)
            g.rsv_3 = random.randint(1, 100)
            g.rsv_4 = random.randint(1, 100)
            g.rsv_5 = random.randint(1, 100)
            g.rsv_6 = random.randint(1, 100)
            g.rsv_7 = random.randint(1, 100)
            g.rsv_8 = random.randint(1, 100)
            g.rsv_9 = random.randint(1, 100)
            g.rsv_10 = random.randint(1, 100)
            g.rsv_11 = random.randint(1, 100)
            g.rsv_12 = random.randint(1, 100)
            g.rsv_13 = random.randint(1, 100)
            g.rsv_14 = random.randint(1, 100)
            g.rsv_15 = random.randint(1, 100)
            g.rsv_16 = random.randint(1, 100)
            g.rsv_17 = random.randint(1, 100)
            g.rsv_18 = random.randint(1, 100)
            g.rsv_19 = random.randint(1, 100)
            g.rsv_20 = random.randint(1, 100)
            g.rsv_21 = random.randint(1, 100)
            g.rsv_22 = random.randint(1, 100)
            g.rsv_23 = random.randint(1, 100)
            g.rsv_24 = random.randint(1, 100)
            g.rsv_25 = random.randint(1, 100)
            g.rsv_26= random.randint(1, 100)
            g.rsv_27 = random.randint(1, 100)
            g.rsv_28 = random.randint(1, 100)
            g.rsv_29 = random.randint(1, 100)
            g.rsv_30 = random.randint(1, 100)
            g.rsv_31 = random.randint(1, 100)
            g.rsv_32 = random.randint(1, 100)
            g.rsv_33 = random.randint(1, 100)
            g.rsv_34 = random.randint(1, 100)
            g.rsv_35 = random.randint(1, 100)
            g.rsv_36 = random.randint(1, 100)
            g.rsv_37 = random.randint(1, 100)
            g.rsv_38 = random.randint(1, 100)
            g.rsv_39 = random.randint(1, 100)
            g.rsv_40 = random.randint(1, 100)
            g.rsv_41 = random.randint(1, 100)
            g.rsv_42 = random.randint(1, 100)
            g.rsv_43 = random.randint(1, 100)
            g.rsv_44 = random.randint(1, 100)
            g.rsv_45 = random.randint(1, 100)
            g.rsv_46 = random.randint(1, 100)
            g.rsv_47 = random.randint(1, 100)
            g.rsv_48 = random.randint(1, 100)
            g.rsv_49 = random.randint(1, 100)
            g.rsv_50 = random.randint(1, 100)
            g.rsv_51 = random.randint(1, 100)
            g.rsv_52 = random.randint(1, 100)
            g.rsv_53 = random.randint(1, 100)
            g.rsv_54 = random.randint(1, 100)
            g.rsv_55 = random.randint(1, 100)
            g.rsv_56 = random.randint(1, 100)
            g.rsv_57 = random.randint(1, 100)
            g.rsv_58 = random.randint(1, 100)
            g.rsv_59 = random.randint(1, 100)
            g.rsv_60 = random.randint(1, 100)


class Group(BaseGroup):
    def set_correct_sliders(self):
        for p in self.get_players():
            correct = 0
            if p.psv_1 == p.rsv_1:
                correct += 1

            if p.psv_2 == p.rsv_2:
                correct += 1

            if p.psv_3 == p.rsv_3:
                correct += 1

            if p.psv_4 == p.rsv_4:
                correct += 1

            if p.psv_5 == p.rsv_5:
                correct += 1

            if p.psv_6 == p.rsv_6:
                correct += 1

            if p.psv_7 == p.rsv_7:
                correct += 1

            if p.psv_8 == p.rsv_8:
                correct += 1

            if p.psv_9 == p.rsv_9:
                correct += 1

            if p.psv_10 == p.rsv_10:
                correct += 1

            if p.psv_11 == p.rsv_11:
                correct += 1

            if p.psv_12 == p.rsv_12:
                correct += 1

            if p.psv_13 == p.rsv_13:
                correct += 1

            if p.psv_14 == p.rsv_14:
                correct += 1

            if p.psv_15 == p.rsv_15:
                correct += 1

            if p.psv_16 == p.rsv_16:
                correct += 1

            if p.psv_17 == p.rsv_17:
                correct += 1

            if p.psv_18 == p.rsv_18:
                correct += 1

            if p.psv_19 == p.rsv_19:
                correct += 1

            if p.psv_20 == p.rsv_20:
                correct += 1

            if p.psv_21 == p.rsv_21:
                correct += 1

            if p.psv_22 == p.rsv_22:
                correct += 1

            if p.psv_23 == p.rsv_23:
                correct += 1

            if p.psv_24 == p.rsv_24:
                correct += 1

            if p.psv_25 == p.rsv_25:
                correct += 1

            if p.psv_26 == p.rsv_26:
                correct += 1

            if p.psv_27 == p.rsv_27:
                correct += 1

            if p.psv_28 == p.rsv_28:
                correct += 1

            if p.psv_29 == p.rsv_29:
                correct += 1

            if p.psv_30 == p.rsv_30:
                correct += 1

            if p.psv_31 == p.rsv_31:
                correct += 1

            if p.psv_32 == p.rsv_32:
                correct += 1

            if p.psv_33 == p.rsv_33:
                correct += 1

            if p.psv_34 == p.rsv_34:
                correct += 1

            if p.psv_35 == p.rsv_35:
                correct += 1

            if p.psv_36 == p.rsv_36:
                correct += 1

            if p.psv_37 == p.rsv_37:
                correct += 1

            if p.psv_38 == p.rsv_38:
                correct += 1

            if p.psv_39 == p.rsv_39:
                correct += 1

            if p.psv_40 == p.rsv_40:
                correct += 1

            if p.psv_41 == p.rsv_41:
                correct += 1

            if p.psv_42 == p.rsv_42:
                correct += 1

            if p.psv_43 == p.rsv_43:
                correct += 1

            if p.psv_44 == p.rsv_44:
                correct += 1

            if p.psv_45 == p.rsv_45:
                correct += 1

            if p.psv_46 == p.rsv_46:
                correct += 1

            if p.psv_47 == p.rsv_47:
                correct += 1

            if p.psv_48 == p.rsv_48:
                correct += 1

            if p.psv_49 == p.rsv_49:
                correct += 1

            if p.psv_50 == p.rsv_50:
                correct += 1

            if p.psv_51 == p.rsv_51:
                correct += 1

            if p.psv_52 == p.rsv_52:
                correct += 1

            if p.psv_53 == p.rsv_53:
                correct += 1

            if p.psv_54 == p.rsv_54:
                correct += 1

            if p.psv_55 == p.rsv_55:
                correct += 1

            if p.psv_56 == p.rsv_56:
                correct += 1

            if p.psv_57 == p.rsv_57:
                correct += 1

            if p.psv_58 == p.rsv_58:
                correct += 1

            if p.psv_59 == p.rsv_59:
                correct += 1

            if p.psv_60 == p.rsv_60:
                correct += 1

            p.correct_sliders = correct
            p.participant.vars["total_correct"] = correct

    def set_sliders_total(self):
        for p in self.get_players():
            p.participant.vars["game_payoff"]["production"] = p.correct_sliders


class Player(BasePlayer):
    # pratice sliders
    pr_sv_1 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    pr_sv_2 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))

    # input from player
    psv_1 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_2 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_3 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_4 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_5 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_6 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_7 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_8 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_9 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_10 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_11 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_12 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_13 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_14 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_15 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_16 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_17 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_18 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_19 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_20 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_21 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_22 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_23 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_24 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_25 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_26 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_27 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_28 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_29 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_30 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_31 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_32 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_33 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_34 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_35 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_36 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_37 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_38 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_39 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_40 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_41 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_42 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_43 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_44 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_45 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_46 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_47 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_48 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_49 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_50 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_51 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_52 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_53 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_54 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_55 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_56 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_57 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_58 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_59 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    psv_60 = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))

    # practice random value
    pr_rsv_1 = models.IntegerField()
    pr_rsv_2 = models.IntegerField()

    # correct values
    rsv_1 = models.IntegerField()
    rsv_2 = models.IntegerField()
    rsv_3 = models.IntegerField()
    rsv_4 = models.IntegerField()
    rsv_5 = models.IntegerField()
    rsv_6 = models.IntegerField()
    rsv_7 = models.IntegerField()
    rsv_8 = models.IntegerField()
    rsv_9 = models.IntegerField()
    rsv_10 = models.IntegerField()
    rsv_11 = models.IntegerField()
    rsv_12 = models.IntegerField()
    rsv_13 = models.IntegerField()
    rsv_14 = models.IntegerField()
    rsv_15 = models.IntegerField()
    rsv_16 = models.IntegerField()
    rsv_17 = models.IntegerField()
    rsv_18 = models.IntegerField()
    rsv_19 = models.IntegerField()
    rsv_20 = models.IntegerField()
    rsv_21 = models.IntegerField()
    rsv_22 = models.IntegerField()
    rsv_23 = models.IntegerField()
    rsv_24 = models.IntegerField()
    rsv_25 = models.IntegerField()
    rsv_26 = models.IntegerField()
    rsv_27 = models.IntegerField()
    rsv_28 = models.IntegerField()
    rsv_29 = models.IntegerField()
    rsv_30 = models.IntegerField()
    rsv_31 = models.IntegerField()
    rsv_32 = models.IntegerField()
    rsv_33 = models.IntegerField()
    rsv_34 = models.IntegerField()
    rsv_35 = models.IntegerField()
    rsv_36 = models.IntegerField()
    rsv_37 = models.IntegerField()
    rsv_38 = models.IntegerField()
    rsv_39 = models.IntegerField()
    rsv_40 = models.IntegerField()
    rsv_41 = models.IntegerField()
    rsv_42 = models.IntegerField()
    rsv_43 = models.IntegerField()
    rsv_44 = models.IntegerField()
    rsv_45 = models.IntegerField()
    rsv_46 = models.IntegerField()
    rsv_47 = models.IntegerField()
    rsv_48 = models.IntegerField()
    rsv_49 = models.IntegerField()
    rsv_50 = models.IntegerField()
    rsv_51 = models.IntegerField()
    rsv_52 = models.IntegerField()
    rsv_53 = models.IntegerField()
    rsv_54 = models.IntegerField()
    rsv_55 = models.IntegerField()
    rsv_56 = models.IntegerField()
    rsv_57 = models.IntegerField()
    rsv_58 = models.IntegerField()
    rsv_59 = models.IntegerField()
    rsv_60 = models.IntegerField()

    correct_sliders = models.IntegerField()
