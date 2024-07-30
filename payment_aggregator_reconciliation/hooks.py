app_name = "payment_aggregator_reconciliation"
app_title = "Payment Aggregator Reconciliation"
app_publisher = "Finbyz Tech Pvt Ltd"
app_description = "payment aggregator reconciliation"
app_email = "info@finbyz.tech"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/payment_aggregator_reconciliation/css/payment_aggregator_reconciliation.css"
# app_include_js = "/assets/payment_aggregator_reconciliation/js/payment_aggregator_reconciliation.js"

# include js, css files in header of web template
# web_include_css = "/assets/payment_aggregator_reconciliation/css/payment_aggregator_reconciliation.css"
# web_include_js = "/assets/payment_aggregator_reconciliation/js/payment_aggregator_reconciliation.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "payment_aggregator_reconciliation/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Aggregator To Bank Transfer" : "public/js/aggregator_to_bank_transfer.js"
    }
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "payment_aggregator_reconciliation/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "payment_aggregator_reconciliation.utils.jinja_methods",
# 	"filters": "payment_aggregator_reconciliation.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "payment_aggregator_reconciliation.install.before_install"
# after_install = "payment_aggregator_reconciliation.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "payment_aggregator_reconciliation.uninstall.before_uninstall"
# after_uninstall = "payment_aggregator_reconciliation.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "payment_aggregator_reconciliation.utils.before_app_install"
# after_app_install = "payment_aggregator_reconciliation.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "payment_aggregator_reconciliation.utils.before_app_uninstall"
# after_app_uninstall = "payment_aggregator_reconciliation.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "payment_aggregator_reconciliation.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	# "*": {
	# 	"on_update": "method",
	# 	"on_cancel": "method",
	# 	"on_trash": "method"
	# }
    "POS Invoice": {
        "on_submit": "payment_aggregator_reconciliation.payment_aggregator_reconciliation.doc_events.pos_invoice.on_submit",
        "on_cancel": "payment_aggregator_reconciliation.payment_aggregator_reconciliation.doc_events.pos_invoice.on_cancel"
    },
     "Aggregator To Bank Transfer": {
        "on_submit": "payment_aggregator_reconciliation.payment_aggregator_reconciliation.doc_events.aggregator_to_bank_transfer.on_submit",
        # "on_cancel": "payment_aggregator_reconciliation.payment_aggregator_reconciliation.doc_events.aggregator_to_bank_transfer.on_cancel"
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"payment_aggregator_reconciliation.tasks.all"
# 	],
# 	"daily": [
# 		"payment_aggregator_reconciliation.tasks.daily"
# 	],
# 	"hourly": [
# 		"payment_aggregator_reconciliation.tasks.hourly"
# 	],
# 	"weekly": [
# 		"payment_aggregator_reconciliation.tasks.weekly"
# 	],
# 	"monthly": [
# 		"payment_aggregator_reconciliation.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "payment_aggregator_reconciliation.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "payment_aggregator_reconciliation.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "payment_aggregator_reconciliation.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["payment_aggregator_reconciliation.utils.before_request"]
# after_request = ["payment_aggregator_reconciliation.utils.after_request"]

# Job Events
# ----------
# before_job = ["payment_aggregator_reconciliation.utils.before_job"]
# after_job = ["payment_aggregator_reconciliation.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"payment_aggregator_reconciliation.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

