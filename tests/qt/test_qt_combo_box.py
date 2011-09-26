#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from ..common import combo_box
from enaml.toolkit import qt_toolkit

class TestQtComboBox(combo_box.TestComboBox):
    """ QtComboBox tests. """

    toolkit = qt_toolkit()

    def get_selected_text(self, widget):
        """ Get the current selected text of a combo box.

        """
        return widget.currentText()

    def get_item_text(self, widget, index):
        """ Get the text of a combo box item at a particular index.

        """
        return widget.itemText(index)

    def select_item(self, widget, index):
        """ Fire an event to simulate the selection of an item.
        
        """
        widget.setCurrentIndex(index)
        
