# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class ShuffleWaitPage(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):

        # sort players by correct sliders from previous rounds
        sorted_players = sorted(
            self.subsession.get_players(),
            key=lambda player: player.participant.vars['total_correct']
        )
        print (sorted_players)

        if len(sorted_players) == 3:
            print ("Only three - can't find median")
        else:
            # assuming 6, 12, 0r 18 players
            median_sort = len(sorted_players) / 2
            for i in sorted_players:
                if sorted_players.index(i) > median_sort:
                    i.participant.vars["rank"] = "high"
                else:
                    i.participant.vars["rank"] = "low"

        # chunk players into groups
        group_matrix = []
        ppg = Constants.players_per_group
        for i in range(0, len(sorted_players), ppg):
            group_matrix.append(sorted_players[i:i+ppg])

        # set new groups
        self.subsession.set_group_matrix(group_matrix)


class Intro(Page):

    def vars_for_template(self):
        participant = self.player.participant
        return {
            'rank': participant.vars["rank"]
        }


class Offer(Page):
    form_model = models.Player
    form_fields = ["keep"]

    def vars_for_template(self):
        participant = self.player.participant
        return {
            'rank': participant.vars["rank"]
        }

    def keep_error_message(self, value):
        if self.player.participant.vars["rank"] == "high":
            if not (value == 0 or value == 75 or value == 150):
                return 'Value must be 0,75, or 150'
        elif self.player.participant.vars["rank"] == "low":
            if not (value == 0 or value == 25 or value == 50):
                return 'Value must be 0, 25, or 50'


class OfferWaitPage(WaitPage):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()



page_sequence = [
    ShuffleWaitPage,
    Intro,
    Offer,
    OfferWaitPage,
    ResultsWaitPage,
    # Results,
]
