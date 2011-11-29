#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
""" Trade Viewer example table models.

This module defines the data table models used by the TableViews in the
events tab and the reports tab of the TradeViewer.

"""
from datetime import datetime
from time import asctime

from enaml.item_models.abstract_item_model import AbstractTableModel
from enaml.styling.brush import Brush
from enaml.styling.color import Color


class TradeTable(AbstractTableModel):

    brush_map = {
        'option': Brush(Color.from_string('lightsteelblue'), None),
        'forward': Brush(Color.from_string('paleturquoise'), None),
        'swap': Brush(Color.from_string('khaki'), None),
        'future': Brush(Color.from_string('white'), None),
    }

    @staticmethod
    def format_price(price):
        return '%.2f' % price

    @staticmethod
    def format_timestamp(timestamp):
        tt = datetime.fromtimestamp(timestamp).timetuple()
        return asctime(tt)

    def __init__(self, book):
        super(AbstractTableModel, self).__init__()
        self._book = book
        self._formatters = {
            'Price': self.format_price, 
            'Entry Time': self.format_timestamp,
        }

    def _get_book(self):
        return self._book
    
    def _set_book(self, book):
        self.begin_reset_model()
        self._book = book
        self.end_reset_model()
    
    book = property(_get_book, _set_book)

    def column_count(self, parent=None):
        if parent is not None:
            return 0
        return len(self._book.fields)
    
    def row_count(self, parent=None):
        if parent is not None:
            return 0
        return len(self._book)
    
    def data(self, index):
        book = self._book
        row = index.row
        col = index.column
        field = book.fields[col]
        fmt = self._formatters.get(field, str)
        val = book[row][field]
        return fmt(val)
    
    def horizontal_header_data(self, section):
        return self._book.fields[section]

    def background(self, index):
        row = index.row
        inst = self._book[row]['Instrument']
        return self.brush_map[inst]


class ReportTable(AbstractTableModel):

    bg_brush = Brush(Color.from_string('#ccffcc'), None)

    columns = [
        'Comment', 'Report', 'Priceable', 'Date', 'Last Event',
        'Market State', 'User', 'Created', 'Updated', 'Status', 'Tag'
    ] * 2

    def column_count(self, parent=None):
        if parent is None:
            return len(self.columns)
        return 0
    
    def row_count(self, parent=None):
        if parent is None:
            return 1000
        return 0
    
    def data(self, index):
        return str(index.row)
    
    def background(self, index):
        return self.bg_brush

    def horizontal_header_data(self, section):
        return self.columns[section]

