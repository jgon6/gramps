#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2014-2015  Nick Hall
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

"""
Class handling displaying of places.
"""

#-------------------------------------------------------------------------
#
# Gramps modules
#
#-------------------------------------------------------------------------
from ..config import config
from ..utils.location import get_location_list
from ..lib import PlaceType

#-------------------------------------------------------------------------
#
# PlaceDisplay class
#
#-------------------------------------------------------------------------
class PlaceDisplay(object):

    def display_event(self, db, event):
        if not event:
            return ""
        place_handle = event.get_place_handle()
        if place_handle:
            place = db.get_place_from_handle(place_handle)
            return self.display(db, place, event.get_date_object())
        else:
            return ""

    def display(self, db, place, date=None):
        if not place:
            return ""
        if not config.get('preferences.place-auto'):
            return place.title
        else:
            lang = config.get('preferences.place-lang')
            places = get_location_list(db, place, date, lang)
            names = [item[0] for item in places]

            if config.get('preferences.place-number'):
                if len(places) > 1 and int(places[0][1]) == PlaceType.NUMBER:
                    names = names[1:]
                    names[0] = places[0][0] + ' ' + names[0]

            if config.get('preferences.place-reverse'):
                names.reverse()

            return ", ".join(names)

displayer = PlaceDisplay()
