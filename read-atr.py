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

from card.ICC import ISO7816

if __name__ == '__main__':
    def __init__(self):
        '''
        connect smartcard and defines class CLA code for communication
        uses "pyscard" library services

        creates self.CLA attribute with CLA code
        and self.coms attribute with associated "apdu_stack" instance
        '''
    print "Checking ATR Value"

    iso = ISO7816()
    iso.ATR_scan()