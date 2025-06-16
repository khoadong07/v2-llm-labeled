from abc import ABC, abstractmethod
from typing import Dict

class CategoryHandler(ABC):
    """Abstract base class for handling different categories."""
    
    @abstractmethod
    def get_labels(self) -> Dict[str, str]:
        """Return the labels dictionary for this category."""
        pass
    
    @abstractmethod
    def get_label_ids(self) -> Dict[str, str]:
        """Return the label IDs dictionary for this category."""
        pass
    
    @abstractmethod
    def get_prompt_template(self) -> str:
        """Return the prompt template for this category."""
        pass
    
    def extract_text(self, data: dict) -> str:
        """Extract text from request data. Can be overridden by subclasses."""
        return data.get("title", "") + " " + data.get("content", "") + " " + data.get("description", "")