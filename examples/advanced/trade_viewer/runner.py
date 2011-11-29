#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
""" Trade Viewer Runner Script

This is the main runnable Python script for the Trade Viewer example.
To execute, simply issue the following command from this directory:

$ python runner.py 

"""
import enaml

from view_model import ViewModel

with enaml.imports():
    from trade_viewer import TradeViewerWindow


if __name__ == '__main__':
    view = TradeViewerWindow(ViewModel())
    view.show()

