from .NeomowBaseSensor import NeomowBaseSensor
from ..coordinator import NeomowCoordinator

class NeomowMapSensor(NeomowBaseSensor):
    """Map sensor for Neomow that provides SVG visualization."""

    def __init__(self, coordinator: NeomowCoordinator) -> None:
        """Initialize the map sensor."""
        super().__init__(coordinator)
        self._attr_name = f"Neomow {coordinator._device_id} Map"
        self._attr_unique_id = f"neomow_{coordinator._device_id}_map"
        self._attr_object_id = f"neomow_{coordinator._device_id}_map"
        self._attr_icon = "mdi:map"

    def _generate_svg(self, map_data, path_data, robot_x, robot_y, robot_direction) -> str:
        """Generate SVG string from map data."""
        if not map_data or not map_data.get("mapDataList") or not map_data["mapDataList"][0]:
            return ""

        # Find bounds
        min_x = float('inf')
        min_y = float('inf')
        max_x = float('-inf')
        max_y = float('-inf')
        
        # Include map bounds
        if map_data["mapDataList"][0].get("mowingArea"):
            for area in map_data["mapDataList"][0]["mowingArea"]:
                if area.get("elementPointList"):
                    for point in area["elementPointList"]:
                        min_x = min(min_x, point["x"])
                        max_x = max(max_x, point["x"])
                        min_y = min(min_y, point["y"])
                        max_y = max(max_y, point["y"])

        # Include path bounds if available
        if path_data and path_data.get("pathList") and path_data["pathList"][0].get("pathPointList"):
            for point in path_data["pathList"][0]["pathPointList"]:
                min_x = min(min_x, point["x"])
                max_x = max(max_x, point["x"])
                min_y = min(min_y, point["y"])
                max_y = max(max_y, point["y"])

        # Include robot position in bounds if available
        if robot_x is not None and robot_y is not None:
            min_x = min(min_x, robot_x)
            max_x = max(max_x, robot_x)
            min_y = min(min_y, robot_y)
            max_y = max(max_y, robot_y)

        # Add padding
        padding = 50
        min_x -= padding
        min_y -= padding
        max_x += padding
        max_y += padding

        # Calculate dimensions
        width = max_x - min_x
        height = max_y - min_y

        # Start SVG
        svg = f'<svg viewBox="{min_x} {min_y} {width} {height}" xmlns="http://www.w3.org/2000/svg">'
        svg += f'<g transform="rotate(-90) scale(1, -1) translate(0, {-(min_y * 2 + height)})">'

        # Draw mowing areas
        if map_data["mapDataList"][0].get("mowingArea"):
            for area in map_data["mapDataList"][0]["mowingArea"]:
                if area.get("elementPointList") and len(area["elementPointList"]) > 0:
                    path_data = ""
                    for i, point in enumerate(area["elementPointList"]):
                        if i == 0:
                            path_data += f"M {point['x']} {point['y']} "
                        else:
                            path_data += f"L {point['x']} {point['y']} "
                    path_data += "Z"
                    fill_color = "#c8f1e1" if area["elementPointList"][0].get("attr") == 0 else "#eb584d"
                    svg += f'<path d="{path_data}" fill="{fill_color}" stroke="#c4ffed" stroke-width="20"/>'

        # Draw exclusion areas
        if map_data["mapDataList"][0].get("exclusionArea"):
            for area in map_data["mapDataList"][0]["exclusionArea"]:
                if area.get("elementPointList") and len(area["elementPointList"]) > 0:
                    path_data = ""
                    for i, point in enumerate(area["elementPointList"]):
                        if i == 0:
                            path_data += f"M {point['x']} {point['y']} "
                        else:
                            path_data += f"L {point['x']} {point['y']} "
                    path_data += "Z"
                    svg += f'<path d="{path_data}" fill="#eb584d" stroke="#eb584d"/>'

        # Draw base station
        if (map_data["mapDataList"][0].get("baseStation") and 
            map_data["mapDataList"][0]["baseStation"][0].get("elementPointList") and 
            map_data["mapDataList"][0]["baseStation"][0]["elementPointList"][0]):
            point = map_data["mapDataList"][0]["baseStation"][0]["elementPointList"][0]
            svg += f'<rect x="{point["x"] - 50}" y="{point["y"] - 50}" width="100" height="100" fill="blue"/>'

        # Draw path if available
        if path_data and path_data.get("pathList") and path_data["pathList"][0].get("pathPointList"):
            path_data = ""
            for i, point in enumerate(path_data["pathList"][0]["pathPointList"]):
                if i == 0:
                    path_data += f"M {point['x']} {point['y']} "
                else:
                    path_data += f"L {point['x']} {point['y']} "
            svg += f'<path d="{path_data}" fill="none" stroke="#10B981" stroke-width="2"/>'

            # Draw current position
            last_point = path_data["pathList"][0]["pathPointList"][-1]
            svg += f'<circle cx="{last_point["x"]}" cy="{last_point["y"]}" r="5" fill="#EF4444"/>'

        # Draw robot position if available
        if robot_x is not None and robot_y is not None:
            # Robot body
            svg += f'<circle cx="{robot_x}" cy="{robot_y}" r="30" fill="#3B82F6"/>'
            svg += f'<circle cx="{robot_x}" cy="{robot_y}" r="14" fill="#FFFFFF"/>'

            # Direction indicator
            if robot_direction is not None:
                angle = (robot_direction - 90) * 3.14159 / 180  # Convert to radians and adjust for SVG
                line_length = 40
                end_x = robot_x + (line_length * (angle))
                end_y = robot_y + (line_length * (angle))
                svg += f'<line x1="{robot_x}" y1="{robot_y}" x2="{end_x}" y2="{end_y}" stroke="#FFFFFF" stroke-width="4" stroke-linecap="round"/>'

        svg += '</g></svg>'
        return svg

    @property
    def native_value(self) -> str | None:
        """Return the map as an SVG string."""
        if not self.coordinator.data:
            return None

        map_data = self.coordinator.data.get("mapData")
        path_data = self.coordinator.data.get("pathList")
        robot_x = self.coordinator.data.get("robotX")
        robot_y = self.coordinator.data.get("robotY")
        robot_direction = self.coordinator.data.get("robotNavigation")

        return self._generate_svg(map_data, path_data, robot_x, robot_y, robot_direction)

    @property
    def extra_state_attributes(self) -> dict:
        """Return additional state attributes."""
        if not self.coordinator.data:
            return {}

        return {
            "robot_x": self.coordinator.data.get("robotX"),
            "robot_y": self.coordinator.data.get("robotY"),
            "robot_direction": self.coordinator.data.get("robotNavigation"),
            "map_data": self.coordinator.data.get("mapData"),
            "path_data": self.coordinator.data.get("pathList")
        } 