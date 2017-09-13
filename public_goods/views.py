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
    body_text = "Please wait."


class Guess(Page):
    form_model = models.Player
    form_fields = ["guess_one", "guess_two"]


class GuessWaitPage(WaitPage):
    body_text = "Please wait."


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()

    body_text = "Please wait."


class Wait(WaitPage):
    body_text = "Please wait."

    wait_for_all_groups = True


page_sequence = [Introduction,
                 Contribute,
                 ContributeWaitPage,
                 Guess,
                 GuessWaitPage,
                 ResultsWaitPage,
                 Wait,
                 ]
