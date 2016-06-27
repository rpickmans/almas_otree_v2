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
    form_fields = ["raven_p1"]

    def is_displayed(self):
        return True


class FeedbackOne(Page):
    def is_displayed(self):
        return True


class PracticeTwo(Page):
    form_model = models.Player
    form_fields = ["raven_p2"]

    def is_displayed(self):
        return True


class FeedbackTwo(Page):
    def is_displayed(self):
        return True


class RavenOne(Page):
    form_model = models.Player
    form_fields = ["raven_1"]

    def is_displayed(self):
        return True


class RavenTwo(Page):
    form_model = models.Player
    form_fields = ["raven_2"]

    def is_displayed(self):
        return True


class RavenThree(Page):
    form_model = models.Player
    form_fields = ["raven_3"]

    def is_displayed(self):
        return True


class RavenFour(Page):
    form_model = models.Player
    form_fields = ["raven_4"]

    def is_displayed(self):
        return True


class RavenFive(Page):
    form_model = models.Player
    form_fields = ["raven_5"]

    def is_displayed(self):
        return True


class RavenSix(Page):
    form_model = models.Player
    form_fields = ["raven_6"]

    def is_displayed(self):
        return True


page_sequence = [
    Introduction,
    PracticeOne,
    FeedbackOne,
    PracticeTwo,
    FeedbackTwo,
    RavenOne,
    RavenTwo,
    RavenThree,
    RavenFour,
    RavenFive,
    RavenSix,
]
