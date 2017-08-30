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


class QuestionOne(Page):
    form_model = models.Player
    l1 = ['menu_a_q1', 'menu_a_q2', 'menu_a_q3', 'menu_a_q4', 'menu_a_q5', 'menu_a_q6']
    shuffle(l1)
    form_fields = l1


class QuestionTwo(Page):
    form_model = models.Player
    l2 = ['menu_b_q1', 'menu_b_q2', 'menu_b_q3', 'menu_b_q4', 'menu_b_q5', 'menu_b_q6']
    shuffle(l2)
    form_fields = l2


class QuestionThree(Page):
    form_model = models.Player
    l3 = ['menu_c_q1', 'menu_c_q2', 'menu_c_q3', 'menu_c_q4', 'menu_c_q5', 'menu_c_q6']
    shuffle(l3)
    form_fields = l3


class QuestionFour(Page):
    form_model = models.Player
    l4 = ['menu_d_q1', 'menu_d_q2', 'menu_d_q3', 'menu_d_q4', 'menu_d_q5', 'menu_d_q6']
    shuffle(l4)
    form_fields = l4


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.select_payoff()

page_sequence = [
    Introduction,
    QuestionOne,
    QuestionTwo,
    QuestionThree,
    QuestionFour,
    ResultsWaitPage,
]
