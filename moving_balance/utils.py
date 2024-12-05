import frappe
from erpnext.accounts.utils import get_balance_on
import frappe.utils


def party_validate(doc, event):
    """ get and set party bal"""

    balance = get_balance_on(
        date=frappe.utils.today(),
        party_type='Customer',
        party= doc.customer
    )
    doc.custom_customer_balance = balance
