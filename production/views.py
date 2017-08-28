# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants
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


class WaitPage(WaitPage):
    pass


class SliderOne(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_one']

    def vars_for_template(self):
        return {
            'random_slider_value_one': self.player.random_slider_value_one
        }

    def before_next_page(self):
        # user has 3 minutes to complete as many pages as possible
        print("niiice")
        self.participant.vars['expiry_timestamp'] = time.time() + 3 * 60


class SliderTwo(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_two']

    def vars_for_template(self):
        return {
            'random_slider_value_two': self.player.random_slider_value_two,
        }

    timer_text = 'Time left to complete this section:'

    # timeout_seconds = 180
    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()


class SliderThree(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_three']

    def vars_for_template(self):
        return {
            'random_slider_value_three': self.player.random_slider_value_three
        }

    timer_text = 'Time left to complete this section:'

    # timeout_seconds = 180
    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()


class SliderFour(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_four']

    def vars_for_template(self):
        return {
            'random_slider_value_four': self.player.random_slider_value_four
        }

    timer_text = 'Time left to complete this section:'

    # timeout_seconds = 180
    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()


class SliderFive(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_five']

    def vars_for_template(self):
        return {
            'random_slider_value_five': self.player.random_slider_value_five
        }

        print("hhhhh")

    timer_text = 'Time left to complete this section:'

    # timeout_seconds = 180
    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()


class SliderSix(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_six']

    def vars_for_template(self):
        return {
            'random_slider_value_six': self.player.random_slider_value_six
        }

    timer_text = 'Time left to complete this section:'

    # timeout_seconds = 180
    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()


class SliderSeven(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_seven']

    def vars_for_template(self):
        return {
            'random_slider_value_seven': self.player.random_slider_value_seven,
        }

    timer_text = 'Time left to complete this section:'

    # timeout_seconds = 180
    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()


class SliderEight(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_eight']

    def vars_for_template(self):
        return {
            'random_slider_value_eight': self.player.random_slider_value_eight,
        }

    timer_text = 'Time left to complete this section:'

    # timeout_seconds = 180
    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()


class SliderNine(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_nine']

    def vars_for_template(self):
        return {
            'random_slider_value_nine': self.player.random_slider_value_nine,
        }

    timer_text = 'Time left to complete this section:'

    # timeout_seconds = 180
    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()


class SliderTen(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_ten']

    def vars_for_template(self):
        return {
            'random_slider_value_ten': self.player.random_slider_value_ten,
        }

    timer_text = 'Time left to complete this section:'

    # timeout_seconds = 180
    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_correct_sliders()
        self.group.set_sliders_total()


page_sequence = [
    Introduction,
    PracticeSliderOne,
    PracticeSliderTwo,
    WaitPage,
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
