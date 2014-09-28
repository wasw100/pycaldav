#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pycaldav.lib.namespace import ns
from base import BaseElement, NamedBaseElement, ValuedBaseElement


## Operations
class AutoProvisioned(BaseElement):
    tag = ns("ical", "autoprovisioned")


class CalendarColor(BaseElement):
    tag = ns("ical", "calendar-color")


class CalendarOrder(BaseElement):
    tag = ns("ical", "calendar-order")


class LanguageCode(BaseElement):
    tag = ns("ical", "language-code")


class LocationCode(BaseElement):
    tag = ns("ical", "location-code")


class RefreshRate(BaseElement):
    tag = ns("ical", "refreshrate")
