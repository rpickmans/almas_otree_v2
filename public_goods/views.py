# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants


class Introduction(Page):
    """Description of the game: How to play and returns expected"""
    pass


class Contribute(Page):

    """Player: Choose how much to contribute"""

    form_model = models.Player
    form_fields = ['contribution']

    timeout_submission = {'contribution': c(Constants.endowment/2)}


class ContributeWaitPage(WaitPage):
    pass


class Guess(Page):
    form_model = models.Player
    form_fields = ["guess_one", "guess_two"]

    def is_displayed(self):
        return True


class GuessWaitPage(WaitPage):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()

    body_text = "Waiting for other participants to contribute."


page_sequence = [Introduction,
                 Contribute,
                 ContributeWaitPage,
                 Guess,
                 GuessWaitPage,
                 ResultsWaitPage,
                 ]
