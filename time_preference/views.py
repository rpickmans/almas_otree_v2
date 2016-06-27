# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from random import shuffle


class Introduction(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1


class  QuestionOne(Page):
    form_model = models.Player
    l1=['q11', 'q12', 'q13', 'q14', 'q15', 'q16']
    shuffle(l1)
    form_fields = l1


class  QuestionTwo(Page):
    form_model = models.Player
    l2=['q21', 'q22', 'q23', 'q24', 'q25', 'q26']
    shuffle(l2)
    form_fields = l2

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


page_sequence = [
    Introduction,
    QuestionOne,
    QuestionTwo,
    ResultsWaitPage,
]
