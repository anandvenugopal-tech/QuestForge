class QuestForgeError(Exception):
    """Base class for all domain-specific errors in QuestForge."""
    pass

class DeadCharacterError(QuestForgeError):
    pass

class InsuffientManaError(QuestForgeError):
    pass

class InvalidActionError(QuestForgeError):
    pass

class InventoryEmptyError(QuestForgeError):
    pass


