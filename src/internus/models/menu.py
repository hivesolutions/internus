#!/usr/bin/python
# -*- coding: utf-8 -*-

# Internus
# Copyright (c) 2008-2020 Hive Solutions Lda.
#
# This file is part of Internus.
#
# Internus is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Internus is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Internus. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2020 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import datetime

import appier

from . import base

class Menu(base.InternusBase):

    day = appier.field(
        type = int,
        index = True,
        meta = "date"
    )

    dishes = appier.field(
        type = list
    )

    @classmethod
    def validate(cls):
        return super(Menu, cls).validate() + [
            appier.not_null("day"),
            appier.gt("day", 0),

            appier.not_null("dishes"),
            appier.not_empty("dishes")
        ]

    @classmethod
    def list_names(cls):
        return ["id", "day"]

    @property
    def day_d(self):
        return datetime.datetime.fromtimestamp(self.day)
