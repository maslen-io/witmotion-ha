"""WitMotion BLE & Modbus Integration for Home Assistant."""
import asyncio
import logging
from homeassistant.core import HomeAssistant
from homeassistant.components import bluetooth
from homeassistant.helpers import config_validation as cv
from bleak import BleakClient
from bleak_retry_connector import establish_connection

_LOGGER = logging.getLogger(__name__)

DOMAIN = "witmotion"
CONFIG_SCHEMA = cv.empty_config_schema(DOMAIN)
NOTIFY_UUID = "0000ffe4-0000-1000-8000-00805f9a34fb"

def to_int16(low, high):
    val = (high << 8) | low
    return val - 65536 if val & 0x8000 else val

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Set up the WitMotion integration."""
    _LOGGER.info("Starting WitMotion sensor integration")
    return True
