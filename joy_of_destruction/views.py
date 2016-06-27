# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class Destroy(Page):
    form_model = models.Player
    form_fields = ["amount_to_destroy"]

    def is_displayed(self):
        return True


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_player_destroyed()
        self.group.set_payoffs()
        self.group.log_payoffs()


# class Results(Page):
#     def vars_for_template(self):
#         return {
#             "vouchers": int(self.player.payoff - self.player.destroyed),
#             "destroyed": int(self.player.destroyed),
#
#         }


page_sequence = [
    Introduction,
    Destroy,
    ResultsWaitPage,
    # Results
]
