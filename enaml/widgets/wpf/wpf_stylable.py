#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
import wpyf

from ..stylable import AbstractTkStylable


class WPFStylable(AbstractTkStylable):
    """ A WPF implementation of Stylable.

    """
    def initialize(self):
        """ Initialize the attributes of the underlying widget.

        """
        super(WPFStylable, self).initialize()
        shell = self.shell_obj
        if shell.bg_color:
            self.set_bg_color(shell.bg_color)
        if shell.fg_color:
            self.set_fg_color(shell.fg_color)
        if shell.font:
            self.set_font(shell.font)
    
    #--------------------------------------------------------------------------
    # Shell Object Change Handlers 
    #--------------------------------------------------------------------------
    def shell_bg_color_changed(self, color):
        """ The change handler for the 'bg_color' attribute on the shell
        object. Sets the background color of the internal widget to the 
        given color.
        
        """
        self.set_bg_color(color)
    
    def shell_fg_color_changed(self, color):
        """ The change handler for the 'fg_color' attribute on the shell
        object. Sets the foreground color of the internal widget to the 
        given color.

        """
        self.set_fg_color(color)

    def shell_font_changed(self, font):
        """ The change handler for the 'font' attribute on the shell 
        object. Sets the font of the internal widget to the given font.

        """
        self.set_font(font)

    #--------------------------------------------------------------------------
    # Widget Update Methods 
    #--------------------------------------------------------------------------
    def set_bg_color(self, color):
        """ Sets the background color of the widget to an appropriate
        color given the provided Enaml Color object.

        """
        pass

    def set_fg_color(self, color):
        """ Sets the foreground color of the widget to an appropriate
        color given the provided Enaml Color object.

        """
        pass

    def set_font(self, font):
        """ Sets the font of the widget to an appropriate font given 
        the provided Enaml Font object.

        """
        pass

