"""
An interface to create level components.
"""
# levels/components/base_component.py
from abc import ABC
from abc import abstractmethod


class ILevelComponent(ABC):
    @abstractmethod
    def load(self, world):
        """Retrieve the elements associated to the component (graphics, sound, effects)."""
        pass

    @abstractmethod
    def update(self, dt):
        """Update component logic each frame if needed."""
        pass

    @abstractmethod
    def draw(self, surface):
        """Render the component."""
        pass
