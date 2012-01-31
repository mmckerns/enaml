#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
import weakref

from ..component import AbstractTkComponent


class WPFComponent(AbstractTkComponent):
    """ Base component object for the WPF based backend.

    """
    #: The a reference to the shell object. Will be stored as a weakref.
    _shell_obj = lambda self: None

    #: The WPF widget created by the component
    widget = None

    #--------------------------------------------------------------------------
    # Setup Methods
    #--------------------------------------------------------------------------
    def create(self, parent):
        """ Creates the underlying Qt widget. As necessary, subclasses
        should reimplement this method to create different types of
        widgets.

        """
        self.widget = None

    def initialize(self):
        """ Initializes the attributes of the the WPF widget.

        """
        super(WPFComponent, self).initialize()
        self.set_enabled(self.shell_obj.enabled)
    
    def bind(self):
        """ Bind any event handlers for the WPF Widget. By default,
        this is a no-op. Subclasses should reimplement this method as
        necessary to bind any widget event handlers or signals.

        """
        super(WPFComponent, self).bind()

    #--------------------------------------------------------------------------
    # Teardown Methods
    #--------------------------------------------------------------------------
    def destroy(self):
        """ Destroys the underlying WPF widget.

        """
        widget = self.widget
        self.widget = None

    #--------------------------------------------------------------------------
    # Abstract Implementation
    #--------------------------------------------------------------------------
    @property
    def toolkit_widget(self):
        """ A property that returns the toolkit specific widget for this
        component.

        """
        return self.widget

    def _get_shell_obj(self):
        """ Returns a strong reference to the shell object.

        """
        return self._shell_obj()
    
    def _set_shell_obj(self, obj):
        """ Stores a weak reference to the shell object.

        """
        self._shell_obj = weakref.ref(obj)
    
    #: A property which gets a sets a reference (stored weakly)
    #: to the shell object
    shell_obj = property(_get_shell_obj, _set_shell_obj)
        
    def disable_updates(self):
        """ Disable rendering updates for the underlying WPF widget.

        """
        #self.widget.set_updates_enabled(False)
        pass

    def enable_updates(self):
        """ Enable rendering updates for the underlying WPF widget.

        """
        #self.widget.set_updates_enabled(True)
        pass

    #--------------------------------------------------------------------------
    # Shell Object Change Handlers 
    #--------------------------------------------------------------------------
    def shell_enabled_changed(self, enabled):
        """ The change handler for the 'enabled' attribute on the shell
        object.

        """
        self.set_enabled(enabled)

    #--------------------------------------------------------------------------
    # Widget Update Methods
    #--------------------------------------------------------------------------
    def set_enabled(self, enabled):
        """ Enable or disable the widget.

        """
        #self.widget.set_enabled(enabled)
        pass

    def set_visible(self, visible):
        """ Show or hide the widget.

        """
        #self.widget.set_visible(visible)
        pass
