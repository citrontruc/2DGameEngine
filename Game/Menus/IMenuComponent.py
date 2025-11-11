"""
An interface to define menu components
Menu components are very similar to LevelComponents.
"""
from abc import ABC
from abc import abstractmethod


class IMenuComponent(ABC):
    @abstractmethod
    def load(self):
        """Retrieve the elements associated to the component (graphics, sound, effects)."""
        pass

    @abstractmethod
    def on_hover(self):
        pass

    @abstractmethod
    def on_click(self):
        pass

    @abstractmethod
    def update(self, delta_time: float):
        """Update component logic each frame if needed."""
        pass

    @abstractmethod
    def draw(self, surface):
        """Render the component."""
        pass
