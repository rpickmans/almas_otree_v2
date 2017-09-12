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
        menu_a_b_today = participant.vars.get("menu_a_b_today", None)
        menu_a_b_3weeks = participant.vars.get("menu_a_b_3weeks", None)
        menu_c_d_3weeks = participant.vars.get("menu_c_d_3weeks", None)
        menu_c_d_7weeks = participant.vars.get("menu_c_d_7weeks", None),

        if menu_a_b_3weeks and menu_a_b_today:
            return {
                'redemption_code': participant.label or participant.code,
                'payoff': int(math.floor(participant.vars.get("carrying_payoff", None))),
                'payoff_ksh': int(math.floor(participant.vars.get("carrying_payoff", None) / 3.5)),
                'airtime_worth': 50 * participant.vars.get("vouchers", None),

                'menu_a_b_today': participant.vars.get("menu_a_b_today", None)["today"],
                'menu_a_b_today_ksh': int(participant.vars.get("menu_a_b_today", None)["today"] / 3.5),

                'menu_a_b_3weeks': participant.vars.get("menu_a_b_3weeks", None)["weeks3"],
                'menu_a_b_3weeks_ksh': int(participant.vars.get("menu_a_b_3weeks", None)["weeks3"] / 3.5)
            }

        elif menu_c_d_3weeks and menu_c_d_7weeks:
            return {
                'redemption_code': participant.label or participant.code,
                'payoff': int(math.floor(participant.vars.get("carrying_payoff", None))),
                'payoff_ksh': int(math.floor(participant.vars.get("carrying_payoff", None) / 3.5)),
                'airtime_worth': 50 * participant.vars.get("vouchers", None),

                'menu_c_d_3weeks': participant.vars.get("menu_c_d_3weeks", None)["weeks3"],
                'menu_c_d_3weeks_ksh': int(participant.vars.get("menu_c_d_3weeks", None)["weeks3"] / 3.5),

                'menu_c_d_7weeks': participant.vars.get("menu_c_d_7weeks", None)["weeks7"],
                'menu_c_d_7weeks_ksh': int(participant.vars.get("menu_c_d_7weeks", None)["weeks7"] / 3.5)
            }
        else:
            return {
                'redemption_code': participant.label or participant.code,
                'payoff': int(math.floor(participant.vars.get("carrying_payoff", None))),
                'payoff_ksh': int(math.floor(participant.vars.get("carrying_payoff", None) / 3.5)),
                'airtime_worth': 50 * participant.vars.get("vouchers", None),
            }


page_sequence = [Wait, PaymentInfo]
