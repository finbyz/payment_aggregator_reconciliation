frappe.ui.form.on('Aggregator To Bank Transfer', {
    get_payments: function(frm, cdt, cdn) {
        console.log("Get Payments Button Clicked");
        frappe.call({
            method: 'frappe.client.get_list',
            args: {
                doctype: 'Aggregator Payments',
                fields: ['name','aggregator', 'aggregator_account', 'transaction_date', 'branch', 'paid_amount', 'swipe_machine_transaction_no', 'charges', 'charge_amount'],
                filters: {
                    'amount_received_in_bank': 0,
                    'transaction_date':  frm.doc.posting_date || '',
                    'branch': frm.doc.branch || '',
                    'aggregator': frm.doc.aggregator || '',
                },
                limit_page_length: 200,
            },
            callback: function(r) {
                frm.clear_table('aggregator_payment_list');
                if (r.message && Array.isArray(r.message)) {
                    r.message.forEach(doc => {
                        let new_row = frappe.model.add_child(frm.doc, "Aggregator Payment List", "aggregator_payment_list");
                        frappe.model.set_value(new_row.doctype, new_row.name, {
                            id: doc.name,
                            aggregator: doc.aggregator,   
                            aggregator_account: doc.aggregator_account,
                            transaction_date: doc.transaction_date,
                            branch: doc.branch,
                            paid_amount: doc.paid_amount,
                            swipe_machine_transaction_no: doc.swipe_machine_transaction_no,
                            charges: doc.charges,
                            charge_amount: doc.charge_amount
                        });
                        
                    });
                    frm.refresh_field('aggregator_payment_list');  
                    frm.trigger('total_calculation');
                } 
            }
        });
    },
    total_calculation(frm) {
        setTimeout(() => {
            console.log("Total Calculation");
            let total = 0;
            let total_charges = 0;
            for (let row of frm.doc.aggregator_payment_list || []) {
                total += flt(row.paid_amount);
                total_charges += flt(row.charge_amount);
            }
            console.log("Total: ", total);
            frm.set_value('total_paid_amount', total);
            frm.set_value('total_charges', total_charges);
            frm.set_value('bank_received_amount', flt(total - total_charges));
            frm.set_value('difference', flt(total - frm.doc.bank_received_amount));
        }, 100);
    },
    refresh: function(frm) {
        frm.fields_dict['aggregator_payment_list'].grid.wrapper.on('click', '.grid-remove-rows', function() {
            frm.trigger('total_calculation');
        });
        frm.fields_dict['aggregator_payment_list'].grid.wrapper.on('click', '.grid-add-row', function() {
            frm.trigger('total_calculation');
        });
    },
    validate: function(frm) {
        frm.trigger('calculation_without_bank_received_amount');
    },

    calculation_without_bank_received_amount (frm){
        let total = 0;
            let total_charges = 0;
            for (let row of frm.doc.aggregator_payment_list || []) {
                total += flt(row.paid_amount);
                total_charges += flt(row.charge_amount);
            }
            console.log("Total: ", total);
            frm.set_value('total_paid_amount', total);
            frm.set_value('total_charges', total_charges);
            frm.set_value('difference', flt(total - frm.doc.bank_received_amount));
    }
});

