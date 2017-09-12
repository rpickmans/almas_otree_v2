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
            g.practice_random_slider_value_one = random.randint(1, 100)
            g.practice_random_slider_value_two = random.randint(1, 100)


            g.random_slider_value_one = random.randint(1, 100)
            g.random_slider_value_two = random.randint(1, 100)
            g.random_slider_value_three = random.randint(1, 100)
            g.random_slider_value_four = random.randint(1, 100)
            g.random_slider_value_five = random.randint(1, 100)
            g.random_slider_value_six = random.randint(1, 100)
            g.random_slider_value_seven = random.randint(1, 100)
            g.random_slider_value_eight = random.randint(1, 100)
            g.random_slider_value_nine = random.randint(1, 100)
            g.random_slider_value_ten = random.randint(1, 100)
            g.random_slider_value_eleven = random.randint(1, 100)
            g.random_slider_value_twelve = random.randint(1, 100)
            g.random_slider_value_thirteen = random.randint(1, 100)
            g.random_slider_value_fourteen = random.randint(1, 100)
            g.random_slider_value_fifteen = random.randint(1, 100)
            g.random_slider_value_sixteen = random.randint(1, 100)
            g.random_slider_value_seventeen = random.randint(1, 100)
            g.random_slider_value_eighteen = random.randint(1, 100)
            g.random_slider_value_nineteen = random.randint(1, 100)
            g.random_slider_value_twenty = random.randint(1, 100)
            g.random_slider_value_twentyone = random.randint(1, 100)
            g.random_slider_value_twentytwo = random.randint(1, 100)
            g.random_slider_value_twentythree = random.randint(1, 100)
            g.random_slider_value_twentyfour = random.randint(1, 100)
            g.random_slider_value_twentyfive = random.randint(1, 100)
            g.random_slider_value_twentysix = random.randint(1, 100)
            g.random_slider_value_twentyseven = random.randint(1, 100)
            g.random_slider_value_twentyeight = random.randint(1, 100)
            g.random_slider_value_twentynine = random.randint(1, 100)
            g.random_slider_value_thirty = random.randint(1, 100)
            g.random_slider_value_thirtyone = random.randint(1, 100)
            g.random_slider_value_thirtytwo = random.randint(1, 100)
            g.random_slider_value_thirtythree = random.randint(1, 100)
            g.random_slider_value_thirtyfour = random.randint(1, 100)
            g.random_slider_value_thirtyfive = random.randint(1, 100)
            g.random_slider_value_thirtysix = random.randint(1, 100)
            g.random_slider_value_thirtyseven = random.randint(1, 100)
            g.random_slider_value_thirtyeight = random.randint(1, 100)
            g.random_slider_value_thirtynine = random.randint(1, 100)
            g.random_slider_value_fourty = random.randint(1, 100)
            g.random_slider_value_fourtyone = random.randint(1, 100)
            g.random_slider_value_fourtytwo = random.randint(1, 100)
            g.random_slider_value_fourtythree = random.randint(1, 100)
            g.random_slider_value_fourtyfour = random.randint(1, 100)
            g.random_slider_value_fourtyfive = random.randint(1, 100)
            g.random_slider_value_fourtysix = random.randint(1, 100)
            g.random_slider_value_fourtyseven = random.randint(1, 100)
            g.random_slider_value_fourtyeight = random.randint(1, 100)
            g.random_slider_value_fourtynine = random.randint(1, 100)
            g.random_slider_value_fifty = random.randint(1, 100)
            g.random_slider_value_fiftyone = random.randint(1, 100)
            g.random_slider_value_fiftytwo = random.randint(1, 100)
            g.random_slider_value_fiftythree = random.randint(1, 100)
            g.random_slider_value_fiftyfour = random.randint(1, 100)
            g.random_slider_value_fiftyfive = random.randint(1, 100)
            g.random_slider_value_fiftysix = random.randint(1, 100)
            g.random_slider_value_fiftyseven = random.randint(1, 100)
            g.random_slider_value_fiftyeight = random.randint(1, 100)
            g.random_slider_value_fiftynine = random.randint(1, 100)
            g.random_slider_value_sixty = random.randint(1, 100)





