# Auto-Plant-Waterer

This is a project to help my daughter not have to water the plants in her planter. Later I hope to deploy it through my house to automatically water house plants and only filling their water storage containers every few days. It hopes to use a few tools to help with this:

Sonic Water Depth Sensor (using a filled water container)

12V submergible water pump

Soil Moisture sensor

2-esp8266s using micropython and mqtt to communicate with one another

Leds to for one of the esp8266s to indicate water level of the container. 

For the Raspberry pi broker (i didn't want to use the online broker) I used this tutorial:
      https://randomnerdtutorials.com/testing-mosquitto-broker-and-client-on-raspbbery-pi/
