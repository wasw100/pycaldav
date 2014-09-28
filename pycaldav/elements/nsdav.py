#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from caldav.lib.namespace import ns
from base import BaseElement, NamedBaseElement, ValuedBaseElement


## Operations
class GetCTag(BaseElement):
    tag = ns("NS", "getctag")


class CreatedBy(BaseElement):
    tag = ns("NS", "created-by")


class UpdatedBy(BaseElement):
    tag = ns("NS", "updated-by")

