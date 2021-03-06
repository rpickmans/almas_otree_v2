# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class PracticeOne(Page):
    form_model = models.Player
    form_fields = ["practise_one"]



class PracticeTwo(Page):
    form_model = models.Player
    form_fields = ["practise_two"]


class Wait(WaitPage):
    def after_all_players_arrive(self):
        pass


class RavenOne(Page):
    form_model = models.Player
    form_fields = ["raven_1"]



class RavenTwo(Page):
    form_model = models.Player
    form_fields = ["raven_2"]



class RavenThree(Page):
    form_model = models.Player
    form_fields = ["raven_3"]



class RavenFour(Page):
    form_model = models.Player
    form_fields = ["raven_4"]



class RavenFive(Page):
    form_model = models.Player
    form_fields = ["raven_5"]


class RavenSix(Page):
    form_model = models.Player
    form_fields = ["raven_6"]


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


page_sequence = [
    Introduction,
    PracticeOne,
    PracticeTwo,
    Wait,
    RavenOne,
    RavenTwo,
    RavenThree,
    RavenFour,
    RavenFive,
    RavenSix,
    ResultsWaitPage,
]
