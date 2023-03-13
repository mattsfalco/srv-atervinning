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

<a href="https://www.buymeacoffee.com/B4dsANbGFE"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=B4dsANbGFE&button_colour=2e9cb8&font_colour=ffffff&font_family=Poppins&outline_colour=ffffff&coffee_colour=FFDD00" /></a>

###### Author: @mattsfalco (Matthew Falco)