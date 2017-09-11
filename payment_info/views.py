# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants
import math


class Wait(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.payoff = p.participant.vars["carrying_payoff"]
            p.total_points = p.participant.vars["carrying_payoff"]


class PaymentInfo(Page):

    def vars_for_template(self):
        participant = self.player.participant
        return {
            'redemption_code': participant.label or participant.code,
            'payoff': math.floor(participant.vars["carrying_payoff"]),
            'time_preference_future_points': participant.vars["chosen_future_tp"],
            'date_to_pay_tp': participant.vars["time_preference_date_to_pay"],
            'vouchers': participant.vars["vouchers"],
        }


page_sequence = [Wait, PaymentInfo]
