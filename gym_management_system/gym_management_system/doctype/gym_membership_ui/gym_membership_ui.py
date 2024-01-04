# Copyright (c) 2024, Nestorbird_Trainee_Team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class GymMembershipUI(Document):
	pass
# your_custom_module/your_custom_script.py
import frappe

@frappe.whitelist()
def get_username_from_email(email_address):
    username = frappe.get_value("User", {"email": email_address}, "full_name")
    return username

@frappe.whitelist()
def snow(abc, xyz):
    # bb = str(xyz)
    doc = frappe.get_doc('Locker Data', abc)
    doc.locker_owner = xyz
    doc.save()
    if doc.save():
        return 1
    else:
        return 0


