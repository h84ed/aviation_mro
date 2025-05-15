import frappe
from frappe.model.document import Document
from frappe.utils import add_days

def auto_set_next_due(doc, method):
    if doc.is_calibrated_tool and doc.last_calibrated_date:
        # Assume 365-day calibration cycle — adjust as needed
        doc.next_calibration_due = add_days(doc.last_calibrated_date, 365)
