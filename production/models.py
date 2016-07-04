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
            g.random_slider_value_one = random.randint(1,100)
            g.random_slider_value_two = random.randint(1,100)
            g.random_slider_value_three = random.randint(1,100)
            g.random_slider_value_four = random.randint(1,100)
            g.random_slider_value_five = random.randint(1,100)
            g.random_slider_value_six = random.randint(1,100)
            g.random_slider_value_seven = random.randint(1,100)
            g.random_slider_value_eight = random.randint(1,100)
            g.random_slider_value_nine = random.randint(1,100)
            g.random_slider_value_ten = random.randint(1,100)
            g.practice_random_slider_value_one = random.randint(1,100)
            g.practice_random_slider_value_two = random.randint(1,100)


class Group(BaseGroup):
    def set_correct_sliders(self):
        for p in self.get_players():
            correct = 0
            if p.player_slider_value_one == p.random_slider_value_one:
                correct+=1
            if p.player_slider_value_two == p.random_slider_value_two:
                correct+=1
            if p.player_slider_value_three == p.random_slider_value_three:
                correct+=1
            if p.player_slider_value_four == p.random_slider_value_four:
                correct+=1
            if p.player_slider_value_five == p.random_slider_value_five:
                correct+=1

            if p.player_slider_value_six == p.random_slider_value_six:
                correct+=1
            if p.player_slider_value_seven == p.random_slider_value_seven:
                correct+=1
            if p.player_slider_value_eight == p.random_slider_value_eight:
                correct+=1
            if p.player_slider_value_nine == p.random_slider_value_nine:
                correct+=1
            if p.player_slider_value_ten == p.random_slider_value_ten:
                correct+=1

            p.correct_sliders = correct

    def set_sliders_total(self):
        for p in self.get_players():
            p.participant.vars["total_correct"] = p.correct_sliders


class Player(BasePlayer):
    # pratice sliders
    practice_slider_value_one = models.IntegerField(widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    practice_slider_value_two = models.IntegerField(widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))

    # input from player
    player_slider_value_one = models.IntegerField(widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_two = models.IntegerField(widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_three = models.IntegerField(widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_four = models.IntegerField(widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_five = models.IntegerField(widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))

    player_slider_value_six = models.IntegerField(widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_seven = models.IntegerField(widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_eight = models.IntegerField(widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_nine = models.IntegerField(widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))
    player_slider_value_ten = models.IntegerField(widget=widgets.SliderInput(attrs={'step': '1', 'min': '0', 'max': '100'}))

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

    correct_sliders = models.IntegerField()
