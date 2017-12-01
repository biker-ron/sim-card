# -*- coding: UTF-8 -*-
"""
author Ron Anderson
"""


#################################
# Python library to work on
# USIM card
# communication based on ISO7816 card
# and commands and formats based on UICC card
#
# needs pyscard from:
# http://pyscard.sourceforge.net/
#################################

import hashlib
from optparse import OptionParser
import os
import random
import re
import sys

from card.ICC import *
from card.SIM import SIM
from card.USIM import USIM
from binascii import hexlify
from struct import unpack, pack
from random import _urandom as urand

ISO7816.dbg = 0
UICC.dbg = 0

# INET HPLMN MCC: 312, MNC: 020, each BCD encoded, then appended
# Pioneer Tel PLMN MCC: 312, MNC: 280, each BCD encoded, then appended
HPLMN = [0x13, 0x02, 0x20]
PTCI_PLMN = [0x13, 0x02, 0x82]

# total of 50 PLMN's so fill in remainder with (dummy) PLMN's using 0xFF
PLMNsel = HPLMN + PTCI_PLMN \
          + 48 * [0xFF, 0xFF, 0xFF]

if __name__ == '__main__':
    def __init__(self):
        '''
        connect smartcard and defines class CLA code for communication
        uses "pyscard" library services
        '''
    print "Checking ATR Value"

    iso = ISO7816()
    iso.ATR_scan()

    print "List Card Information"

    u = USIM()
    imsi = u.get_imsi()
    acc = u.get_acc()
    spdi = u.get_spdi()
    spdi2 = u.get_spdi_readBinary()
    iccid = u.get_ICCID()
    plmnsel = u.get_plmnsel()

    print " "
    print "------------------------------------"
    print "------------- Results --------------"
    print "------------------------------------"
    print "IMSI: " + imsi
    print "ACCs: " , acc
    print "SPDI: " , spdi
    print "SPDI Read Binary response: ", spdi2
    print "ICCID: " + iccid
    print "PLMNSel" , plmnsel