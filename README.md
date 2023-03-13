[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![BuyMeACoffee]][buymeacoffee]

# Home Assistant SRV Årtervinning Integration
Integration for Home Assistant that generates sensors for individual containers serviced by SRV Årtervinning AB.

This works in Southern Stockholm in the following counties (kommuner):
 - Botkyrka
 - Haninge
 - Huddinge
 - Nynäshamn
 - Salem

Main Container Types:
 - Sewer Containers (Slamavskiljare, Slut Tank etc...)
 - Trash and Compost (Restavfall och Matavfall)



Here is an example of what to add to your sensor section in configuration.yaml: 
 ```yaml
 - platform: srv
   street: Runstensvägen 1
   city: Handen
 ```

Note: Exact street required in order to fetch the correct containers.

<a href="https://www.buymeacoffee.com/mattsfalco"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=mattsfalco&button_colour=2e9cb8&font_colour=ffffff&font_family=Poppins&outline_colour=ffffff&coffee_colour=FFDD00" /></a>

###### Author: @mattsfalco (Matthew Falco)

[buymeacoffee]: https://www.buymeacoffee.com/mattsfalco