# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants

class CognitiveReflectionTest(Page):

    form_model = models.Player
    form_fields = ['cognitive_reflection_one',
                  'cognitive_reflection_two',
                  'cognitive_reflection_three',
                   'cognitive_reflection_four',
                   'cognitive_reflection_five',
                   'cognitive_reflection_six']

    def before_next_page(self):
        self.player.set_payoff()

class Demographics(Page):

    form_model = models.Player
    form_fields = ['demographic_one_scale', 'age', 'no_age', 'height', 'no_height',
                   'weight', 'no_weight', 'gender', 'ethnicity', 'california_residency',
                   'father_occupation', 'mother_occupation', 'income', 'education_father',
                   'education_mother']

page_sequence = [
    CognitiveReflectionTest,
    Demographics,
]
