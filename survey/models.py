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

from django_countries.fields import CountryField


doc = """
Survey questions to collect general background information about the subjects.
"""


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    def set_payoff(self):
        """Calculate payoff, which is zero for the survey"""
        self.payoff = 0

    q_age = models.PositiveIntegerField(verbose_name='What is your age?',
                                        choices=range(13, 125),
                                        initial=None)

    q_gender = models.CharField(initial=None,
                                choices=['Male', 'Female'],
                                verbose_name='What is your gender?',
                                widget=widgets.RadioSelect())

    q_occupation = models.CharField(widget=widgets.RadioSelect(),
                                    choices=["wage-employed", "self-employed", "unemployed"]
                                    )

    q_income = models.CharField(widget=widgets.RadioSelect(),
                                choices=["Less than Ksh.10,000",
                                         "Ksh.10,000 - Ksh. 30,000",
                                         "Ksh. 30,000 - Ksh. 60,000",
                                         "Ksh. 60,000 - Ksh.100,000",
                                         "More than Ksh.100,000",
                                         "Don’t know",
                                         ])

    q_education_father = models.CharField(widget=widgets.RadioSelect(),
                                          choices=["Completed High School",
                                                   "Completed Vocational College",
                                                   "Completed University (Bachelor)",
                                                   "Completed University (Advanced)",
                                                   "Other",
                                                   ])

    q_education_mother = models.CharField(widget=widgets.RadioSelect(),
                                          choices=["Completed High School",
                                                   "Completed Vocational College",
                                                   "Completed University (Bachelor)",
                                                   "Completed University (Advanced)",
                                                   "Other",
                                                   ])

    crt_bat = models.PositiveIntegerField()
    crt_widget = models.PositiveIntegerField()
    crt_lake = models.PositiveIntegerField()