class Group(BaseGroup):
    def set_correct_sliders(self):
        for p in self.get_players():
            correct = 0
            if p.player_slider_value_one == p.random_slider_value_one:
                correct += 1

            if p.player_slider_value_two == p.random_slider_value_two:
                correct += 1

            if p.player_slider_value_three == p.random_slider_value_three:
                correct += 1

            if p.player_slider_value_four == p.random_slider_value_four:
                correct += 1

            if p.player_slider_value_five == p.random_slider_value_five:
                correct += 1

            if p.player_slider_value_six == p.random_slider_value_six:
                correct += 1

            if p.player_slider_value_seven == p.random_slider_value_seven:
                correct += 1

            if p.player_slider_value_eight == p.random_slider_value_eight:
                correct += 1

            if p.player_slider_value_nine == p.random_slider_value_nine:
                correct += 1

            if p.player_slider_value_ten == p.random_slider_value_ten:
                correct += 1

            if p.player_slider_value_eleven == p.random_slider_value_eleven:
                correct += 1

            if p.player_slider_value_twelve == p.random_slider_value_twelve:
                correct += 1

            if p.player_slider_value_thirteen == p.random_slider_value_thirteen:
                correct += 1

            if p.player_slider_value_fourteen == p.random_slider_value_fourteen:
                correct += 1

            if p.player_slider_value_fifteen == p.random_slider_value_fifteen:
                correct += 1

            if p.player_slider_value_sixteen == p.random_slider_value_sixteen:
                correct += 1

            if p.player_slider_value_seventeen == p.random_slider_value_seventeen:
                correct += 1

            if p.player_slider_value_eighteen == p.random_slider_value_eighteen:
                correct += 1

            if p.player_slider_value_nineteen == p.random_slider_value_nineteen:
                correct += 1

            if p.player_slider_value_twenty == p.random_slider_value_twenty:
                correct += 1

            if p.player_slider_value_twentyone == p.random_slider_value_twentyone:
                correct += 1

            if p.player_slider_value_twentytwo == p.random_slider_value_twentytwo:
                correct += 1

            if p.player_slider_value_twentythree == p.random_slider_value_twentythree:
                correct += 1

            if p.player_slider_value_twentyfour == p.random_slider_value_twentyfour:
                correct += 1

            if p.player_slider_value_twentyfive == p.random_slider_value_twentyfive:
                correct += 1

            if p.player_slider_value_twentysix == p.random_slider_value_twentysix:
                correct += 1

            if p.player_slider_value_twentyseven == p.random_slider_value_twentyseven:
                correct += 1

            if p.player_slider_value_twentyeight == p.random_slider_value_twentyeight:
                correct += 1

            if p.player_slider_value_twentynine == p.random_slider_value_twentynine:
                correct += 1

            if p.player_slider_value_thirty == p.random_slider_value_thirty:
                correct += 1

            if p.player_slider_value_thirtyone == p.random_slider_value_thirtyone:
                correct += 1

            if p.player_slider_value_thirtytwo == p.random_slider_value_thirtytwo:
                correct += 1

            if p.player_slider_value_thirtythree == p.random_slider_value_thirtythree:
                correct += 1

            if p.player_slider_value_thirtyfour == p.random_slider_value_thirtyfour:
                correct += 1

            if p.player_slider_value_thirtyfive == p.random_slider_value_thirtyfive:
                correct += 1

            if p.player_slider_value_thirtysix == p.random_slider_value_thirtysix:
                correct += 1

            if p.player_slider_value_thirtyseven == p.random_slider_value_thirtyseven:
                correct += 1

            if p.player_slider_value_thirtyeight == p.random_slider_value_thirtyeight:
                correct += 1

            if p.player_slider_value_thirtynine == p.random_slider_value_thirtynine:
                correct += 1

            if p.player_slider_value_fourty == p.random_slider_value_fourty:
                correct += 1

            if p.player_slider_value_fourtyone == p.random_slider_value_fourtyone:
                correct += 1

            if p.player_slider_value_fourtytwo == p.random_slider_value_fourtytwo:
                correct += 1

            if p.player_slider_value_fourtythree == p.random_slider_value_fourtythree:
                correct += 1

            if p.player_slider_value_fourtyfour == p.random_slider_value_fourtyfour:
                correct += 1

            if p.player_slider_value_fourtyfive == p.random_slider_value_fourtyfive:
                correct += 1

            if p.player_slider_value_fourtysix == p.random_slider_value_fourtysix:
                correct += 1

            if p.player_slider_value_fourtyseven == p.random_slider_value_fourtyseven:
                correct += 1

            if p.player_slider_value_fourtyeight == p.random_slider_value_fourtyeight:
                correct += 1

            if p.player_slider_value_fourtynine == p.random_slider_value_fourtynine:
                correct += 1

            if p.player_slider_value_fifty == p.random_slider_value_fifty:
                correct += 1

            if p.player_slider_value_fiftyone == p.random_slider_value_fiftyone:
                correct += 1

            if p.player_slider_value_fiftytwo == p.random_slider_value_fiftytwo:
                correct += 1

            if p.player_slider_value_fiftythree == p.random_slider_value_fiftythree:
                correct += 1

            if p.player_slider_value_fiftyfour == p.random_slider_value_fiftyfour:
                correct += 1

            if p.player_slider_value_fiftyfive == p.random_slider_value_fiftyfive:
                correct += 1

            if p.player_slider_value_fiftysix == p.random_slider_value_fiftysix:
                correct += 1

            if p.player_slider_value_fiftyseven == p.random_slider_value_fiftyseven:
                correct += 1

            if p.player_slider_value_fiftyeight == p.random_slider_value_fiftyeight:
                correct += 1

            if p.player_slider_value_fiftynine == p.random_slider_value_fiftynine:
                correct += 1

            if p.player_slider_value_sixty == p.random_slider_value_sixty:
                correct += 1

            p.correct_sliders = correct
            p.participant.vars["total_correct"] = correct

    def set_sliders_total(self):
        for p in self.get_players():
            p.participant.vars["game_payoff"]["production"] = p.correct_sliders


