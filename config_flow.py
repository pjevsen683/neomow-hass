"""Config flow for Neomow integration."""
from __future__ import annotations

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult
from homeassistant.const import CONF_SCAN_INTERVAL

from .const import DOMAIN, DEFAULT_SCAN_INTERVAL

class NeomowConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Neomow."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        if user_input is not None:
            device_id = user_input["device_id"]
            scan_interval = user_input[CONF_SCAN_INTERVAL]
            use_beta = user_input["use_beta"]
            
            # Check if already configured
            await self.async_set_unique_id(device_id)
            self._abort_if_unique_id_configured()
            
            return self.async_create_entry(
                title=f"Neomow {device_id}",
                data={
                    "device_id": device_id,
                    CONF_SCAN_INTERVAL: scan_interval,
                    "use_beta": use_beta
                }
            )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("device_id"): str,
                vol.Required(
                    CONF_SCAN_INTERVAL,
                    default=DEFAULT_SCAN_INTERVAL
                ): vol.All(
                    vol.Coerce(int),
                    vol.Range(min=1)
                ),
                vol.Required("use_beta", default=False): bool,
            })
        ) 