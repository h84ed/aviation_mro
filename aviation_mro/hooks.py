from . import __version__ as app_version

app_name = "aviation_mro"
app_title = "Aviation MRO"
app_publisher = "Ed Harrison"
app_description = "Aviation maintenance and inventory for parts"
app_email = "ed@turbinetech.aero"
app_icon = "octicon octicon-tools"
app_color = "blue"
app_license = "MIT"

app_include_css = "/assets/aviation_mro/css/aviation_mro.css"

doctype_js = {
    "BOM": "public/js/bom_custom.js",
    "Stock Entry": "public/js/stock_entry.js",
}

doc_events = {
    "Asset": {
        "validate": "aviation_mro.hooks.asset_hooks.auto_set_next_due"
    }
}


