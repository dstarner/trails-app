import os
import sys

from decouple import Undefined, UndefinedValueError, config

_Undefined = Undefined()


def is_management_cmd(argv=None):
    if not argv:
        argv = sys.argv
    return len(argv) > 1 and argv[1] in [
        'collectstatic', 'init_local_env', 'makemigrations', 'migrate',
    ]

def is_testing(argv=None):
    """Return True if running django or py.test unit tests.
    """
    if 'PYTEST_CURRENT_TEST' in os.environ.keys():
        return True
    argv = sys.argv if argv is None else argv
    if len(argv) >= 1 and ('py.test' in argv[0] or 'py/test.py' in argv[0]):
        return True
    return len(argv) >= 2 and argv[1] in ['test', 'checks', 'lint'] # noqa: PLR2004


def multi_config(*env_var_names, cast=str, default=_Undefined):
    """Allows loading a config from multiple variable locations
    """
    if not env_var_names:
        raise ValueError('Expected at least 1 environment variable name to be given')
    for env_var in env_var_names:
        try:
            val = config(env_var, cast=cast)
            return val
        except UndefinedValueError:
            pass  # just try the next one

    if not isinstance(default, Undefined):
        return default

    raise UndefinedValueError(
        f'[{"|".join(env_var_names)}] not found. Declare one as an envvar or define a default value.',
    )
