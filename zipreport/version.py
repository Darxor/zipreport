ZIPREPORT_VERSION = ["2", "0", "0"]


def get_version():
    return ".".join(ZIPREPORT_VERSION)


__version__ = get_version()
