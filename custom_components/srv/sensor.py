"""Platform for SRV sensor integration."""
import urllib.request, json, asyncio, hashlib, requests
from datetime import timedelta, date
from urllib import request

import voluptuous as vol
import homeassistant.helpers.config_validation as cv

from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.entity import Entity
from homeassistant.util import Throttle

DOMAIN = "srv"

TODAY = date.today()

CONF_CITY = "city"
CONF_STREET = "street"

MIN_TIME_BETWEEN_UPDATES = timedelta(minutes=60)

SCAN_INTERVAL = timedelta(minutes=30)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {vol.Required(CONF_CITY): cv.string, vol.Required(CONF_STREET): cv.string}
)


def setup_platform(hass, config, add_entities, discovery_info=None) -> None:
    """Set up the SRV sensor platform."""

    sensor_street = config[CONF_STREET]
    sensor_city = config[CONF_CITY]

    entities = []
    containers = CustomerData().get_srv_data(sensor_street, sensor_city)
    for container in containers:
        print(str(container))
        entities.append(SrvSensor(container))

    add_entities(entities)


class CustomerData:
    """Get the containers from SRV."""

    def __init__(self) -> None:
        """Initialize the Class."""

    def get_srv_data(self, street, city):
        """Get the raw container data."""
        params = {"query": street, "city": city}
        return requests.get(
            url="https://www.srvatervinning.se/rest-api/srv-slamsok-rest-new/search",
            headers={},
            params=params,
            timeout=5.000,
        ).json()["results"][0]["containers"]


class SrvSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self, container) -> None:
        """Initialize the sensor."""

        self._data = container

        self._type = self._data["containerType"]
        self._state = self._data["firstCalendarDate"]
        self._unique_id = self._data["containerId"]
        self._content_type = self._data["contentType"]
        self._property_code = self._data["propertyCode"]
        self._address = self._data["address"]
        self._city = self._data["city"]
        self._zip_code = self._data["zipCode"]
        self._customer_id = self._data["customerId"]
        self._calendars = self._data["calendars"]

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._type

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def icon(self):
        """Icon to use in the frontend."""
        if self._content_type == "Matavfall":
            return "mdi:compost"
        if self._content_type == "Restavfall":
            return "mdi:trash-can"
        if self._content_type == "Slamtömning":
            return "mdi:tanker-truck"
        return "mdi:water"

    @property
    def unique_id(self):
        """Unique ID."""
        return self._unique_id

    @property
    def native_value(self):
        """If a datetime is available, return the native_value property."""
        if not self._state == date:
            return None
        return "datetime.date"

    @property
    def extra_state_attributes(self):
        """All remaining fields of interest."""
        attr = {}
        attr["container_id"] = self._unique_id
        attr["customer_id"] = self._customer_id
        attr["content_type"] = self._content_type
        attr["address"] = self._address
        attr["city"] = self._city
        attr["property_code"] = self._property_code
        attr["zip_code"] = self._zip_code
        attr["calendars"] = self._calendars

        return attr
