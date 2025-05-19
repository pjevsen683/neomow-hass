# neomow-hass
Custom integration with neomow and home assistant

To install either do
cd homeassistant/config/custom_components/
git clone https://github.com/pjevsen683/neomow-hass.git

The config folder is the same as where the configuration.yaml is located.


This is still en early stages and is still under development. Please feel free to do with as you like.
You are also very welcome to contrubute in any way.

To add new sensors, simply copy one form either sensors or binary sensors. Update what you want, and remember to add it to the __init__.py file in same folder.
Right now only the STATUS message is parsed on succesfully, but I'm working on the map etc to be parsed aswell.