# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random


class Donate(Page):
    form_model = models.Player
    form_fields = ['donated_amount']

    def vars_for_template(self):

        charities = ["Kiambu Orphans Initiative",
                    "Kanyawegi childrens home",
                    "Destined Childrens Home Kikuyu",
                    "Kakamega Orphans Care Centre",
                    "Upendo Childrens Centre Nyeri",
                    "Huruma Childrens Home Ngong",
                    "Baraka Childrens Home Mombasa"]



        return {
            'charity': random.choice(charities),
            'carrying_payoff': self.player.carrying_payoff
        }

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass

class Results(Page):
    def vars_for_template(self):
        return {
            'donated': self.player.donated_amount,
        }

page_sequence = [
    Donate,
    ResultsWaitPage,
    Results
]
