# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


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
    def after_all_players_arrive(self):
        pass


class SliderOne(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_one']

    def vars_for_template(self):
        return {
            'random_slider_value_one': self.player.random_slider_value_one
        }

    timeout_seconds = 180


class SliderTwo(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_two']

    def vars_for_template(self):
        return {
            'random_slider_value_two': self.player.random_slider_value_two,
        }

    timeout_seconds = 180


class SliderThree(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_three']

    def vars_for_template(self):
        return {
            'random_slider_value_three': self.player.random_slider_value_three
        }

    timeout_seconds = 180


class SliderFour(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_four']

    def vars_for_template(self):
        return {
            'random_slider_value_four': self.player.random_slider_value_four
        }

    timeout_seconds = 180


class SliderFive(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_five']

    def vars_for_template(self):
        return {
            'random_slider_value_five': self.player.random_slider_value_five
        }

    timeout_seconds = 180


class SliderSix(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_six']

    def vars_for_template(self):
        return {
            'random_slider_value_six': self.player.random_slider_value_six
        }

    timeout_seconds = 180


class SliderSeven(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_seven']

    def vars_for_template(self):
        return {
            'random_slider_value_seven': self.player.random_slider_value_seven,
        }

    timeout_seconds = 180


class SliderEight(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_eight']

    def vars_for_template(self):
        return {
            'random_slider_value_eight': self.player.random_slider_value_eight,
        }

    timeout_seconds = 180


class SliderNine(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_nine']

    def vars_for_template(self):
        return {
            'random_slider_value_nine': self.player.random_slider_value_nine,
        }

    timeout_seconds = 180


class SliderTen(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_ten']

    def vars_for_template(self):
        return {
            'random_slider_value_ten': self.player.random_slider_value_ten,
        }

    timeout_seconds = 180


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
