from __future__ import unicode_literals
import frappe
#import re
from frappe import _
from frappe.utils import now_datetime, flt
from frappe.model.mapper import get_mapped_doc


def validate(self, method):
    make_charges_calculations(self, method)

def on_update_after_submit(self, method):
    after_submit_make_charges_calculations(self, method)

def make_charges_calculations(self, method):
    self.charge_amount = flt(self.paid_amount * self.charges / 100)
    frappe.db.commit()

def after_submit_make_charges_calculations(self, method):
    self.charge_amount = flt(self.paid_amount * self.charges / 100)
    frappe.db.set_value("Aggregator Payments", self.name , "charge_amount", self.charge_amount)
    frappe.db.commit()

