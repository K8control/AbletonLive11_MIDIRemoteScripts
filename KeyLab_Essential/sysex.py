# decompyle3 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.8.9 (default, Mar 30 2022, 13:51:17) 
# [Clang 13.1.6 (clang-1316.0.21.2.3)]
# Embedded file name: output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/KeyLab_Essential/sysex.py
# Compiled at: 2022-01-27 16:28:16
# Size of source mod 2**32: 1836 bytes
from __future__ import absolute_import, print_function, unicode_literals
START_BYTE = 240
END_BYTE = 247
ON_VALUE = 127
OFF_VALUE = 0
NULL = 0
ARTURIA_MANUFACTURER_ID = (0, 32, 107)
BROADCAST_DEVICE_ID = 127
ARTURIA_EXTENDED_KEYBOARD_PROTOCOL = 66
SET_RESPONSE_DATA_COMMAND = 2
SET_RESPONSE_STRING_COMMAND = 4
RECALL_MEMORY_COMMAND = 5
WORKING_MEMORY_ID = 0
GLOBAL_PARAMETER_ID = 64
ITEM_VALUE_PARAMETER_ID = 0
BACKLIGHTING_PARAMETER_ID = 22
LCD_STRING_PARAMETER_ID = 96
LIVE_MODE_ITEM_ID = 17
MEMORY_PRESET_SELECT_ITEM_ID = 21
LCD_LINE_1_ITEM_ID = 1
LCD_LINE_2_ITEM_ID = 2
VEGAS_MODE_ITEM_ID = 80
DAW_MEMORY_PRESET_INDEX = 2
MESSAGE_HEADER = (
 START_BYTE,) + ARTURIA_MANUFACTURER_ID + (BROADCAST_DEVICE_ID, ARTURIA_EXTENDED_KEYBOARD_PROTOCOL)
LIVE_MODE_MESSAGE_HEADER = MESSAGE_HEADER + (
 SET_RESPONSE_DATA_COMMAND,
 WORKING_MEMORY_ID,
 GLOBAL_PARAMETER_ID,
 LIVE_MODE_ITEM_ID)
MEMORY_PRESET_SWITCH_MESSAGE_HEADER = MESSAGE_HEADER + (RECALL_MEMORY_COMMAND,)
MEMORY_PRESET_SELECT_MODE_MESSAGE_HEADER = MESSAGE_HEADER + (
 SET_RESPONSE_DATA_COMMAND,
 WORKING_MEMORY_ID,
 ITEM_VALUE_PARAMETER_ID,
 MEMORY_PRESET_SELECT_ITEM_ID)
LIGHT_PAD_LED_MSG_PREFIX = MESSAGE_HEADER + (
 SET_RESPONSE_DATA_COMMAND,
 WORKING_MEMORY_ID,
 BACKLIGHTING_PARAMETER_ID)
LCD_SET_STRING_MESSAGE_HEADER = MESSAGE_HEADER + (
 SET_RESPONSE_STRING_COMMAND,
 WORKING_MEMORY_ID,
 LCD_STRING_PARAMETER_ID)
VEGAS_MODE_MESSAGE_HEADER = MESSAGE_HEADER + (
 SET_RESPONSE_DATA_COMMAND,
 WORKING_MEMORY_ID,
 GLOBAL_PARAMETER_ID,
 VEGAS_MODE_ITEM_ID)