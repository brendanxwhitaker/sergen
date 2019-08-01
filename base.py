# coding=utf-8
# pynput
# Copyright (C) 2015-2018 Moses Palmér
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
This module contains the base implementation.

The actual interface to mouse classes is defined here, but the implementation
is located in a platform dependent module.
"""

# pylint: disable=R0903
# We implement stubs

import enum

from pynput._util import AbstractListener
from pynput import _logger

# pylint: disable=W0223; This is also an abstract class
class Listener(AbstractListener):
    """A listener for mouse events.

    Instances of this class can be used as context managers. This is equivalent
    to the following code::

        listener.start()
        try:
            listener.wait()
            with_statements()
        finally:
            listener.stop()

    This class inherits from :class:`threading.Thread` and supports all its
    methods. It will set :attr:`daemon` to ``True`` when created.

    :param callable on_move: The callback to call when mouse move events occur.

        It will be called with the arguments ``(x, y)``, which is the new
        pointer position. If this callback raises :class:`StopException` or
        returns ``False``, the listener is stopped.

    :param callable on_click: The callback to call when a mouse button is
        clicked.

        It will be called with the arguments ``(x, y, button, pressed)``,
        where ``(x, y)`` is the new pointer position, ``button`` is one of the
        :class:`Button` values and ``pressed`` is whether the button was
        pressed.

        If this callback raises :class:`StopException` or returns ``False``,
        the listener is stopped.

    :param callable on_scroll: The callback to call when mouse scroll
        events occur.

        It will be called with the arguments ``(x, y, dx, dy)``, where
        ``(x, y)`` is the new pointer position, and ``(dx, dy)`` is the scroll
        vector.

        If this callback raises :class:`StopException` or returns ``False``,
        the listener is stopped.

    :param bool suppress: Whether to suppress events. Setting this to ``True``
        will prevent the input events from being passed to the rest of the
        system.

    :param kwargs: Any non-standard platform dependent options. These should be
        prefixed with the platform name thus: ``darwin_``, ``xorg_`` or
        ``win32_``.

        Supported values are:

        ``darwin_intercept``
            A callable taking the arguments ``(event_type, event)``, where
            ``event_type`` is any mouse related event type constant, and
            ``event`` is a ``CGEventRef``.

            This callable can freely modify the event using functions like
            ``Quartz.CGEventSetIntegerValueField``. If this callable does not
            return the event, the event is suppressed system wide.

        ``win32_event_filter``
            A callable taking the arguments ``(msg, data)``, where ``msg`` is
            the current message, and ``data`` associated data as a
            `MSLLHOOKSTRUCT <https://msdn.microsoft.com/en-us/library/windows/desktop/ms644970(v=vs.85).aspx>`_.

            If this callback returns ``False``, the event will not
            be propagated to the listener callback.

            If ``self.suppress_event()`` is called, the event is suppressed
            system wide.
    """
    def __init__(self, on_move=None, on_click=None, on_scroll=None,
                 suppress=False, **kwargs):
        self._log = _logger(self.__class__)
        prefix = self.__class__.__module__.rsplit('.', 1)[-1][1:] + '_'
        self._options = {
            key[len(prefix):]: value
            for key, value in kwargs.items()
            if key.startswith(prefix)}
        super(Listener, self).__init__(
            on_move=on_move, on_click=on_click, on_scroll=on_scroll,
            suppress=suppress)
# pylint: enable=W0223
