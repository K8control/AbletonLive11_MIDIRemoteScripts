# decompyle3 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.8.9 (default, Mar 30 2022, 13:51:17) 
# [Clang 13.1.6 (clang-1316.0.21.2.3)]
# Embedded file name: output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/ableton/v2/control_surface/control/radio_button.py
# Compiled at: 2022-01-27 16:28:17
# Size of source mod 2**32: 1778 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ...base import nop
from .button import ButtonControlBase
from .control import control_color, control_event

class RadioButtonControl(ButtonControlBase):
    checked = control_event('checked')

    class State(ButtonControlBase.State):
        unchecked_color = control_color('DefaultButton.Off')
        checked_color = control_color('DefaultButton.On')

        def __init__(self, unchecked_color=None, checked_color=None, *a, **k):
            (super(RadioButtonControl.State, self).__init__)(*a, **k)
            if unchecked_color is not None:
                self.unchecked_color = unchecked_color
            if checked_color is not None:
                self.checked_color = checked_color
            self._checked = False
            self._on_checked = nop

        @property
        def is_checked(self):
            return self._checked

        @is_checked.setter
        def is_checked(self, value):
            if self._checked != value:
                self._checked = value
                if self._checked:
                    self._on_checked()
                self._send_current_color()

        def _send_button_color(self):
            self._control_element.set_light(self.checked_color if self._checked else self.unchecked_color)

        def _on_pressed(self):
            super(RadioButtonControl.State, self)._on_pressed()
            if not self._checked:
                self._checked = True
                self._notify_checked()

        def _notify_checked(self):
            if self._checked:
                self._call_listener('checked')
                self._on_checked()