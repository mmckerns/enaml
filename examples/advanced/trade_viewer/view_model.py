#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
""" Trade Viewer example view models.

This module defines a few simple classes that help drive the Trade
Viewer ui components. The classes provide very thin management of 
the data table models that are used by the various TableViews in 
the ui.

"""
from traits.api import HasTraits, Instance, Str, Property, Dict

from books import BOOKS
from trade_table_model import TradeTable, ReportTable


class EventsModel(HasTraits):

    trade_table = Instance(TradeTable)

    _books = Dict(BOOKS)

    book_choices = Property(depends_on='_books')

    book_choice = Str('ALL')

    def _trade_table_default(self):
        book = self._books[self.book_choice]
        return TradeTable(book)
    
    def _get_book_choices(self):
        return sorted(self._books.keys())
    
    def _book_choice_changed(self, choice):
        book = self._books[choice]
        self.trade_table.book =  book


class ReportModel(HasTraits):

    report_table = Instance(ReportTable, ())

    
class ViewModel(HasTraits):

    events_model = Instance(EventsModel, ())

    report_model = Instance(ReportModel, ())

