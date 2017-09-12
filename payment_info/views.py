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
            'payoff': int(math.floor(participant.vars.get("carrying_payoff", None))),
            'payoff_ksh': int(math.floor(participant.vars.get("carrying_payoff", None) / 0.5)),
            'chosen_future_tp': participant.vars.get("chosen_future_tp", None),
            'to_tokens_ksh': int(participant.vars.get("chosen_future_tp", None) / 0.5),
            'date_to_pay_tp': participant.vars.get("date_to_pay_tp", None),
            'vouchers': participant.vars.get("vouchers", None),
            'airtime_worth': 50 * participant.vars.get("vouchers", None),
        }


page_sequence = [Wait, PaymentInfo]
