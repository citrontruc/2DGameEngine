"""
An interface to create level components.
"""
# levels/components/base_component.py
from abc import ABC
from abc import abstractmethod


class ILevelComponent(ABC):
    @abstractmethod
    def load(self):
        """Retrieve the elements associated to the component (graphics, sound, effects)."""
        pass

    @abstractmethod
    def provides_support(self) -> bool:
        """Check if the element can be stepped on and serve as a platform."""
        pass

    @abstractmethod
    def update(self, delta_time: float):
        """Update component logic each frame if needed."""
        pass

    @abstractmethod
    def draw(self, surface, displacement_list: list):
        """Render the component."""
        pass
