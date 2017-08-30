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
    form_fields = ["player_destroyed"]

    def player_destroyed_max(self):
        return self.player.get_others_in_group()[0].participant.vars["ravens_points"]/2

    def vars_for_template(self):
        py = self.player.get_others_in_group()[0]
        return {
            "raven_points": py.participant.vars["ravens_points"],
        }

    def before_next_page(self):
        self.player.vouchers = self.player.participant.vars["ravens_points"] - self.player.player_destroyed


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        for player in self.group.get_players():
            player.set_player_destroyed()
        self.group.set_payoffs()


page_sequence = [
    Introduction,
    Destroy,
    ResultsWaitPage,
]
