#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pycaldav.lib.namespace import ns
from base import BaseElement, NamedBaseElement, ValuedBaseElement


## Operations
class CalendarQuery(BaseElement):
    tag = ns("caldav", "calendar-query")

class Mkcalendar(BaseElement):
    tag = ns("D", "mkcalendar")

## Filters
class Filter(BaseElement):
    tag = ns("caldav", "filter")


class CompFilter(NamedBaseElement):
    tag = ns("caldav", "comp-filter")


class PropFilter(NamedBaseElement):
    tag = ns("caldav", "prop-filter")


class ParamFilter(NamedBaseElement):
    tag = ns("caldav", "param-filter")


## Conditions
class TextMatch(ValuedBaseElement):
    tag = ns("caldav", "text-match")

    def __init__(self, value, collation="i;octet", negate=False):
        super(TextMatch, self).__init__(value=value)
        self.attributes['collation'] = collation
        self.attributes['negate'] = "no"
        if negate:
            self.attributes['negate'] = "yes"


class TimeRange(BaseElement):
    tag = ns("caldav", "time-range")

    def __init__(self, start=None, end=None):
        super(TimeRange, self).__init__()
        if start is not None:
            self.attributes['start'] = \
                    start.strftime("%Y%m%dT%H%M%SZ")
        if end is not None:
            self.attributes['end'] = end.strftime("%Y%m%dT%H%M%SZ")


class NotDefined(BaseElement):
    tag = ns("caldav", "is-not-defined")


## Components / Data
class CalendarData(BaseElement):
    tag = ns("caldav", "calendar-data")


class Expand(BaseElement):
    tag = ns("caldav", "expand")

    def __init__(self, start, end=None):
        super(Expand, self).__init__()
        self.attributes['start'] = start.strftime("%Y%m%dT%H%M%SZ")
        if end is not None:
            self.attributes['end'] = end.strftime("%Y%m%dT%H%M%SZ")


class Comp(NamedBaseElement):
    tag = ns("caldav", "comp")


class CalendarCollection(BaseElement):
    tag = ns("caldav", "calendar-collection")


## Properties

class CalendarHomeSet(BaseElement):
    tag = ns("caldav", "calendar-home-set")

# calendar resource type, see rfc4791, sec. 4.2
class Calendar(BaseElement):
    tag = ns("caldav", "calendar")


class CalendarDescription(ValuedBaseElement):
    tag = ns("caldav", "calendar-description")


class CalendarTimeZone(ValuedBaseElement):
    tag = ns("caldav", "calendar-timezone")


class SupportedCalendarComponentSet(ValuedBaseElement):
    tag = ns("caldav", "supported-calendar-component-set")


class SupportedCalendarData(ValuedBaseElement):
    tag = ns("caldav", "supported-calendar-data")


class MaxResourceSize(ValuedBaseElement):
    tag = ns("caldav", "max-resource-size")


class MinDateTime(ValuedBaseElement):
    tag = ns("caldav", "min-date-time")


class MaxDateTime(ValuedBaseElement):
    tag = ns("caldav", "max-date-time")


class MaxInstances(ValuedBaseElement):
    tag = ns("caldav", "max-instances")


class MaxAttendeesPerInstance(ValuedBaseElement):
    tag = ns("caldav", "max-attendees-per-instance")


#add at 2014-09
class CalendarMultiget(BaseElement):
    tag = ns("caldav", "calendar-multiget")


class ScheduleTag(BaseElement):
    tag = ns("caldav", "schedule-tag")


class CalendarFreeBusySet(BaseElement):
    tag = ns("caldav", "calendar-free-busy-set")


class DefaultAlarmVeventDate(BaseElement):
    tag = ns("caldav", "default-alarm-vevent-date")


class DefaultAlarmVeventDatetime(BaseElement):
    tag = ns("caldav", "default-alarm-vevent-datetime")


class ScheduleCalendarTransp(BaseElement):
    tag = ns("caldav", "schedule-calendar-transp")


class ScheduleDefaultCalendarUrl(BaseElement):
    tag = ns("caldav", "schedule-default-calendar-URL")


class SupportedCalendarComponentSets(BaseElement):
    tag = ns("caldav", "supported-calendar-component-sets")