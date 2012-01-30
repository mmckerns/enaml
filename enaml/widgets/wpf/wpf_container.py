#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
import weakref

import wpyf

from ..container import AbstractTkContainer


class WPFContainer(AbstractTkContainer):
    """ A WPF implementation of Container.

    """
    def create(self, parent):
        """ Creates the underlying WPF widget.

        """
        self.widget = None

    def initialize(self):
        """ Initializes the widget.

        """
        super(WPFContainer, self).initialize()

    def bind(self):
        """ Binds the signal handlers for the widget.

        """
        super(WPFContainer, self).bind()
