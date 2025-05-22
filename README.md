# Neomow Home Assistant Integration

A custom integration for Home Assistant that enables communication with Neomow robotic lawn mowers.

## Features

- Integration with Neomow robotic lawn mowers
- Status monitoring
- Map parsing (in development)
- Customizable sensors and binary sensors

## Installation

1. Navigate to your Home Assistant custom components directory:
```bash
cd homeassistant/config/custom_components/
```

2. Clone this repository:
```bash
git clone https://github.com/pjevsen683/neomow-hass.git
```

Note: The `config` folder is located in the same directory as your `configuration.yaml` file.

## Configuration

Go to integrations and search for neomow and add it. then enter your serial number, and how often it should update.
Later, i will make this more dynamic, e.g. when the battery is full dont poll anymore.

When everything is setup, open your Neomow mobile app to make this integration get the access token and then it should run by self.


## Development Status

This integration is currently in early development stages. The following features are implemented:
- ✅ Status message parsing
- 🚧 Map parsing (in progress)

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

### Adding New Sensors

To add new sensors:
1. Copy an existing sensor from either `sensors` or `binary_sensors` directory
2. Modify the sensor according to your needs
3. Add the new sensor to the `__init__.py` file in the corresponding folder

## License

Use as you please.

## Support

For support, please [open an issue](https://github.com/pjevsen683/neomow-hass/issues) on GitHub.