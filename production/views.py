# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1


class PracticeSlider(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1

    form_model = models.Player
    form_fields = ['practice_slider_value_one', 'practice_slider_value_two']

    def vars_for_template(self):
        return {
            'practice_random_slider_value_one': self.player.practice_random_slider_value_one,
            'practice_random_slider_value_two': self.player.practice_random_slider_value_two,
        }

    timeout_seconds = 300


class WaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Slider(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_one', 'player_slider_value_two', 'player_slider_value_three', 'player_slider_value_four', 'player_slider_value_five', 'player_slider_value_six', 'player_slider_value_seven', 'player_slider_value_eight', 'player_slider_value_nine', 'player_slider_value_ten']

    def vars_for_template(self):
        return {
            'random_slider_value_one': self.player.random_slider_value_one,
            'random_slider_value_two': self.player.random_slider_value_two,
            'random_slider_value_three': self.player.random_slider_value_three,
            'random_slider_value_four': self.player.random_slider_value_four,
            'random_slider_value_five': self.player.random_slider_value_five,
            'random_slider_value_six': self.player.random_slider_value_six,
            'random_slider_value_seven': self.player.random_slider_value_seven,
            'random_slider_value_eight': self.player.random_slider_value_eight,
            'random_slider_value_nine': self.player.random_slider_value_nine,
            'random_slider_value_ten': self.player.random_slider_value_ten,
        }

    timeout_seconds = 300


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()
        self.group.select_winner()
        self.group.correct_sliders_total()
        self.group.view_participant_vars()


# class Results(Page):
#
#     def is_displayed(self):
#         return self.subsession.round_number == Constants.num_rounds
#
#     def vars_for_template(self):
#
#         total = 0
#
#         for p in self.player.in_all_rounds():
#             if p.payoff:
#                 total += p.payoff
#
#         return {
#             "correct_sliders": self.player.correct_sliders,
#         }


page_sequence = [
    Introduction,
    PracticeSlider,
    WaitPage,
    Slider,
    ResultsWaitPage,
    # Results
]
