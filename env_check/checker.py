import os

class EnvMissingError(Exception):
    """Raised when a required environment variable is missing."""
    pass

def check_env(required_keys, warn_only=False):
    """
    Checks if required environment variables exist.

    :param required_keys: list of keys to check
    :param warn_only: if True, missing keys only print warning
    :raises EnvMissingError: if warn_only=False and key missing
    """
    missing = []

    for key in required_keys:
        if key not in os.environ or os.environ[key] == "":
            missing.append(key)

    if missing:
        msg = f"[django-env-check] Missing environment variables: {', '.join(missing)}"

        if warn_only:
            print("WARNING:", msg)
        else:
            raise EnvMissingError(msg)

    return True
