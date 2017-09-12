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
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        pass


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
        self.participant.vars["expiry_timestamp"] = time.time() + 3 * 60
        return True


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


class SliderEleven(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_eleven']

    def vars_for_template(self):
        return {
            'random_slider_value_eleven': self.player.random_slider_value_eleven,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderTwelve(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_twelve']

    def vars_for_template(self):
        return {
            'random_slider_value_twelve': self.player.random_slider_value_twelve,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderThirteen(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_thirteen']

    def vars_for_template(self):
        return {
            'random_slider_value_thirteen': self.player.random_slider_value_thirteen,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFourteen(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_fourteen']

    def vars_for_template(self):
        return {
            'random_slider_value_fourteen': self.player.random_slider_value_fourteen,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFifteen(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_fifteen']

    def vars_for_template(self):
        return {
            'random_slider_value_fifteen': self.player.random_slider_value_fifteen,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderSixteen(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_sixteen']

    def vars_for_template(self):
        return {
            'random_slider_value_sixteen': self.player.random_slider_value_sixteen,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderSeventeen(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_seventeen']

    def vars_for_template(self):
        return {
            'random_slider_value_seventeen': self.player.random_slider_value_seventeen,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderEighteen(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_eighteen']

    def vars_for_template(self):
        return {
            'random_slider_value_eighteen': self.player.random_slider_value_eighteen,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderNineteen(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_nineteen']

    def vars_for_template(self):
        return {
            'random_slider_value_nineteen': self.player.random_slider_value_nineteen,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderTwenty(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_twenty']

    def vars_for_template(self):
        return {
            'random_slider_value_twenty': self.player.random_slider_value_twenty,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderTwentyOne(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_twentyone']

    def vars_for_template(self):
        return {
            'random_slider_value_twentyone': self.player.random_slider_value_twentyone,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderTwentyTwo(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_twentytwo']

    def vars_for_template(self):
        return {
            'random_slider_value_twentytwo': self.player.random_slider_value_twentytwo,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderTwentyThree(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_twentythree']

    def vars_for_template(self):
        return {
            'random_slider_value_twentythree': self.player.random_slider_value_twentythree,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderTwentyFour(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_twentyfour']

    def vars_for_template(self):
        return {
            'random_slider_value_twentyfour': self.player.random_slider_value_twentyfour,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderTwentyFive(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_twentyfive']

    def vars_for_template(self):
        return {
            'random_slider_value_twentyfive': self.player.random_slider_value_twentyfive,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderTwentySix(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_twentysix']

    def vars_for_template(self):
        return {
            'random_slider_value_twentysix': self.player.random_slider_value_twentysix,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderTwentySeven(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_twentyseven']

    def vars_for_template(self):
        return {
            'random_slider_value_twentyseven': self.player.random_slider_value_twentyseven,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderTwentyEight(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_twentyeight']

    def vars_for_template(self):
        return {
            'random_slider_value_twentyeight': self.player.random_slider_value_twentyeight,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderTwentyNine(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_twentynine']

    def vars_for_template(self):
        return {
            'random_slider_value_twentynine': self.player.random_slider_value_twentynine,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderThirty(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_thirty']

    def vars_for_template(self):
        return {
            'random_slider_value_thirty': self.player.random_slider_value_thirty,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderThirtyOne(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_thirtyone']

    def vars_for_template(self):
        return {
            'random_slider_value_thirtyone': self.player.random_slider_value_thirtyone,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderThirtyTwo(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_thirtytwo']

    def vars_for_template(self):
        return {
            'random_slider_value_thirtytwo': self.player.random_slider_value_thirtytwo,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderThirtyThree(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_thirtythree']

    def vars_for_template(self):
        return {
            'random_slider_value_thirtythree': self.player.random_slider_value_thirtythree,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderThirtyFour(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_thirtyfour']

    def vars_for_template(self):
        return {
            'random_slider_value_thirtyfour': self.player.random_slider_value_thirtyfour,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderThirtyFive(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_thirtyfive']

    def vars_for_template(self):
        return {
            'random_slider_value_thirtyfive': self.player.random_slider_value_thirtyfive,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderThirtySix(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_thirtysix']

    def vars_for_template(self):
        return {
            'random_slider_value_thirtysix': self.player.random_slider_value_thirtysix,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderThirtySeven(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_thirtyseven']

    def vars_for_template(self):
        return {
            'random_slider_value_thirtyseven': self.player.random_slider_value_thirtyseven,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderThirtyEight(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_thirtyeight']

    def vars_for_template(self):
        return {
            'random_slider_value_thirtyeight': self.player.random_slider_value_thirtyeight,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderThirtyNine(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_thirtynine']

    def vars_for_template(self):
        return {
            'random_slider_value_thirtynine': self.player.random_slider_value_thirtynine,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFourty(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_fourty']

    def vars_for_template(self):
        return {
            'random_slider_value_fourty': self.player.random_slider_value_fourty,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFourtyOne(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_fourtyone']

    def vars_for_template(self):
        return {
            'random_slider_value_fourtyone': self.player.random_slider_value_fourtyone,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFourtyTwo(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_fourtytwo']

    def vars_for_template(self):
        return {
            'random_slider_value_fourtytwo': self.player.random_slider_value_fourtytwo,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFourtyThree(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_fourtythree']

    def vars_for_template(self):
        return {
            'random_slider_value_fourtythree': self.player.random_slider_value_fourtythree,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFourtyFour(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_fourtyfour']

    def vars_for_template(self):
        return {
            'random_slider_value_fourtyfour': self.player.random_slider_value_fourtyfour,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFourtyFive(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_fourtyfive']

    def vars_for_template(self):
        return {
            'random_slider_value_fourtyfive': self.player.random_slider_value_fourtyfive,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFourtySix(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_fourtysix']

    def vars_for_template(self):
        return {
            'random_slider_value_fourtysix': self.player.random_slider_value_fourtysix,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFourtySeven(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_fourtyseven']

    def vars_for_template(self):
        return {
            'random_slider_value_fourtyseven': self.player.random_slider_value_fourtyseven,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFourtyEight(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_fourtyeight']

    def vars_for_template(self):
        return {
            'random_slider_value_fourtyeight': self.player.random_slider_value_fourtyeight,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFourtyNine(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_fourtynine']

    def vars_for_template(self):
        return {
            'random_slider_value_fourtynine': self.player.random_slider_value_fourtynine,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFifty(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_fifty']

    def vars_for_template(self):
        return {
            'random_slider_value_fifty': self.player.random_slider_value_fifty,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFiftyOne(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_fiftyone']

    def vars_for_template(self):
        return {
            'random_slider_value_fiftyone': self.player.random_slider_value_fiftyone,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFiftyTwo(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_fiftytwo']

    def vars_for_template(self):
        return {
            'random_slider_value_fiftytwo': self.player.random_slider_value_fiftytwo,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFiftyThree(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_fiftythree']

    def vars_for_template(self):
        return {
            'random_slider_value_fiftythree': self.player.random_slider_value_fiftythree,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFiftyFour(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_fiftyfour']

    def vars_for_template(self):
        return {
            'random_slider_value_fiftyfour': self.player.random_slider_value_fiftyfour,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFiftyFive(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_fiftyfive']

    def vars_for_template(self):
        return {
            'random_slider_value_fiftyfive': self.player.random_slider_value_fiftyfive,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFiftySix(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_fiftysix']

    def vars_for_template(self):
        return {
            'random_slider_value_fiftysix': self.player.random_slider_value_fiftysix,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFiftySeven(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_fiftyseven']

    def vars_for_template(self):
        return {
            'random_slider_value_fiftyseven': self.player.random_slider_value_fiftyseven,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFiftyEight(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_fiftyeight']

    def vars_for_template(self):
        return {
            'random_slider_value_fiftyeight': self.player.random_slider_value_fiftyeight,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFiftyNine(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_fiftynine']

    def vars_for_template(self):
        return {
            'random_slider_value_fiftynine': self.player.random_slider_value_fiftynine,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderSixty(Page):
    form_model = models.Player
    form_fields = ['player_slider_value_sixty']

    def vars_for_template(self):
        return {
            'random_slider_value_sixty': self.player.random_slider_value_sixty,
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
    SliderEleven,
    SliderTwelve,
    SliderThirteen,
    SliderFourteen,
    SliderFifteen,
    SliderSixteen,
    SliderSeventeen,
    SliderEighteen,
    SliderNineteen,
    SliderTwenty,
    SliderTwentyOne,
    SliderTwentyTwo,
    SliderTwentyThree,
    SliderTwentyFour,
    SliderTwentyFive,
    SliderTwentySix,
    SliderTwentySeven,
    SliderTwentyEight,
    SliderTwentyNine,
    SliderThirty,
    SliderThirtyOne,
    SliderThirtyTwo,
    SliderThirtyThree,
    SliderThirtyFour,
    SliderThirtyFive,
    SliderThirtySix,
    SliderThirtySeven,
    SliderThirtyEight,
    SliderThirtyNine,
    SliderFourty,
    SliderFourtyOne,
    SliderFourtyTwo,
    SliderFourtyThree,
    SliderFourtyFour,
    SliderFourtyFive,
    SliderFourtySix,
    SliderFourtySeven,
    SliderFourtyEight,
    SliderFourtyNine,
    SliderFifty,
    SliderFiftyOne,
    SliderFiftyTwo,
    SliderFiftyThree,
    SliderFiftyFour,
    SliderFiftyFive,
    SliderFiftySix,
    SliderFiftySeven,
    SliderFiftyEight,
    SliderFiftyNine,
    SliderSixty,
    ResultsWaitPage,
]
