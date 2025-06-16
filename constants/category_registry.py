from typing import Dict, Optional

from constants.category_handler import CategoryHandler

class CategoryRegistry:
    """Registry for managing different category handlers."""
    
    def __init__(self):
        self._handlers: Dict[str, CategoryHandler] = {}
    
    def register(self, category: str, handler: CategoryHandler):
        """Register a category handler."""
        self._handlers[category] = handler
    
    def get_handler(self, category: str) -> Optional[CategoryHandler]:
        """Get handler for a specific category."""
        return self._handlers.get(category)
    
    def get_available_categories(self) -> list:
        """Get list of available categories."""
        return list(self._handlers.keys())
