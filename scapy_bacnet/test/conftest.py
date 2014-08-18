# -*- coding: UTF-8 -*-
'''
@since: 12.08.2014
'''


import os.path

from scapy.all import *

import pytest

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

from bacnet import BVLC, BACNET_PORT, NPDU, APDU


@pytest.fixture
def bind_bvlc():
    bind_layers(UDP, BVLC, sport=BACNET_PORT)
    bind_layers(UDP, BVLC, dport=BACNET_PORT)


@pytest.fixture
def bind_apdu():
    bind_bvlc()
    bind_layers(BVLC, NPDU)
    bind_layers(NPDU, APDU)
