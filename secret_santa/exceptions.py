class SecretSantaError(Exception):
    """Base class for exceptions in this module."""
    pass


class InvalidInputError(SecretSantaError):
    """Raised when there is an issue with the input data (e.g. invalid format or duplicate emails)."""
    pass


class AssignmentImpossibleError(SecretSantaError):
    """Raised when a valid Secret Santa assignment cannot be generated due to constraints."""
    pass
