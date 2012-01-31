#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from .wpf.window import Window

from .wpf_window import WPFWindow

from ..main_window import AbstractTkMainWindow


class WPFMainWindow(WPFWindow, AbstractTkMainWindow):
    """ A WPF implementation of a MainWindow.

    """
    #--------------------------------------------------------------------------
    # Setup methods
    #--------------------------------------------------------------------------
    def create(self, parent):
        """ Creates the underlying WPFMainWindow object.

        """
        self.widget = Window()

    def initialize(self):
        """ Initialize the WPFMainWindow object.

        """
        super(WPFMainWindow, self).initialize()
        self.update_menu_bar()

    #--------------------------------------------------------------------------
    # Change Handlers
    #--------------------------------------------------------------------------
    def shell_menu_bar_changed(self, menu_bar):
        """ Update the menu bar of the window with the new value from
        the shell object.

        """
        self.update_menu_bar()

    #--------------------------------------------------------------------------
    # Abstract Implementation
    #--------------------------------------------------------------------------
    def menu_bar_height(self):
        """ Returns the height of the menu bar in pixels. If the menu
        bar does not have an effect on the height of the main window,
        this method returns Zero.

        """
        return 0

    #--------------------------------------------------------------------------
    # Widget Update Methods
    #--------------------------------------------------------------------------
    def update_menu_bar(self):
        """ Updates the menu bar in the main window with the value
        from the shell object.

        """
        menu_bar = self.shell_obj.menu_bar

    def update_central_widget(self):
        """ Updates the central widget in the main window with the 
        value from the shell object.

        """
        # It's possible for the central widget component to be None.
        # This must be allowed since the central widget may be generated
        # by an Include component, in which case it will not exist 
        # during initialization. However, we must have a central widget
        # for the MainWindow, and in that case we just fill it with a
        # dummy widget.
        central_widget = self.shell_obj.central_widget

    def set_visible(self, visible):
        """ Overridden from the parent class to raise the window to
        the front if it should be shown.

        """
        pass

