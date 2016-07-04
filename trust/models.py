# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division
from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

from otree import widgets
from otree.common import Currency as c, currency_range
import random
# </standard imports>


doc = """
In the trust game, the participants are matched in pairs where
one of them, participant A, is given a fixed amount of money, say X KSH and the other,
participant B, is not given any money. Participant A can decide to keep the money, in
which case player A will receive the actual payment of X KSH and player B will receive
nothing. Participant A can also decide to send part or all of the money, Y <= X to
player B in which case player B will receive 3Y KSH. In this case player B is given the
option to send money back to player A (any amount he or she likes). If participant A
trusts that some money will be sent back, he or she will benefit from sending the money
to participant B. If, on the other hand, the trust is lower, participant A may decide
to keep the money. Hence, the amount sent from A measures the level of trust of the
participants. The amount sent back from B, reveals the trustworthiness which is also an
interesting measure to study in itself.
"""


class Constants(BaseConstants):
    name_in_url = 'trust'
    players_per_group = 2
    num_rounds = 2

    # Initial amount allocated to each player
    amount_allocated = c(50)
    multiplication_factor = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    sent_amount = models.CurrencyField(
        min=0, max=Constants.amount_allocated,
        doc="""Amount sent by Player One""",
    )

    sent_back_amount = models.CurrencyField(
        doc="""Amount sent back by Player Two""",
        min=c(0),
    )

    def set_payoffs(self):
        if self.subsession.round_number == 1:
            for p in self.get_players():
                if p.id == 1:
                    p.payoff = int(Constants.amount_allocated) - int(self.sent_amount) + int(self.sent_back_amount)
                    p.participant.vars["carrying_payoff"] += p.payoff
                elif p.id == 2:
                    p.payoff = int(self.sent_amount) * Constants.multiplication_factor - int(self.sent_back_amount)
                    p.participant.vars["carrying_payoff"] += p.payoff
                print(p.id, p.payoff)
        elif self.subsession.round_number == 2:
            for p in self.get_players():
                if p.in_previous_rounds()[0].id == 2:
                    p.payoff = int(self.sent_amount) * Constants.multiplication_factor - int(self.sent_back_amount)
                    p.participant.vars["carrying_payoff"] += p.payoff
                elif p.in_previous_rounds()[0].id == 1:
                    p.payoff = int(Constants.amount_allocated) - int(self.sent_amount) + int(self.sent_back_amount)
                    p.participant.vars["carrying_payoff"] += p.payoff

    def log_payoffs(self):
        for p in self.get_players():
            print("player {} payoff is: {}, and contribution was: {}, and the other player sent you: {}".
                  format(p.id, p.payoff, self.sent_amount, self.sent_back_amount))


class Player(BasePlayer):

    def role(self):
        return {1: 'Player One', 2: 'Player Two'}[self.id_in_group]
