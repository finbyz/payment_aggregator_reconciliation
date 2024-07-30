from __future__ import unicode_literals
import frappe
#import re
from frappe import _


def on_submit(self, method):
    check_amount_received_in_bank(self, method)
    make_payment_entry(self, method)

def on_cancel(self, method):
    cancel_payment_entry(self, method)

    
def make_payment_entry(self, method):
    if self.aggregator:
        if self.bank_reference:
            if self.bank_account:
                company = frappe.get_all("Company")
                doc = frappe.new_doc('Payment Entry')
                doc.payment_type = "Internal Transfer"
                doc.posting_date = frappe.utils.nowdate()

                doc.paid_from = frappe.get_value("Aggregators", self.aggregator, "aggregator_account")
                doc.paid_to = frappe.get_value("Bank Account", self.bank_account, "account")
                # doc.paid_from_account_balance = 
                # doc.paid_to_account_balance = 
                doc.paid_amount = self.total_paid_amount
                doc.received_amount = self.bank_received_amount
                doc.branch = self.branch

                # Handle child table 'deductions'
                deduction = doc.append('deductions', {})
                deduction.account = self.charges_account
                deduction.cost_center = frappe.get_value("Cost Center", {'company':company[0].name, 'cost_center_name': "Sales"}, "name")
                deduction.amount = self.total_charges

                doc.company_address = frappe.get_value("Address", {'address_title':company[0].name}, "name")
                doc.reference_no = self.name
                doc.reference_date = self.posting_date

                doc.save()
                frappe.db.commit()

            else:
                frappe.thdoc.deductions(_("Bank Account is mandatory"))
        else:
            frappe.throw(_("Bank Reference is mandatory"))
    else:
        frappe.throw(_("Aggregator is mandatory"))

def check_amount_received_in_bank(self, method):
    for row in self.aggregator_payment_list:
        doc = frappe.get_doc("Aggregator Payments", row.id)
        doc.amount_received_in_bank = 1
        doc.submit()

def cancel_payment_entry(self, method):
    payment_entry = frappe.get_doc('Payment Entry', {'reference_no': self.name})
    # frappe.throw(payment_entry.name)
    payment_entry.cancel()
    frappe.db.commit()
    # frappe.msgprint(_("Payment Entry is cancelled"))
