#import re
from frappe import _
from frappe.utils import now_datetime, flt

def on_submit(self, method):
    make_aggregator_payment_entry(self, method)

def on_cancel(self, method):
    cancel_aggregator_payment_entry(self, method)

def make_aggregator_payment_entry(self, method):
        for payment in self.payments:
            parent_doc = frappe.get_single('Aggregator Reconciliation Setting')
            for row in parent_doc.aggregators:
                
                if row.aggregator_account == payment.account:
                    if payment.amount > 0:
                        doc = frappe.new_doc('Aggregator Payments')
                        doc.aggregator = payment.mode_of_payment
                        doc.aggregator_account = payment.account
                        doc.transaction_date = now_datetime()
                        doc.paid_amount = payment.amount
                        doc.branch = self.pos_profile
                        doc.charges =  row.charges
                        doc.swipe_machine_transaction_no =self.swipe_machine_transaction_no
                        doc.charge_amount = flt(doc.paid_amount * doc.charges / 100)
                        doc.submit()
                        payment.db_set('aggregator_payment_receipt_number',doc.name)
                        self.save()
                        frappe.db.commit()

def cancel_aggregator_payment_entry(self, method):
    for payment in self.payments:
        if payment.aggregator_payment_receipt_number:
            frappe.delete_doc('Aggregator Payments', payment.aggregator_payment_receipt_number)
            payment.db_set('aggregator_payment_receipt_number','')
            frappe.db.commit()  