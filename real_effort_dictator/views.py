# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    pass


class Question(Page):
    form_model = models.Player
    form_fields = ["answer"]

    def is_displayed(self):
        return True


class Feedback(Page):

    def is_displayed(self):
        return True


class Offer(Page):
    form_model = models.Player
    form_fields = ["keep"]

    def is_displayed(self):
        return True


class OfferWaitPage(WaitPage):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


# class Results(Page):
#     def vars_for_template(self):
#         return {
#             # 'total_earnings': self.group.total_contribution * Constants.efficiency_factor,
#             'individual_earnings': self.player.payoff,
#             'contribution': self.player.contribution,
#         }


page_sequence = [
    Intro,
    Question,
    Feedback,
    Offer,
    OfferWaitPage,
    ResultsWaitPage,
    # Results,
]
