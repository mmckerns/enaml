#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
import wpyf

from ..sizable import AbstractTkSizable


class WPFSizable(AbstractTkSizable):
    """ A WPF implementation of Sizable.

    """

    def size_hint(self):
        """ Returns a (width, height) tuple of integers which represent
        the suggested size of the widget for its current state, ignoring
        any windowing decorations. This value is used by the layout 
        manager to determine how much space to allocate the widget.

        """
        return (0, 0)

    def layout_geometry(self):
        """ Returns the (x, y, width, height) to of layout geometry
        info for the internal toolkit widget. This should ignore any
        windowing decorations, and may be different than the value
        returned by geometry() if the widget's effective layout rect
        is different from its paintable rect.

        """
        return (0, 0, 1, 1)

    def set_layout_geometry(self, x, y, width, height):
        """ Sets the layout geometry of the internal widget to the 
        given x, y, width, and height values. The parameters passed
        are equivalent semantics to layout_geometry().

        """
        pass

    def geometry(self):
        """ Returns an (x, y, width, height) tuple of geometry info
        for the internal toolkit widget, ignoring any windowing
        decorations.

        """
        return (0, 0, 1, 1)

    def set_geometry(self, x, y, width, height):
        """ Sets the geometry of the internal widget to the given
        x, y, width, and height values, ignoring any windowing 
        decorations.

        """
        pass

    def min_size(self):
        """ Returns the hard minimum (width, height) of the widget, 
        ignoring any windowing decorations. A widget will not be able
        to be resized smaller than this value

        """
        return (0, 0)

    def set_min_size(self, min_width, min_height):
        """ Set the hard minimum width and height of the widget, ignoring
        any windowing decorations. A widget will not be able to be resized 
        smaller than this value.

        """
        pass

    def max_size(self):
        """ Returns the hard maximum (width, height) of the widget, 
        ignoring any windowing decorations. A widget will not be able
        to be resized larger than this value

        """
        return (0, 0)

    def set_max_size(self, max_width, max_height):
        """ Set the hard maximum width and height of the widget, ignoring
        any windowing decorations. A widget will not be able to be resized 
        larger than this value.

        """
        pass

    def size(self):
        """ Returns the size of the internal toolkit widget, ignoring any
        windowing decorations, as a (width, height) tuple of integers.

        """
        return (0, 0)
                
    def resize(self, width, height):
        """ Resizes the internal toolkit widget according the given
        width and height integers, ignoring any windowing decorations.

        """
        pass

    def pos(self):
        """ Returns the position of the internal toolkit widget as an
        (x, y) tuple of integers, including any windowing decorations. 
        The coordinates should be relative to the origin of the widget's 
        parent, or to the screen if the widget is toplevel.

        """
        return (0, 0)
            
    def move(self, x, y):
        """ Moves the internal toolkit widget according to the given
        x and y integers which are relative to the origin of the
        widget's parent and includes any windowing decorations.

        """
        pass

