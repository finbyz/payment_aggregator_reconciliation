frappe.ui.form.on("Payment Entry", {
    payment_type: function(frm) {
        if (frm.doc.payment_type === "Receive" && frm.doc.cost_center == "Sales - VNRL") {
            frm.set_value('naming_series', '.custom_branch_code./REC/.fiscal.-.####');
        }
        else if (frm.doc.payment_type === "Receive" && frm.doc.cost_center == "Service - VNRL") {
            frm.set_value('naming_series', '.custom_branch_code./REC-S/.fiscal.-.####');
        }
        else if (frm.doc.payment_type === "Pay") {
            frm.set_value('naming_series', '.custom_branch_code./PAY/.fiscal.-.####');
        }
        else if (frm.doc.payment_type === "Internal Transfer") {
            frm.set_value('naming_series', '.custom_branch_code./IT/.fiscal.-.####');
        }
    },
    onload: function(frm) {
        if (frm.doc.payment_type === "Receive" && frm.doc.cost_center == "Sales - VNRL") {
            frm.set_value('naming_series', '.custom_branch_code./REC/.fiscal.-.####');
        }
        else if (frm.doc.payment_type === "Receive" && frm.doc.cost_center == "Service - VNRL") {
            frm.set_value('naming_series', '.custom_branch_code./REC-S/.fiscal.-.####');
        }
        else if (frm.doc.payment_type === "Pay") {
            frm.set_value('naming_series', '.custom_branch_code./PAY/.fiscal.-.####');
        }
        else if (frm.doc.payment_type === "Internal Transfer") {
            frm.set_value('naming_series', '.custom_branch_code./IT/.fiscal.-.####');
        }
    },
    setup: function(frm) {
        if (frm.doc.payment_type === "Receive" && frm.doc.cost_center == "Sales - VNRL") {
            frm.set_value('naming_series', '.custom_branch_code./REC/.fiscal.-.####');
        }
        else if (frm.doc.payment_type === "Receive" && frm.doc.cost_center == "Service - VNRL") {
            frm.set_value('naming_series', '.custom_branch_code./REC-S/.fiscal.-.####');
        }
        else if (frm.doc.payment_type === "Pay") {
            frm.set_value('naming_series', '.custom_branch_code./PAY/.fiscal.-.####');
        }
        else if (frm.doc.payment_type === "Internal Transfer") {
            frm.set_value('naming_series', '.custom_branch_code./IT/.fiscal.-.####');
        }
    },
    cost_center: function(frm) {    
        if (frm.doc.payment_type === "Receive" && frm.doc.cost_center == "Sales - VNRL") {
            frm.set_value('naming_series', '.custom_branch_code./REC/.fiscal.-.####');
        }
        else if (frm.doc.payment_type === "Receive" && frm.doc.cost_center == "Service - VNRL") {
            frm.set_value('naming_series', '.custom_branch_code./REC-S/.fiscal.-.####');
        }
    },

    
});
