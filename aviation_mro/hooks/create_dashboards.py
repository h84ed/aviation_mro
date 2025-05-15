import frappe

def run():
    def create_chart(name, chart_type, document_type, filters, timespan="Last 30 days", aggregate_function="count", group_by=None):
        if not frappe.db.exists("Dashboard Chart", name):
            chart = frappe.get_doc({
                "doctype": "Dashboard Chart",
                "chart_name": name,
                "chart_type": chart_type,
                "document_type": document_type,
                "filters_json": filters,
                "timespan": timespan,
                "aggregate_function": aggregate_function,
                "group_by": group_by or "creation",
                "is_custom": 1
            })
            chart.insert()
            print(f"✅ Created chart: {name}")
        return name

    def create_dashboard(name, chart_names):
        if not frappe.db.exists("Dashboard", name):
            dashboard = frappe.get_doc({
                "doctype": "Dashboard",
                "module": "MRO",
                "label": name,
                "charts": [{"chart": c, "label": c} for c in chart_names]
            })
            dashboard.insert()
            print(f"✅ Created dashboard: {name}")

    # Create charts
    charts = [
        create_chart("Active Repair Jobs", "Bar", "Work Order", "{}", "Last 30 days", "count", "status"),
        create_chart("Parts Received (GRN)", "Line", "Purchase Receipt", "{}", "Last 30 days", "count", "posting_date"),
        create_chart("Field Service Visits", "Bar", "Maintenance Visit", "{}", "Last 30 days", "count", "status")
    ]

    # Create dashboard
    create_dashboard("MRO Dashboard", charts)
