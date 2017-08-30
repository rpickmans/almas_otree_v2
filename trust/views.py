# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range

from ._builtin import Page, WaitPage
from . import models
from .models import Constants


class Introduction(Page):

    def vars_for_template(self):
        return {'amount_allocated': Constants.amount_allocated}

    def is_displayed(self):
        return self.subsession.round_number == 1


class Send(Page):
    # both players are player 1
    form_model = models.Player
    form_fields = ['sent_amount']


class ShuffleWaitPage(WaitPage):
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        self.subsession.group_randomly()
        # # sort players by amount sent
        # sorted_players = sorted(
        #     self.subsession.get_players(),
        #     key=lambda player: player.sent_amount
        # )
        #
        # if len(sorted_players) == 3:
        #     pass
        # else:
        #     # assuming 6, 12, 0r 18 players
        #     median_sort = len(sorted_players) / 2
        #     for i in sorted_players:
        #         if sorted_players.index(i) > median_sort:
        #             i.participant.vars["ranked"] = "high"
        #         else:
        #             i.participant.vars["ranked"] = "low"
        #
        # # chunk players into groups
        # group_matrix = []
        # ppg = Constants.players_per_group
        # for i in range(0, len(sorted_players), ppg):
        #     group_matrix.append(sorted_players[i:i+ppg])
        #
        # # set new groups
        # self.subsession.set_group_matrix(group_matrix)


class SendBack(Page):
    # both players are player 2
    form_model = models.Player
    form_fields = ['sent_back_amount']

    def vars_for_template(self):
        amount_sent = self.player.get_others_in_group()[0].sent_amount
        tripled_amount = amount_sent * Constants.multiplication_factor

        return {'amount_allocated': Constants.amount_allocated,
                'tripled_amount': tripled_amount,
                'amount_sent': amount_sent,
                'prompt': 'Please enter a number from 0 to %s:' % tripled_amount,
                }

    def sent_back_amount_max(self):
        return self.player.get_others_in_group()[0].sent_amount * Constants.multiplication_factor


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


page_sequence = [
        Introduction,
        Send,
        ShuffleWaitPage,
        SendBack,
        ResultsWaitPage,
    ]
