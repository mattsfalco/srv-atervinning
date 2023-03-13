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
   street: Vädersjövägen 25A
   city: Tungelsta
 ```

Note: Exact street required in order to fetch the correct containers.

###### Author: @mattsfalco (Matthew Falco)