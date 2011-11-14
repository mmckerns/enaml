#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------

from traits.api import HasTraits, Str, Property, cached_property
from enaml.traits_view import configure_traits

class Person(HasTraits):
    first_name = Str
    last_name = Str
    
    #full_name = Property(Str, depends_on=['first_name', 'last_name'])
    
    #@cached_property
    #def _get_full_name(self):
    #    return self.first_name + ' ' + self.last_name

if __name__ == '__main__':
    person = Person(first_name='John', last_name='Citizen')
    configure_traits(person)
