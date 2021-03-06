#------------------------------------------------------------------------------
#  Copyright (c) 2013, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
import logging

from enaml.colors import parse_color

from .qt.QtCore import Qt, QSize
from .qt.QtGui import QListWidgetItem, QColor, QIcon, QPixmap, QImage
from .qt_font_utils import QtFontCache
from .qt_object import QtObject


logger = logging.getLogger(__name__)


HORIZONTAL_ALIGN = {
    'left': Qt.AlignLeft,
    'right': Qt.AlignRight,
    'center': Qt.AlignHCenter,
    'justify': Qt.AlignJustify,
}


VERTICAL_ALIGN = {
    'top': Qt.AlignTop,
    'bottom': Qt.AlignBottom,
    'center': Qt.AlignVCenter,
}


CHECKED_STATE = {
    None: None,
    True: Qt.Checked,
    False: Qt.Unchecked,
    Qt.Checked: True,
    Qt.Unchecked: False,
}


class QtListItem(QtObject):
    """ A Qt implementation of an Enaml ListItem.

    """
    # Temporary internal storage for the icon source.
    _icon_source = None

    #--------------------------------------------------------------------------
    # Setup Methods
    #--------------------------------------------------------------------------
    def create_widget(self, parent, tree):
        """ Create the underlying widget.

        """
        # QListWidgetItem is not a QObject and is therefore not used as
        # a widget for this item. The creation of the item is performed
        # explicitly during the parent layout pass.
        self._tree = tree
        self._item = None
        return None

    def create_item(self):
        """ A method called by the parent QtListControl.

        This method is called during the parent layout pass to allow
        the QListWidgetItem to be created. The returned item will be
        uninitialized.

        Returns
        -------
        return : QListWidgetItem
            The uninitialized QListWidgetItem owned by this object.

        """
        # The `item_owner` ref is used by the parent QtListControl
        # to route signals generated by an item back to the QtListItem
        # which owns the underlying widget item.
        self._item = QListWidgetItem()
        self._item.item_owner = self
        return self._item

    def initialize_item(self):
        """ A method called by the parent QtListControl.

        This method is called during the parent layout pass to allow
        the QListWidgetItem to be initialized.

        """
        tree = self._tree
        self._tree = None
        self.set_text(tree['text'])
        self.set_tool_tip(tree['tool_tip'])
        self.set_status_tip(tree['status_tip'])
        self.set_background(tree['background'])
        self.set_foreground(tree['foreground'])
        self.set_font(tree['font'])
        self.set_checkable(tree['checkable'])
        self.set_selectable(tree['selectable'])
        self.set_checked(tree['checked'])
        self.set_selected(tree['selected'])
        self.set_editable(tree['editable'])
        self.set_enabled(tree['enabled'])
        self.set_visible(tree['visible'])
        self.set_text_align(tree['text_align'])
        self.set_vertical_text_align(tree['vertical_text_align'])
        self.set_preferred_size(tree['preferred_size'])
        icon = tree['icon_source']
        if icon:
            # Only create the instance attribute if it's not null.
            # This helps save memory when the number of items is large.
            self._icon_source = icon

    def activate(self):
        """ Activate the underlying item.

        """
        super(QtListItem, self).activate()
        self.set_icon_source(self._icon_source)

    #--------------------------------------------------------------------------
    # Public API
    #--------------------------------------------------------------------------
    def item(self):
        """ Get the widget item associated with this object.

        Returns
        -------
        result : QListWidgetItem or None
            The widget item for this object, or None if the object
            has no widget.

        """
        return self._item

    def destroy(self):
        """ A reimplemented destructor method.

        This method clears the item reference and removes the circular
        reference to the owner item.

        """
        super(QtListItem, self).destroy()
        item = self._item
        if item is not None:
            item.item_owner = None
            self._item = None

    #--------------------------------------------------------------------------
    # Signal Handlers
    #--------------------------------------------------------------------------
    def on_changed(self):
        """ A handler called by the parent list widget from within the
        `itemChanged` signal handler.

        """
        if 'changed' not in self.loopback_guard:
            text = self._item.data(Qt.DisplayRole)
            state = self._item.data(Qt.CheckStateRole)
            content = {'text': text, 'checked': CHECKED_STATE[state]}
            self.send_action('changed', content)

    def on_clicked(self):
        """ A handler called by the parent list widget from within the
        `itemClicked` signal handler.

        """
        self.send_action('clicked', {})

    def on_double_clicked(self):
        """ A handler called by the parent list widget from within the
        `itemDoubleClicked` signal handler.

        """
        self.send_action('double_clicked', {})

    #--------------------------------------------------------------------------
    # Message Handling
    #--------------------------------------------------------------------------
    def on_action_set_text(self, content):
        """ Handle the 'set_text' action from the Enaml item.

        """
        self.set_text(content['text'])

    def on_action_set_tool_tip(self, content):
        """ Handle the 'set_tool_tip' action from the Enaml item.

        """
        self.set_tool_tip(content['tool_tip'])

    def on_action_set_status_tip(self, content):
        """ Handle the 'set_status_tip' action from the Enaml item.

        """
        self.set_status_tip(content['status_tip'])

    def on_action_set_background(self, content):
        """ Handle the 'set_background' action from the Enaml item.

        """
        self.set_background(content['background'])

    def on_action_set_foreground(self, content):
        """ Handle the 'set_foreground' action from the Enaml item.

        """
        self.set_foreground(content['foreground'])

    def on_action_set_font(self, content):
        """ Handle the 'set_font' action from the Enaml item.

        """
        self.set_font(content['font'])

    def on_action_set_icon_source(self, content):
        """ Handle the 'set_icon_source' action from the Enaml item.

        """
        self.set_icon_source(content['icon_source'])

    def on_action_set_checkable(self, content):
        """ Handle the 'set_checkable' action from the Enaml item.

        """
        self.set_checkable(content['checkable'])

    def on_action_set_selectable(self, content):
        """ Handle the 'set_selectable' action from the Enaml item.

        """
        self.set_selectable(content['selectable'])

    def on_action_set_checked(self, content):
        """ Handle the 'set_checked' action from the Enaml item.

        """
        self.set_checked(content['checked'])

    def on_action_set_selected(self, content):
        """ Handle the 'set_selected' action from the Enaml item.

        """
        self.set_selected(content['selected'])

    def on_action_set_editable(self, content):
        """ Handle the 'set_editable' action from the Enaml item.

        """
        self.set_editable(content['editable'])

    def on_action_set_enabled(self, content):
        """ Handle the 'set_enabled' action from the Enaml item.

        """
        self.set_enabled(content['enabled'])

    def on_action_set_visible(self, content):
        """ Handle the 'set_visible' action from the Enaml item.

        """
        self.set_visible(content['visible'])

    def on_action_set_text_align(self, content):
        """ Handle the 'set_text_align' action from the Enaml item.

        """
        self.set_text_align(content['text_align'])

    def on_action_set_vertical_text_align(self, content):
        """ Handle the 'set_vertical_text_align' action from the Enaml
        item.

        """
        self.set_vertical_text_align(content['vertical_text_align'])

    def on_action_set_preferred_size(self, content):
        """ Handle the 'set_preferred_size' action from the Enaml item.

        """
        self.set_preferred_size(content['preferred_size'])

    #--------------------------------------------------------------------------
    # Widget Update Methods
    #--------------------------------------------------------------------------
    # Note: Qt's abstract item views handle invalid QVariants differently
    # than they handle an invalid value of a particular type. The code in
    # these setters therefore sets the data using roles instead of the
    # more convenient setter methods. Every data change is guarded to
    # prevent loopback for a change that was not initiated by the user.

    def set_text(self, text):
        """ Set the text for the list item.

        """
        with self.loopback_guard('changed'):
            self._item.setData(Qt.DisplayRole, text or None)

    def set_tool_tip(self, tool_tip):
        """ Set the tool tip for the list item.

        """
        with self.loopback_guard('changed'):
            self._item.setData(Qt.ToolTipRole, tool_tip or None)

    def set_status_tip(self, status_tip):
        """ Set the status tip for the list item.

        """
        with self.loopback_guard('changed'):
            self._item.setData(Qt.StatusTipRole, status_tip or None)

    def set_background(self, background):
        """ Set the background color for the list item.

        """
        qcolor = None
        if background:
            color = parse_color(background)
            if color is not None:
                qcolor = QColor.fromRgbF(*color)
        with self.loopback_guard('changed'):
            self._item.setData(Qt.BackgroundRole, qcolor)

    def set_foreground(self, foreground):
        """ Set the foreground color for the list item.

        """
        qcolor = None
        if foreground:
            color = parse_color(foreground)
            if color is not None:
                qcolor = QColor.fromRgbF(*color)
        with self.loopback_guard('changed'):
            self._item.setData(Qt.ForegroundRole, qcolor)

    def set_font(self, font):
        """ Set the font for the list item.

        """
        item = self._item
        if not font:
            if item.data(Qt.FontRole) is not None:
                item.setData(Qt.FontRole, None)
        else:
            # XXX this may warrant more work
            parent = self.parent()
            cache = getattr(parent, '_items_font_cache', None)
            if cache is None:
                pfont = parent.widget().font()
                cache = parent._items_font_cache = QtFontCache(pfont)
            item.setData(Qt.FontRole, cache[font])

    def set_icon_source(self, icon_source):
        """ Set the icon source for the list item.

        """
        if icon_source:
            loader = self._session.load_resource(icon_source)
            loader.on_load(self._on_icon_load)
        else:
            with self.loopback_guard('changed'):
                self._item.setData(Qt.DecorationRole, None)

    def set_checkable(self, checkable):
        """ Set the checkable state for the list item.

        """
        self._set_item_flag(Qt.ItemIsUserCheckable, checkable)

    def set_selectable(self, selectable):
        """ Set the selectable state for the list item.

        """
        self._set_item_flag(Qt.ItemIsSelectable, selectable)

    def set_checked(self, checked):
        """ Set the checked state for the list item.

        """
        with self.loopback_guard('changed'):
            self._item.setData(Qt.CheckStateRole, CHECKED_STATE[checked])

    def set_selected(self, selected):
        """ Set the selected state for the list item.

        """
        # Note that the item must be parented for this to have effect.
        self._item.setSelected(selected)

    def set_editable(self, editable):
        """ Set the editable state for the list item.

        """
        self._set_item_flag(Qt.ItemIsEditable, editable)

    def set_enabled(self, enabled):
        """ Set the enabled state for the list item.

        """
        self._set_item_flag(Qt.ItemIsEnabled, enabled)

    def set_visible(self, visible):
        """ Set the visible state for the list item.

        """
        # Note that the item must be parented for this to have effect.
        self._item.setHidden(not visible)

    def set_text_align(self, align):
        """ Set the horizontal text alignment for the list item.

        """
        # Use the convenience getter and setters instead of the `data`
        # method, since the latter is broken on PySide; likely to do
        # with its conversion of the align flag into a QVariant.
        item = self._item
        flags = item.textAlignment()
        flags &= ~Qt.AlignHorizontal_Mask
        flags |= HORIZONTAL_ALIGN[align]
        with self.loopback_guard('changed'):
            item.setTextAlignment(flags)

    def set_vertical_text_align(self, align):
        """ Set the vertical text alignment for the list item.

        """
        # Use the convenience getter and setters instead of the `data`
        # method, since the latter is broken on PySide; likely to do
        # with its conversion of the align flag into a QVariant.
        item = self._item
        flags = item.textAlignment()
        flags &= ~Qt.AlignVertical_Mask
        flags |= VERTICAL_ALIGN[align]
        with self.loopback_guard('changed'):
            item.setTextAlignment(flags)

    def set_preferred_size(self, preferred_size):
        """ Set the preferred size for the list item.

        """
        size = QSize(*preferred_size)
        if not size.isValid():
            size = None
        with self.loopback_guard('changed'):
            self._item.setData(Qt.SizeHintRole, size)

    #--------------------------------------------------------------------------
    # Private API
    #--------------------------------------------------------------------------
    def _set_item_flag(self, flag, enabled):
        """ Set or unset the given item flag for the item.

        """
        item = self._item
        flags = item.flags()
        if enabled:
            flags |= flag
        else:
            flags &= ~flag
        with self.loopback_guard('changed'):
            item.setFlags(flags)

    def _on_icon_load(self, icon):
        """ A private resource loader callback.

        This method is invoked when the requested icon is successfully
        loaded. It will update the icon on the item.

        Parameters
        ----------
        icon : QIcon or QImage
            The icon or image that was loaded by the request.

        """
        if isinstance(icon, QImage):
            icon = QIcon(QPixmap.fromImage(icon))
        elif not isinstance(icon, QIcon):
            msg = 'got incorrect type for icon: `%s`'
            logger.error(msg % type(icon).__name__)
            icon = None
        with self.loopback_guard('changed'):
            self._item.setData(Qt.DecorationRole, icon)

