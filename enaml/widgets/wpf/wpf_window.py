#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------

from .wpf_component import WPFComponent
from .wpf_sizable import WPFSizable

from ..window import AbstractTkWindow


class WPFWindow(WPFComponent, WPFSizable, AbstractTkWindow):
    """ A WPF implementation of a Window. It serves as a base class for 
    WPFMainWindow and WPFDialog. It is not meant to be used directly.

    """
    #--------------------------------------------------------------------------
    # Setup methods
    #--------------------------------------------------------------------------
    def create(self, parent):
        """ Create the underlying WPF widget.

        """
        msg = 'A WPFWindow is a base class and cannot be used directly'
        raise NotImplementedError(msg)

    def initialize(self):
        """ Intializes the attributes on the underlying WPF widget.

        """
        super(WPFWindow, self).initialize()
        self.set_title(self.shell_obj.title)
        self.update_central_widget()

    #--------------------------------------------------------------------------
    # Implementation
    #--------------------------------------------------------------------------
    def maximize(self):
        """ Maximizes the window to fill the screen.

        """
        pass
            
    def minimize(self):
        """ Minimizes the window to the task bar.

        """
        pass
            
    def normalize(self):
        """ Restores the window after it has been minimized or maximized.

        """
        pass

    def shell_title_changed(self, title):
        """ The change handler for the 'title' attribute on the shell
        object.

        """
        self.set_title(title)
    
    def shell_central_widget_changed(self, central_widget):
        """ The change handler for the 'central_widget' attribute on 
        the shell object.

        """
        self.update_central_widget()
    
    #--------------------------------------------------------------------------
    # Widget Update Methods 
    #--------------------------------------------------------------------------
    def update_central_widget(self):
        """ Updates the central widget from the value on the shell 
        object. This method must be implemented by subclasses.

        """
        raise NotImplementedError

    def set_title(self, title):
        """ Sets the title of the underlying widget.

        """
        pass

