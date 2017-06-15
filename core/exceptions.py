"""
 * This module defines common exceptions classes that can be reused in any application, and are not replaceable by built-in exceptions.
 * https://github.com/RobertoPrevato/PythonMySQL
 *
 * Copyright 2017, Roberto Prevato
 * https://robertoprevato.github.io
 *
 * Licensed under the MIT license:
 * http://www.opensource.org/licenses/MIT
"""

class InvalidOperation(RuntimeError):
    """
    Exception to raise upon invalid operations - i.e. operations that don't make sense in their context.
    """
    pass


class ConfigurationError(Exception):
    """
    Exception to raise upon configuration error - i.e. when a configuration file is misconfigured.
    """
    pass


class NotFoundException(RuntimeError):
    """
    Exception risen when an expected object was not found.
    """
    pass

class ArgumentNullException(RuntimeError):
    def __init__(self, param_name):
        super().__init__("Parameter cannot be null or empty: `%s`" % param_name)


class InvalidArgument(Exception):
    pass


class WaitException(Exception):
    """Exception risen when the user should wait to perform an operation"""


class NotFoundException(RuntimeError):
    """
    Exception risen when an expected object was not found.
    """
    pass