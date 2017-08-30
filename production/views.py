# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json
from otree.models import BaseGroup

from . import models
from ._builtin import Page, WaitPage
from .models import Constants, Player
import time


class Introduction(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1


class PracticeSliderOne(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1

    form_model = models.Player
    form_fields = ['practice_slider_value_one']

    def vars_for_template(self):
        return {
            'practice_random_slider_value_one': self.player.practice_random_slider_value_one,
        }


class PracticeSliderTwo(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1

    form_model = models.Player
    form_fields = ['practice_slider_value_two']

    def vars_for_template(self):
        return {
            'practice_random_slider_value_two': self.player.practice_random_slider_value_two,
        }


class ProceedScreen(Page):
    pass


class Wait(WaitPage):
    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.participant.vars["expiry_timestamp"] = time.time() + 3 * 60


class SliderOne(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_one']

    def vars_for_template(self):
        return {
            'random_slider_value_one': self.player.random_slider_value_one
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderTwo(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_two']

    def vars_for_template(self):
        return {
            'random_slider_value_two': self.player.random_slider_value_two,
        }

    timer_text = 'Time left to complete this section:'

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderThree(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_three']

    def vars_for_template(self):
        return {
            'random_slider_value_three': self.player.random_slider_value_three
        }

    timer_text = 'Time left to complete this section:'

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFour(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_four']

    def vars_for_template(self):
        return {
            'random_slider_value_four': self.player.random_slider_value_four
        }

    timer_text = 'Time left to complete this section:'

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFive(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_five']

    def vars_for_template(self):
        return {
            'random_slider_value_five': self.player.random_slider_value_five
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderSix(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_six']

    def vars_for_template(self):
        return {
            'random_slider_value_six': self.player.random_slider_value_six
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderSeven(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_seven']

    def vars_for_template(self):
        return {
            'random_slider_value_seven': self.player.random_slider_value_seven,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderEight(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_eight']

    def vars_for_template(self):
        return {
            'random_slider_value_eight': self.player.random_slider_value_eight,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderNine(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_nine']

    def vars_for_template(self):
        return {
            'random_slider_value_nine': self.player.random_slider_value_nine,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderTen(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_ten']

    def vars_for_template(self):
        return {
            'random_slider_value_ten': self.player.random_slider_value_ten,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_correct_sliders()
        self.group.set_sliders_total()


page_sequence = [
    Introduction,
    PracticeSliderOne,
    PracticeSliderTwo,
    ProceedScreen,
    Wait,
    SliderOne,
    SliderTwo,
    SliderThree,
    SliderFour,
    SliderFive,
    SliderSix,
    SliderSeven,
    SliderEight,
    SliderNine,
    SliderTen,
    ResultsWaitPage,
]
