#!/usr/bin/env python
# -*- encoding: utf-8 -*-

## nsmap2 is ref https://bitbucket.org/cyrilrbt/pycaldav/issue/29/centos59-minifix
## This looks wrong - should think more about it at a later stage. 
## -- Tobias Brox, 2014-02-16

nsmap = {
    "D": "DAV:",
    "caldav": "urn:ietf:params:xml:ns:caldav",
    "cs": "http://calendarserver.org/ns/",
    "ical": "http://apple.com/ns/ical/",
}

nsmap2 = {
    "D": "DAV:",
    "caldav": "urn:ietf:params:xml:ns:caldav",
    "cs": "http://calendarserver.org/ns/",
    "ical": "http://apple.com/ns/ical/",
}


def ns(prefix, tag=None):
    name = "{%s}" % nsmap2[prefix]
    if tag is not None:
        name = "%s%s" % (name, tag)
    return name
