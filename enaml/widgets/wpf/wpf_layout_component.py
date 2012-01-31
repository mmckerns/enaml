#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from .wpf_component import WPFComponent
from .wpf_sizable import WPFSizable
from .wpf_stylable import WPFStylable

from ..layout_component import AbstractTkLayoutComponent


class WPFLayoutComponent(WPFComponent, WPFSizable, WPFStylable,
                         AbstractTkLayoutComponent):
    """ A WPF implementation of LayoutComponent.

    """
    pass

