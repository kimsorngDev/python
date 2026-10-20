class InventoryError(Exception):
    """Base exception for inventory operations."""
    pass


class OutOfStockError(InventoryError):
    """Raised when trying to sell more than available stock."""
    pass


class ProductNotFoundError(ValueError, InventoryError):
    """Raised when a product is not found in the shop."""
    pass


class ProductAlreadyExistsError(ValueError, InventoryError):
    """Raised when trying to add a product with an existing ID."""
    pass


class InvalidQuantityError(ValueError, InventoryError):
    """Raised when an invalid amount (<= 0) is specified."""
    pass
