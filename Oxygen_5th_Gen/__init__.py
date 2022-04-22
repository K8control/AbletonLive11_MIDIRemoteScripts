# decompyle3 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.8.9 (default, Mar 30 2022, 13:51:17) 
# [Clang 13.1.6 (clang-1316.0.21.2.3)]
# Embedded file name: output/Live/mac_64_static/Release/python-bundle/MIDI Remote Scripts/Oxygen_5th_Gen/__init__.py
# Compiled at: 2021-11-23 12:54:43
# Size of source mod 2**32: 885 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, REMOTE, SCRIPT, controller_id, inport, outport
from .oxygen_5th_gen import Oxygen_5th_Gen

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=1891,
                          product_ids=[
                         1, 2, 3],
                          model_name=[
                         'Oxygen 25 MKV', 'Oxygen 49 MKV', 'Oxygen 61 MKV']), 
     
     PORTS_KEY: [
                 inport(props=[NOTES_CC, REMOTE]),
                 inport(props=[NOTES_CC, SCRIPT]),
                 outport(props=[]),
                 outport(props=[SCRIPT])]}


def create_instance(c_instance):
    return Oxygen_5th_Gen(c_instance=c_instance)