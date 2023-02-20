# Copyright 2021 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Access all OUs' Purchase Requests",
    "version": "14.0.1.0.0",
    "author": "Ecosoft,Odoo Community Association (OCA)",
    "category": "Purchase Management",
    "license": "AGPL-3",
    "website": "https://github.com/OCA/operating-unit",
    "depends": ["purchase_request_operating_unit"],
    "data": [
        "security/purchase_security.xml",
    ],
    "installable": True,
    "maintainers": ["kittiu"],
}
