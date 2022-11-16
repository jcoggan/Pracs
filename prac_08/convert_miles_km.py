from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesKm(App):
    """ ConvertMilesKm is a Kivy App for converting miles to kilometres"""
    output = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "convert miles to kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def convert_to_km(self, text):
        """Converts miles to kilometres"""
        try:
            result = float(text) * MILES_TO_KM
            self.root.ids.output_km.text = str(result)
        except ValueError:
            self.root.ids.output_km.text = '0.0'

    def handle_increment(self, text, increment):
        """Handles incremental increases and decreases"""
        try:
            current_number = float(text)
        except ValueError:
            current_number = 0
        increment = float(increment)
        result = current_number + increment
        self.root.ids.input_miles.text = str(result)


ConvertMilesKm().run()
