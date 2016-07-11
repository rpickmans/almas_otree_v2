# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range

from ._builtin import Page, WaitPage
from . import models
from .models import Constants


def vars_for_all_templates(self):
    role = ""
    if self.subsession.round_number == 1 and self.player.id_in_group == 1:
        role = "Player One"
    elif self.subsession.round_number == 1 and self.player.id_in_group == 2:
        role = "Player Two"
    elif self.subsession.round_number == 2 and self.player.id_in_group == 1:
        role = "Player Two"
    elif self.subsession.round_number == 2 and self.player.id_in_group == 2:
        role = "Player One"
    return {
        'role': role,
        'instructions': 'trust/Instructions.html',
    }


class Introduction(Page):

    def vars_for_template(self):
        return {'amount_allocated': Constants.amount_allocated}

    def is_displayed(self):
        return self.subsession.round_number == 1


class Send(Page):

    """This page is only for P1
    P1 sends amount (all, some, or none) to P2
    This amount is tripled by experimenter,
    i.e if sent amount by P1 is 5, amount received by P2 is 15"""

    form_model = models.Group
    form_fields = ['sent_amount']

    def is_displayed(self):
        if self.subsession.round_number == 2:
            return self.player.id_in_group == 2
        return self.player.id_in_group == 1


class SendBack(Page):

    """This page is only for P2
    P2 sends back some amount (of the tripled amount received) to P1"""

    form_model = models.Group
    form_fields = ['sent_back_amount']

    def is_displayed(self):
        if self.subsession.round_number == 2:
            return self.player.id_in_group == 1
        return self.player.id_in_group == 2

    def vars_for_template(self):
        tripled_amount = self.group.sent_amount * Constants.multiplication_factor

        return {'amount_allocated': Constants.amount_allocated,
                'tripled_amount': tripled_amount,
                'prompt':
                'Please enter a number from 0 to %s:' % tripled_amount}

    def sent_back_amount_max(self):
        return self.group.sent_amount * Constants.multiplication_factor


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class RoundNumber(Page):
    def is_displayed(self):
        if self.subsession.round_number == 1:
            self
            return True
        else:
            return False

page_sequence = [
        Introduction,
        Send,
        WaitPage,
        SendBack,
        ResultsWaitPage,
        RoundNumber
    ]
