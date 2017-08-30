# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random
import math


class Donate(Page):
    form_model = models.Player
    form_fields = ['donated_amount']


    def donated_amount_error_message(self, value):
        if self.player.participant.vars["carrying_payoff"] < value:
            return 'Amount to donate should be less than what you have!'

    def vars_for_template(self):
        charities = ["Kiambu Orphans Initiative",
                     "Kanyawegi childrens home",
                     "Destined Childrens Home Kikuyu",
                     "Kakamega Orphans Care Centre",
                     "Upendo Childrens Centre Nyeri",
                     "Huruma Childrens Home Ngong",
                     "Baraka Childrens Home Mombasa"]

        charity = random.choice(charities)
        self.player.charity_allocated = charity
        return {
            'charity': charity,
            'carrying_payoff': math.floor(self.player.participant.vars["carrying_payoff"])
        }


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoff()


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
