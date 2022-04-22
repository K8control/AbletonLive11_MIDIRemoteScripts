# decompyle3 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.8.9 (default, Mar 30 2022, 13:51:17) 
# [Clang 13.1.6 (clang-1316.0.21.2.3)]
# Embedded file name: output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/LV2_LX2_LC2_LD2/consts.py
# Compiled at: 2022-01-27 16:28:16
# Size of source mod 2**32: 3278 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import range
TRACK_CHANNEL_SETUP1 = 9
AUX_CHANNEL_SETUP1 = 10
CHANNEL_SETUP1 = 11
TRACK_CHANNEL_SETUP2 = 12
AUX_CHANNEL_SETUP2 = 13
CHANNEL_SETUP2 = 14
SEND_CCS = [[x + i for x in (40, 60, 80, 100)] for i in range(0, 16)]
PAN_X_CC = list(range(20, 36))
PAN_Y_CC = list(range(0, 16))
PAN_X_MASTER_CC = 36
PAN_Y_MASTER_CC = 16
LAUNCH_NOTES = [
 0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80, 88, 96, 104, 112, 120]
STOP_NOTES = [1, 9, 17, 25, 33, 41, 49, 57, 65, 73, 81, 89, 97, 105, 113, 121]
MUTE_NOTES = [2, 10, 18, 26, 34, 42, 50, 58, 66, 74, 82, 90, 98, 106, 114, 122]
SOLO_NOTES = [3, 11, 19, 27, 35, 43, 51, 59, 67, 75, 83, 91, 99, 107, 115, 123]
MONITOR_NOTES = [4, 12, 20, 28, 36, 44, 52, 60, 68, 76, 84, 92, 100, 108, 116, 124]
ARM_NOTES = [5, 13, 21, 29, 37, 45, 53, 61, 69, 77, 85, 93, 101, 109, 117, 125]
CROSS_AB_NOTES = [6, 14, 22, 30, 38, 46, 54, 62, 70, 78, 86, 94, 102, 110, 118, 126]
LV1_FX3_CCS = [
 57, 77, 97, 117]
LV1_FX4_CCS = [58, 78, 98, 118]
LV1_FX1_JOY_X_CC = 37
LV1_FX1_JOY_Y_CC = 17
LV1_FX2_JOY_X_CC = 38
LV1_FX2_JOY_Y_CC = 18
FX1_JOY_X_CC = 38
FX1_JOY_Y_CC = 36
FX2_JOY_X_CC = 39
FX2_JOY_Y_CC = 37
SCENE_SCROLL_CC = 41
CUE_VOLUME_CC = 40
LV1_CUE_VOLUME_CC = 17
MAIN_VOLUME_CC = 17
LV1_MAIN_VOLUME_CC = 16
SCENE_UP_NOTE = 33
SCENE_DOWN_NOTE = 34
CROSSFADER_CC = 18
LV1_CROSSFADER_CC = 19
TRACK_SELECT_NOTES = list(range(16, 32))
MASTER_TRACK_SELECT_NOTE = 32
CLIP_SELECT_NOTE = 103
SCENE_LAUNCH_NOTE = 0
SCENE_STOP_NOTE = 1
MASTER_LAUNCH_NOTE = 0
MASTER_STOP_NOTE = 1
MASTER_MUTE_NOTE = 2
MASTER_SOLO_NOTE = 3
MASTER_MONITOR_NOTE = 4
MASTER_ARM_NOTE = 5
CLIP_TRANSPOSE_CC = 20
CLIP_GAIN_CC = 21
CLIP_LOOP_START_CC = 22
CLIP_LOOP_END_CC = 23
CLIP_CCS = [20, 21, 22, 23]
CLIP_A_NOTE = 104
CLIP_STARTPOINT_NOTE = 105
CLIP_LOOP_STARTPOINT_NOTE = 106
CLIP_LOOP_ENDPOINT_NOTE = 107
FX3_CCS = [
 24, 25, 26, 27]
FX3_NOTES = [108, 109, 110, 111]
FX4_CCS = [28, 29, 30, 31]
FX4_NOTES = [112, 113, 114, 115]
FX5_CCS = [32, 33, 34, 35]
FX5_NOTES = [116, 117, 118, 119]
MASTER_EQ_CCS = [
 56, 76, 96, 116]
VOLUME_CCS = list(range(0, 16))
SCENE_LAUNCH_NOTES = [
 8, 9, 10, 11, 12, 13, 14, 15, 39, 40, 41, 42]
GLOBAL_PLAY_NOTE = 35
GLOBAL_STOP_NOTE = 36
SESSION_ARRANGE_SWITCH_NOTE = 37
CLIP_TRACK_SWITCH_NOTE = 38
MASTER_SEND_A_CC = 56
MASTER_SEND_B_CC = 76
MASTER_SEND_C_CC = 96
MASTER_SEND_D_CC = 116
MASTER_SEND_CCS = [
 56, 76, 96, 116]
EQ_CCS = [[x + i for x in (40, 60, 80, 100)] for i in range(0, 16)]
SLOT_LAUNCH_NOTES1 = [list(range(i * 8, i * 8 + 6)) for i in range(0, 16)]
SLOT_LAUNCH_NOTES2 = [
 [
  6, 7, 55, 56, 57, 58],
 [
  14, 15, 59, 60, 61, 62],
 [
  22, 23, 63, 64, 65, 66],
 [
  30, 31, 67, 68, 69, 70],
 [
  38, 39, 71, 72, 73, 74],
 [
  46, 47, 75, 76, 77, 78],
 [
  54, 55, 79, 80, 81, 82],
 [
  62, 63, 83, 84, 85, 86],
 [
  70, 71, 87, 88, 89, 90],
 [
  78, 79, 91, 92, 93, 94],
 [
  86, 87, 95, 96, 97, 98],
 [
  94, 95, 99, 100, 101, 102],
 [
  102, 103],
 [
  110, 111],
 [
  118, 119],
 [
  126, 127]]
STATUS_MASK = 240
CHAN_MASK = 15
CC_STATUS = 176
NOTEON_STATUS = 144
NOTEOFF_STATUS = 128
STATUS_ON = 127
STATUS_OFF = 0
STATUS_OFF2 = 64