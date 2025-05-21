"""Constants for the Neomow integration."""

DOMAIN = "neomow"

# Configuration
CONF_DEVICE_ID = "device_id"
DEFAULT_SCAN_INTERVAL = 10

# MQTT
MQTT_BROKER = "neomowx.app.hookii.com"
MQTT_PORT = 1883
MQTT_USERNAME = "neomow"
MQTT_PASSWORD = "FfO&hyl4RhQ6QRh7c7cpf8HqySdTrTgOWyVRH76CQ%DIbJ!MtUQ7%qQM$9*c2vhC"

BETA_MQTT_BROKER = "neomowx.pre.hookii.com"
BETA_MQTT_USERNAME = "preHookii"
BETA_MQTT_PASSWORD = "uN6vK2yR7wM9sY1z"

# Reconnection
MAX_RECONNECT_ATTEMPTS = 5
RECONNECT_DELAY = 5  # seconds 