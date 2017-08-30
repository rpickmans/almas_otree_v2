# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants
import math


class PaymentInfo(Page):
    def is_displayed(self):
        self.player.payoff = self.player.participant.vars["carrying_payoff"]
        return True

    def vars_for_template(self):
        participant = self.player.participant
        return {
            'redemption_code': participant.label or participant.code,
            'payoff': math.floor(participant.vars["carrying_payoff"]),
            'apoints': participant.vars["vouchers"]
        }


page_sequence = [PaymentInfo]
