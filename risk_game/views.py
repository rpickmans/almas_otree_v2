# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class Decide(Page):
    form_model = models.Player
    form_fields = ['decision']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.make_random_toss()
        self.group.set_payoffs()


page_sequence = [
    Introduction,
    Decide,
    ResultsWaitPage,
]
