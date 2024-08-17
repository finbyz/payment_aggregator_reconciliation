from __future__ import unicode_literals
import frappe
#import re
from frappe import _
from frappe.utils import now_datetime, flt
from frappe.model.mapper import get_mapped_doc

def on_submit(self, method):
	make_aggregator_payment_entry(self, method)
	create_sales_invoice(self, method)
	consolidate_pos_invoice(self, method)
	


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
						# self.save()
						frappe.db.commit()

def cancel_aggregator_payment_entry(self, method):
	for payment in self.payments:
		if payment.aggregator_payment_receipt_number:
			frappe.delete_doc('Aggregator Payments', payment.aggregator_payment_receipt_number)
			payment.db_set('aggregator_payment_receipt_number','')
			frappe.db.commit()  

def create_sales_invoice(doc, method):
	pos_invoice = doc

	sales_invoice = get_mapped_doc(
		"POS Invoice",
		pos_invoice.name,
		{
			"POS Invoice": {
				"doctype": "Sales Invoice",
				"field_map": {"pos_profile": "branch"},
			},
			"POS Invoice Item": {
				"doctype": "Sales Invoice Item",
			},
			"POS Invoice Tax": {
				"doctype": "Sales Taxes and Charges",
			}
		}
	)
	# Custom logic or additional fields
	
	def set_missing_values(source, target):
		target.flags.ignore_permissions = True

	set_missing_values(pos_invoice, sales_invoice)

	for item in sales_invoice.items:
		pos_item = next((i for i in pos_invoice.items if i.item_code == item.item_code), None)

		if pos_item and pos_item.serial_and_batch_bundle:
			bundle_doc = frappe.get_doc("Serial and Batch Bundle", pos_item.serial_and_batch_bundle)
			for entry in bundle_doc.entries:
				serial_no = entry.serial_no
				if serial_no:
					serial_doc = frappe.get_doc("Serial No", serial_no)
					serial_doc.discount = flt(item.rate - item.net_rate)
					serial_doc.discount_transaction_ref_no = pos_invoice.discount_transaction_no
					serial_doc.save()

	sales_invoice.insert()
	sales_invoice.submit()
	pos_invoice.db_set("consolidated_invoice", sales_invoice.name)	

def consolidate_pos_invoice(self ,method):
	self.db_set("status", "Consolidated")
	frappe.db.commit()  		
					

