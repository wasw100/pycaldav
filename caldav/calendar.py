# -*- coding: utf-8 -*-
"""
google
"""

# from datetime import datetime
import datetime
from lxml import etree

from caldav.elements import dav, cdav, nsdav
from caldav.lib import error, vcal, url
from caldav.lib.url import URL
from caldav.objects import Calendar, DAVObject, Event


class CalendarClient(DAVObject):

    def __init__(self, client, url):
        ## backwards compatibility.
        if url is not None:
            print 'url1-%s' % url
            url = client.url.join(URL.objectify(url))
            print 'url2-%s' % url
        else:
            raise TypeError("url can't be NoneType")

        super(CalendarClient, self).__init__(client=client, url=url)

    def get_ctag_token(self):
        """
        获取ctag, sync-token
        :return: (ctag, token)
        """
        props = [nsdav.GetCTag(), dav.SyncToken()]
        rc = self.get_properties(props)
        return rc['{http://calendarserver.org/ns/}getctag'], rc['{DAV:}sync-token']

    def events_from_last_month(self):
        now = datetime.datetime.today()
        start = datetime.datetime(now.year, now.month, now.day) - datetime.timedelta(days=31)
        return self.events(start)


    def events(self, start, end=None):
        matches = []

        # build the request
        prop = dav.Prop() + [dav.GetETag(), dav.GetContentType(), ]

        range = cdav.TimeRange(start, end)
        vevent = cdav.CompFilter("VEVENT") + range
        vcalendar = cdav.CompFilter("VCALENDAR") + vevent
        filter = cdav.Filter() + vcalendar

        root = cdav.CalendarQuery() + [prop, filter]

        q = etree.tostring(root.xmlelement(), encoding="utf-8",
                           xml_declaration=True)
        response = self.client.report(self.url, q, 1)
        for r in response.tree.findall(".//" + dav.Response.tag):
            status = r.find(".//" + dav.Status.tag)
            if status.text.endswith("200 OK"):
                # href = URL.objectify(r.find(dav.Href.tag).text)
                # href = self.url.join(href)
                href = r.find(dav.Href.tag).text
                etag = r.find(".//" + dav.GetETag.tag).text
                e = (href, etag)
                print e
                # e = Event(self.client, url=href, data=data, parent=self)
                matches.append(e)
            else:
                raise error.ReportError(response.raw)

        return matches

    def events_detail(self, hrefs):
        """
        获取Event的详情
        """
        props = [dav.GetETag(),
                 cdav.CalendarData(),
                 cdav.ScheduleTag(),
                 nsdav.CreatedBy(),
                 nsdav.UpdatedBy(),
                 ]
        prop = dav.Prop() + props

        multiget = [prop]
        for href in hrefs:
            href_tag = dav.Href(value=href)
            multiget.append(href_tag)

        root = cdav.CalendarMultiget() + multiget

        q = etree.tostring(root.xmlelement(), encoding="utf-8",
                           xml_declaration=True)
        response = self.client.report(self.url, q, 1)


def _get_last_month_day():
    """
    获取上个月的今天
    :return:
    """
    now = datetime.datetime.today()
    last_month_last_day = datetime.datetime(now.year, now.month, now.day) - datetime.timedelta(days=31)
    return last_month_last_day


if __name__ == '__main__':
    print _get_last_month_day()