class Player(BasePlayer):
    # pratice sliders
    practice_slider_value_one = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    practice_slider_value_two = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))

    # input from player
    player_slider_value_one = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_two = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_three = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_four = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_five = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_six = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_seven = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_eight = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_nine = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_ten = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_eleven = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_twelve = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_thirteen = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_fourteen = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_fifteen = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_sixteen = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_seventeen = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_eighteen = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_nineteen = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_twenty = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_twentyone = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_twentytwo = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_twentythree = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_twentyfour = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_twentyfive = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_twentysix = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_twentyseven = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_twentyeight = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_twentynine = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_thirty = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_thirtyone = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_thirtytwo = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_thirtythree = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_thirtyfour = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_thirtyfive = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_thirtysix = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_thirtyseven = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_thirtyeight = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_thirtynine = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_fourty = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_fourtyone = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_fourtytwo = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_fourtythree = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_fourtyfour = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_fourtyfive = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_fourtysix = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_fourtyseven = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_fourtyeight = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_fourtynine = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_fifty = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_fiftyone = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_fiftytwo = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_fiftythree = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_fiftyfour = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_fiftyfive = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_fiftysix = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_fiftyseven = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_fiftyeight = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_fiftynine = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_sixty = models.IntegerField(
        widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))

    # practice random value
    practice_random_slider_value_one = models.IntegerField()
    practice_random_slider_value_two = models.IntegerField()

    # correct values
    random_slider_value_one = models.IntegerField()
    random_slider_value_two = models.IntegerField()
    random_slider_value_three = models.IntegerField()
    random_slider_value_four = models.IntegerField()
    random_slider_value_five = models.IntegerField()
    random_slider_value_six = models.IntegerField()
    random_slider_value_seven = models.IntegerField()
    random_slider_value_eight = models.IntegerField()
    random_slider_value_nine = models.IntegerField()
    random_slider_value_ten = models.IntegerField()
    random_slider_value_eleven = models.IntegerField()
    random_slider_value_twelve = models.IntegerField()
    random_slider_value_thirteen = models.IntegerField()
    random_slider_value_fourteen = models.IntegerField()
    random_slider_value_fifteen = models.IntegerField()
    random_slider_value_sixteen = models.IntegerField()
    random_slider_value_seventeen = models.IntegerField()
    random_slider_value_eighteen = models.IntegerField()
    random_slider_value_nineteen = models.IntegerField()
    random_slider_value_twenty = models.IntegerField()
    random_slider_value_twentyone = models.IntegerField()
    random_slider_value_twentytwo = models.IntegerField()
    random_slider_value_twentythree = models.IntegerField()
    random_slider_value_twentyfour = models.IntegerField()
    random_slider_value_twentyfive = models.IntegerField()
    random_slider_value_twentysix = models.IntegerField()
    random_slider_value_twentyseven = models.IntegerField()
    random_slider_value_twentyeight = models.IntegerField()
    random_slider_value_twentynine = models.IntegerField()
    random_slider_value_thirty = models.IntegerField()
    random_slider_value_thirtyone = models.IntegerField()
    random_slider_value_thirtytwo = models.IntegerField()
    random_slider_value_thirtythree = models.IntegerField()
    random_slider_value_thirtyfour = models.IntegerField()
    random_slider_value_thirtyfive = models.IntegerField()
    random_slider_value_thirtysix = models.IntegerField()
    random_slider_value_thirtyseven = models.IntegerField()
    random_slider_value_thirtyeight = models.IntegerField()
    random_slider_value_thirtynine = models.IntegerField()
    random_slider_value_fourty = models.IntegerField()
    random_slider_value_fourtyone = models.IntegerField()
    random_slider_value_fourtytwo = models.IntegerField()
    random_slider_value_fourtythree = models.IntegerField()
    random_slider_value_fourtyfour = models.IntegerField()
    random_slider_value_fourtyfive = models.IntegerField()
    random_slider_value_fourtysix = models.IntegerField()
    random_slider_value_fourtyseven = models.IntegerField()
    random_slider_value_fourtyeight = models.IntegerField()
    random_slider_value_fourtynine = models.IntegerField()
    random_slider_value_fifty = models.IntegerField()
    random_slider_value_fiftyone = models.IntegerField()
    random_slider_value_fiftytwo = models.IntegerField()
    random_slider_value_fiftythree = models.IntegerField()
    random_slider_value_fiftyfour = models.IntegerField()
    random_slider_value_fiftyfive = models.IntegerField()
    random_slider_value_fiftysix = models.IntegerField()
    random_slider_value_fiftyseven = models.IntegerField()
    random_slider_value_fiftyeight = models.IntegerField()
    random_slider_value_fiftynine = models.IntegerField()
    random_slider_value_sixty = models.IntegerField()

    correct_sliders = models.IntegerField()
