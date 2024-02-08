# Part of Odoo. See LICENSE file for full copyright and licensing details.

import datetime
import logging
import os
import re
import tempfile

from lxml import html

import odoo
import odoo.modules.registry
from odoo import http
from odoo.http import content_disposition, dispatch_rpc, request, Response
from odoo.service import db
from odoo.tools.misc import file_open, str2bool
from odoo.tools.translate import _

from odoo.addons.base.models.ir_qweb import render as qweb_render

from odoo.addons.web.controllers.database import Database
_logger = logging.getLogger(__name__)


DBNAME_PATTERN = '^[a-zA-Z0-9][a-zA-Z0-9_.-]+$'


class CustomDatabase(Database):

    @http.route('/web/database/selector', type='http', auth="none")
    def selector(self, **kw):
        return request.redirect('/web/login')

    @http.route('/web/database/manager', type='http', auth="none")
    def manager(self, **kw):

        return request.redirect('/web/login')
