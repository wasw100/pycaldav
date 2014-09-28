#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pycaldav.lib.namespace import ns
from base import BaseElement, NamedBaseElement, ValuedBaseElement


## Operations
class GetCTag(BaseElement):
    tag = ns("cs", "getctag")


class CreatedBy(BaseElement):
    tag = ns("cs", "created-by")


class UpdatedBy(BaseElement):
    tag = ns("cs", "updated-by")


class AllowedSharingModes(BaseElement):
    tag = ns("cs", "allowed-sharing-modes")


class PrePublishUrl(BaseElement):
    tag = ns("cs", "pre-publish-url")


class PublishUrl(BaseElement):
    tag = ns("cs", "publish-url")


class PushTransports(BaseElement):
    tag = ns("cs", "push-transports")


class Pushkey(BaseElement):
    tag = ns("cs", "pushkey")


class Source(BaseElement):
    tag = ns("cs", "source")


class SubscribedStripAlarms(BaseElement):
    tag = ns("cs", "subscribed-strip-alarms")


class SubscribedStripAttachments(BaseElement):
    tag = ns("cs", "subscribed-strip-attachments")


class SubscribedStripTodos(BaseElement):
    tag = ns("cs", "subscribed-strip-todos")

