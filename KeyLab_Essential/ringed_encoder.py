# decompyle3 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.8.9 (default, Mar 30 2022, 13:51:17) 
# [Clang 13.1.6 (clang-1316.0.21.2.3)]
# Embedded file name: output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_Essential/ringed_encoder.py
# Compiled at: 2022-01-27 16:28:16
# Size of source mod 2**32: 1654 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import range, round
from past.utils import old_div
import Live
from ableton.v2.control_surface import MIDI_CC_TYPE, CompoundElement
from ableton.v2.control_surface.elements import EncoderElement
RING_VALUE_MIN = 17
RING_VALUE_MAX = 27

class RingedEncoderElement(CompoundElement, EncoderElement):

    def __init__(self, msg_type=MIDI_CC_TYPE, channel=0, identifier=0, map_mode=Live.MidiMap.MapMode.absolute, ring_element=None, *a, **k):
        (super(RingedEncoderElement, self).__init__)(a, msg_type=msg_type, channel=channel, identifier=identifier, map_mode=map_mode, **k)
        self._ring_element = self.register_control_element(ring_element)
        self.request_listen_nested_control_elements()
        self._ring_value_range = list(range(RING_VALUE_MIN, RING_VALUE_MAX + 1))

    def on_nested_control_element_value(self, value, control):
        pass

    def set_ring_value(self, parameter):
        ring_value = self._parameter_value_to_ring_value(parameter.value, parameter.min, parameter.max)
        self._ring_element.send_value(ring_value)

    def _parameter_value_to_ring_value(self, value, minv, maxv):
        vrange = self._ring_value_range
        index = int(round((value - minv) * old_div(len(vrange) - 1, float(maxv - minv))))
        return vrange[index]