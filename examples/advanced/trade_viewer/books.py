#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
""" Trade Viewer Book class.

This module defines the simple Book object for the Trade Viewer example.
It is a simple object that wraps a group of trades represented by a 
Numpy structured array. A few predefined Book objects are available 
via the BOOKS dictionary. These books are populated with trades generated
by the the generate_data.py script.

"""
class Book(object):

    def __init__(self, trades):
        self._trades = trades

    def __len__(self):
        return len(self._trades)

    def __getitem__(self, idx):
        return self._trades[idx]
    
    @property
    def fields(self):
        return self._trades.dtype.names
    

def load_trades():
    import numpy as np
    import generate_data
    mm = np.memmap('./trades.arr', mode='r')
    trades = mm.view(generate_data.trade_dt)
    return trades


_trades = load_trades()


BOOKS = {
    'ALL': Book(_trades),
    'EUR': Book(_trades[:2500000]),
    'JPY': Book(_trades[2500000:5000000]),
    'GBP': Book(_trades[5000000:7500000]),
    'SKK': Book(_trades[7500000:]),
}

