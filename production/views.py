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
    form_fields = ['pr_sv_1']

    def vars_for_template(self):
        return {
            'pr_rsv_1': self.player.pr_rsv_1,
        }


class PracticeSliderTwo(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1

    form_model = models.Player
    form_fields = ['pr_sv_2']

    def vars_for_template(self):
        return {
            'pr_rsv_2': self.player.pr_rsv_2,
        }


class ProceedScreen(Page):
    pass


class Wait(WaitPage):
    title_text = ""
    body_text = "Please wait."
    wait_for_all_groups = True

    def after_all_players_arrive(self):
        pass


class SliderOne(Page):
    form_model = models.Player
    form_fields = ['psv_1']

    def vars_for_template(self):
        return {
            'rsv_1': self.player.rsv_1
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        self.participant.vars["expiry_timestamp"] = time.time() + 3 * 60
        return True


class SliderTwo(Page):
    form_model = models.Player
    form_fields = ['psv_2']

    def vars_for_template(self):
        return {
            'rsv_2': self.player.rsv_2,
        }

    timer_text = 'Time left to complete this section:'

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderThree(Page):
    form_model = models.Player
    form_fields = ['psv_3']

    def vars_for_template(self):
        return {
            'rsv_3': self.player.rsv_3
        }

    timer_text = 'Time left to complete this section:'

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFour(Page):
    form_model = models.Player
    form_fields = ['psv_4']

    def vars_for_template(self):
        return {
            'rsv_4': self.player.rsv_4
        }

    timer_text = 'Time left to complete this section:'

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFive(Page):
    form_model = models.Player
    form_fields = ['psv_5']

    def vars_for_template(self):
        return {
            'rsv_5': self.player.rsv_5
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderSix(Page):
    form_model = models.Player
    form_fields = ['psv_6']

    def vars_for_template(self):
        return {
            'rsv_6': self.player.rsv_6
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderSeven(Page):
    form_model = models.Player
    form_fields = ['psv_7']

    def vars_for_template(self):
        return {
            'rsv_7': self.player.rsv_7,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderEight(Page):
    form_model = models.Player
    form_fields = ['psv_8']

    def vars_for_template(self):
        return {
            'rsv_8': self.player.rsv_8,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderNine(Page):
    form_model = models.Player
    form_fields = ['psv_9']

    def vars_for_template(self):
        return {
            'rsv_9': self.player.rsv_9,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderTen(Page):
    form_model = models.Player
    form_fields = ['psv_10']

    def vars_for_template(self):
        return {
            'rsv_10': self.player.rsv_10,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderEleven(Page):
    form_model = models.Player
    form_fields = ['psv_11']

    def vars_for_template(self):
        return {
            'rsv_11': self.player.rsv_11,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderTwelve(Page):
    form_model = models.Player
    form_fields = ['psv_12']

    def vars_for_template(self):
        return {
            'rsv_12': self.player.rsv_12,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderThirteen(Page):
    form_model = models.Player
    form_fields = ['psv_13']

    def vars_for_template(self):
        return {
            'rsv_13': self.player.rsv_13,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFourteen(Page):
    form_model = models.Player
    form_fields = ['psv_14']

    def vars_for_template(self):
        return {
            'rsv_14': self.player.rsv_14,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFifteen(Page):
    form_model = models.Player
    form_fields = ['psv_15']

    def vars_for_template(self):
        return {
            'rsv_15': self.player.rsv_15,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderSixteen(Page):
    form_model = models.Player
    form_fields = ['psv_16']

    def vars_for_template(self):
        return {
            'rsv_16': self.player.rsv_16,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderSeventeen(Page):
    form_model = models.Player
    form_fields = ['psv_17']

    def vars_for_template(self):
        return {
            'rsv_17': self.player.rsv_17,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderEighteen(Page):
    form_model = models.Player
    form_fields = ['psv_18']

    def vars_for_template(self):
        return {
            'rsv_18': self.player.rsv_18,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderNineteen(Page):
    form_model = models.Player
    form_fields = ['psv_19']

    def vars_for_template(self):
        return {
            'rsv_19': self.player.rsv_19,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderTwenty(Page):
    form_model = models.Player
    form_fields = ['psv_20']

    def vars_for_template(self):
        return {
            'rsv_20': self.player.rsv_20,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderTwentyOne(Page):
    form_model = models.Player
    form_fields = ['psv_21']

    def vars_for_template(self):
        return {
            'rsv_21': self.player.rsv_21,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderTwentyTwo(Page):
    form_model = models.Player
    form_fields = ['psv_22']

    def vars_for_template(self):
        return {
            'rsv_22': self.player.rsv_22,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderTwentyThree(Page):
    form_model = models.Player
    form_fields = ['psv_23']

    def vars_for_template(self):
        return {
            'rsv_23': self.player.rsv_23,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderTwentyFour(Page):
    form_model = models.Player
    form_fields = ['psv_24']

    def vars_for_template(self):
        return {
            'rsv_24': self.player.rsv_24,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderTwentyFive(Page):
    form_model = models.Player
    form_fields = ['psv_25']

    def vars_for_template(self):
        return {
            'rsv_25': self.player.rsv_25,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderTwentySix(Page):
    form_model = models.Player
    form_fields = ['psv_26']

    def vars_for_template(self):
        return {
            'rsv_26': self.player.rsv_26,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderTwentySeven(Page):
    form_model = models.Player
    form_fields = ['psv_27']

    def vars_for_template(self):
        return {
            'rsv_27': self.player.rsv_27,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderTwentyEight(Page):
    form_model = models.Player
    form_fields = ['psv_28']

    def vars_for_template(self):
        return {
            'rsv_28': self.player.rsv_28,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderTwentyNine(Page):
    form_model = models.Player
    form_fields = ['psv_29']

    def vars_for_template(self):
        return {
            'rsv_29': self.player.rsv_29,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderThirty(Page):
    form_model = models.Player
    form_fields = ['psv_30']

    def vars_for_template(self):
        return {
            'rsv_30': self.player.rsv_30,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderThirtyOne(Page):
    form_model = models.Player
    form_fields = ['psv_31']

    def vars_for_template(self):
        return {
            'rsv_thirtyone': self.player.rsv_31,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderThirtyTwo(Page):
    form_model = models.Player
    form_fields = ['psv_32']

    def vars_for_template(self):
        return {
            'rsv_32': self.player.rsv_32,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderThirtyThree(Page):
    form_model = models.Player
    form_fields = ['psv_33']

    def vars_for_template(self):
        return {
            'rsv_33': self.player.rsv_33,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderThirtyFour(Page):
    form_model = models.Player
    form_fields = ['psv_34']

    def vars_for_template(self):
        return {
            'rsv_34': self.player.rsv_34,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderThirtyFive(Page):
    form_model = models.Player
    form_fields = ['psv_35']

    def vars_for_template(self):
        return {
            'rsv_35': self.player.rsv_35,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderThirtySix(Page):
    form_model = models.Player
    form_fields = ['psv_36']

    def vars_for_template(self):
        return {
            'rsv_36': self.player.rsv_36,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderThirtySeven(Page):
    form_model = models.Player
    form_fields = ['psv_37']

    def vars_for_template(self):
        return {
            'rsv_37': self.player.rsv_37,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderThirtyEight(Page):
    form_model = models.Player
    form_fields = ['psv_38']

    def vars_for_template(self):
        return {
            'rsv_38': self.player.rsv_38,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderThirtyNine(Page):
    form_model = models.Player
    form_fields = ['psv_39']

    def vars_for_template(self):
        return {
            'rsv_39': self.player.rsv_39,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFourty(Page):
    form_model = models.Player
    form_fields = ['psv_40']

    def vars_for_template(self):
        return {
            'rsv_40': self.player.rsv_40,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFourtyOne(Page):
    form_model = models.Player
    form_fields = ['psv_41']

    def vars_for_template(self):
        return {
            'rsv_42': self.player.rsv_41,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFourtyTwo(Page):
    form_model = models.Player
    form_fields = ['psv_42']

    def vars_for_template(self):
        return {
            'rsv_42': self.player.rsv_42,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFourtyThree(Page):
    form_model = models.Player
    form_fields = ['psv_43']

    def vars_for_template(self):
        return {
            'rsv_43': self.player.rsv_43,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFourtyFour(Page):
    form_model = models.Player
    form_fields = ['psv_44']

    def vars_for_template(self):
        return {
            'rsv_44': self.player.rsv_44,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFourtyFive(Page):
    form_model = models.Player
    form_fields = ['psv_45']

    def vars_for_template(self):
        return {
            'rsv_46': self.player.rsv_45,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFourtySix(Page):
    form_model = models.Player
    form_fields = ['psv_46']

    def vars_for_template(self):
        return {
            'rsv_46': self.player.rsv_46,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFourtySeven(Page):
    form_model = models.Player
    form_fields = ['psv_47']

    def vars_for_template(self):
        return {
            'rsv_47': self.player.rsv_47,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFourtyEight(Page):
    form_model = models.Player
    form_fields = ['psv_48']

    def vars_for_template(self):
        return {
            'rsv_48': self.player.rsv_48,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFourtyNine(Page):
    form_model = models.Player
    form_fields = ['psv_49']

    def vars_for_template(self):
        return {
            'rsv_49': self.player.rsv_49,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFifty(Page):
    form_model = models.Player
    form_fields = ['psv_50']

    def vars_for_template(self):
        return {
            'rsv_50': self.player.rsv_50,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFiftyOne(Page):
    form_model = models.Player
    form_fields = ['psv_51']

    def vars_for_template(self):
        return {
            'rsv_51': self.player.rsv_51,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFiftyTwo(Page):
    form_model = models.Player
    form_fields = ['psv_52']

    def vars_for_template(self):
        return {
            'rsv_52': self.player.rsv_52,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFiftyThree(Page):
    form_model = models.Player
    form_fields = ['psv_53']

    def vars_for_template(self):
        return {
            'rsv_53': self.player.rsv_53,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFiftyFour(Page):
    form_model = models.Player
    form_fields = ['psv_54']

    def vars_for_template(self):
        return {
            'rsv_54': self.player.rsv_54,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFiftyFive(Page):
    form_model = models.Player
    form_fields = ['psv_55']

    def vars_for_template(self):
        return {
            'rsv_55': self.player.rsv_55,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFiftySix(Page):
    form_model = models.Player
    form_fields = ['psv_56']

    def vars_for_template(self):
        return {
            'rsv_56': self.player.rsv_56,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFiftySeven(Page):
    form_model = models.Player
    form_fields = ['psv_57']

    def vars_for_template(self):
        return {
            'rsv_57': self.player.rsv_57,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFiftyEight(Page):
    form_model = models.Player
    form_fields = ['psv_58']

    def vars_for_template(self):
        return {
            'rsv_59': self.player.rsv_58,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderFiftyNine(Page):
    form_model = models.Player
    form_fields = ['psv_59']

    def vars_for_template(self):
        return {
            'rsv_59': self.player.rsv_59,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class SliderSixty(Page):
    form_model = models.Player
    form_fields = ['psv_60']

    def vars_for_template(self):
        return {
            'rsv_60': self.player.rsv_60,
        }

    def get_timeout_seconds(self):
        return self.participant.vars['expiry_timestamp'] - time.time()

    def is_displayed(self):
        return self.participant.vars['expiry_timestamp'] - time.time() > 3


class ResultsWaitPage(WaitPage):
    title_text = ""
    body_text = "Please wait."

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
