#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from pycaldav.lib.namespace import ns
from base import BaseElement, ValuedBaseElement


## Operations
class Propfind(BaseElement):
    tag = ns("D", "propfind")


class PropertyUpdate(BaseElement):
    tag = ns("D", "propertyupdate")


class Mkcol(BaseElement):
    tag = ns("D", "mkcol")

## Filters

## Conditions

## Components / Data


class Prop(BaseElement):
    tag = ns("D", "prop")


class Collection(BaseElement):
    tag = ns("D", "collection")


class Set(BaseElement):
    tag = ns("D", "set")


## Properties
class ResourceType(BaseElement):
    tag = ns("D", "resourcetype")


class DisplayName(ValuedBaseElement):
    tag = ns("D", "displayname")


class Href(BaseElement):
    tag = ns("D", "href")


class Response(BaseElement):
    tag = ns("D", "response")


class Status(BaseElement):
    tag = ns("D", "status")

class CurrentUserPrincipal(BaseElement):
    tag = ns("D", "current-user-principal")


#add 2014-9
class SyncToken(BaseElement):
    tag = ns("D", "sync-token")


class GetETag(BaseElement):
    tag = ns("D", 'getetag')


class GetContentType(BaseElement):
    tag = ns("D", 'getcontenttype')


class AddMember(BaseElement):
    tag = ns("D", 'add-member')


class CurrentUserPrivilegeSet(BaseElement):
    tag = ns("D", "current-user-privilege-set")


class Owner(BaseElement):
    tag = ns("D", "owner")

class QuotaAvailableBytes(BaseElement):
    tag = ns("D", "quota-available-bytes")


class QuotaUsedBytes(BaseElement):
    tag = ns("D", "quota-used-bytes")


class ResourceId(BaseElement):
    tag = ns("D", "resource-id")


class SupportedReportSet(BaseElement):
    tag = ns("D", "supported-report-set")

