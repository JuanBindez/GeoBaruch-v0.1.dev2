# GeoBaruch: geolocation app
# Copyright (C) 2023  Juan Bindez   <juanbindez780@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of version 2 of the GNU General Public License as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import toga
from toga.style import Pack
from toga.style.pack import COLUMN, RIGHT, LEFT, CENTER
import geocoder


class GeoBaruch(toga.App):
    def get_location(self, widget):
        """
        Callback function when the button is clicked to get the device's location.
        """
        g = geocoder.ip('me')
        if g.latlng:
            latitude, longitude = g.latlng
            self.location_label.text = f"Latitude: {latitude}\nLongitude: {longitude}"
        else:
            self.location_label.text = "Unable to get location."

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        
        main_box = toga.Box(style=Pack(direction=COLUMN))

        button = toga.Button('Get Location', on_press=self.get_location)

        self.location_label = toga.Label('Location:', style=Pack(padding=10))

        # Create a label for copyright
        self.copyright_label = toga.Label('Copyright (C) 2023  Juan Bindez',
                                          style=Pack(text_align=CENTER))

        # Add the button, location label, and copyright label to the main box
        main_box.add(button)
        main_box.add(self.location_label)
        main_box.add(self.location_label)
        main_box.add(self.copyright_label)

        self.main_window = toga.MainWindow(title=self.formal_name, size=(200, 150))
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return GeoBaruch()
