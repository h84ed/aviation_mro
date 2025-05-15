import frappe
from frappe.model.document import Document
from frappe.utils import date_diff, nowdate, flt, cint

class Aircraft(Document):
    def validate(self):
        self.calculate_remaining_to_inspection()
        # Call the engine update if aircraft hours/cycles change.
        # This assumes engines get their hours/cycles primarily from the aircraft.
    # elf.update_engine_hours_from_aircraft()
        # A more robust way to update engine references on aircraft save:
    #   self.sync_engine_installation_status()


    def calculate_remaining_to_inspection(self):
        """
        Calculates remaining time/cycles/days until the aircraft's next major inspection.
        This version assumes specific fields for the *next* inspection are manually set
        or set by another process (e.g., a maintenance program module).

        Required Custom Fields on Aircraft DocType (for *next* inspection details):
            - next_inspection_type (Data)
            - next_inspection_due_hours (Float)
            - next_inspection_due_cycles (Int)
            - next_inspection_due_date (Date)

        Required Custom Fields on Aircraft DocType (to store calculated remaining values - Read Only):
            - remaining_hours_to_inspection (Float)
            - remaining_cycles_to_inspection (Int)
            - remaining_days_to_inspection (Int)
        """
        current_fh = flt(self.current_flight_hours)
        current_fc = cint(self.current_flight_cycles) # Use cint for cycles
        today = nowdate()

        # --- Hours Based ---
        if self.next_inspection_due_hours is not None and flt(self.next_inspection_due_hours) > 0:
            self.remaining_hours_to_inspection = flt(self.next_inspection_due_hours) - current_fh
        else:
            self.remaining_hours_to_inspection = None

        # --- Cycles Based ---
        if self.next_inspection_due_cycles is not None and cint(self.next_inspection_due_cycles) > 0:
            self.remaining_cycles_to_inspection = cint(self.next_inspection_due_cycles) - current_fc
        else:
            self.remaining_cycles_to_inspection = None

        # --- Date Based ---
        if self.next_inspection_due_date:
            try:
                self.remaining_days_to_inspection = date_diff(self.next_inspection_due_date, today)
            except Exception: # Handle invalid date
                self.remaining_days_to_inspection = None
        else:
            self.remaining_days_to_inspection = None



        
        # Commit changes made to other documents if any
        frappe.db.commit()

# Note: The `update_engine_hours_from_aircraft` and `sync_engine_installation_status`
# functions involve saving other documents (Engine). This can have performance implications
# and might lead to nested save triggers if not handled carefully.
# Consider if some of these operations are better suited for explicit user actions
# (e.g., an "Install Engine" or "Update Fleet Hours" button/process).
