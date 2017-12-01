# -*- coding: UTF-8 -*-
"""
Author Ron Anderson
"""
########################################################################
# script to program INET USIM adding PTCI PLMN to PLMNsel file
########################################################################

from card.ICC import *
from card.SIM import SIM
from card.USIM import USIM
from binascii import hexlify
from struct import unpack, pack
from random import _urandom as urand

# INET HPLMN MCC: 312, MNC: 020
# Pioneer Tel PLMN MCC: 312, MNC: 280
HPLMN = [0x13, 0x02, 0x20]
PTCI_PLMN = [0x13, 0x02, 0x82]

# total of 50 PLMN's so fill in remainder with (dummy) PLMN's value 0xFF
PLMNsel = HPLMN + PTCI_PLMN \
          + 48 * [0xFF, 0xFF, 0xFF]

ISO7816.dbg = 0
UICC.dbg = 0

######################################################
# fixed prefixes
# The ADM and PIN's are for Ron's test SIM only
######################################################

ACC = [0x08, 0x00]
P2_def = 0x00
P2_chv1 = 0x01
P2_chv2 = 0x81
P2_adm = 0x0A
NO_PIN = ''
ADM1 = '47470374'
PIN1 = '1234'
PIN2 = '3191'


# Converts the PIN digits to hex ascii characters
# INET's PIN1 is disabled so the VERIFY will not work
def verify_chv(uicc, chv = PIN1, adm = P2_def):
    print ('Starting verification of PIN: ', chv)
    apdu = [0x30 + int(d) for d in chv if d.isdigit()]
    ret = uicc.VERIFY(P2=adm, Data=apdu)
    if ret[2] == (0x90, 0x00):
        print ('verify_chv SUCCESSFUL')
        return True
    else:
        print ('verify_chv FAILED. RET value: ', ret)
        return False


def program_files(uicc):
    print ('start program_files...')

    uicc.SELECT_FILE(0, 4, [0x3F, 0x00])
    uicc.SELECT_FILE(0, 4, [0x7F, 0x20])
    uicc.SELECT_FILE(0, 4, [0x6F, 0x30])

    print ('PLMNsel EF File selected.')

    # go to PLMNsel address and update binary string for HPLMN
    ret = uicc.UPDATE_BINARY(0, 0, PLMNsel)
    print('Writing PLMN selector: %s' % ret)

if __name__ == '__main__':

    print 'INET USIM card update PLMNsel  with value: '

    u = USIM()
    imsi = u.get_imsi()
    print '====>> IMSI: ' + imsi
    plmnsel_before = u.get_plmnsel()
    print '====>> Current PLMNsel: ' , plmnsel_before
    program_files(u)
    plmnsel_after = u.get_plmnsel()
    print '====>> Modified PLMNsel: ' , plmnsel_after
    u.disconnect()
    print 'INET USIM card PLMNsel update completed'






