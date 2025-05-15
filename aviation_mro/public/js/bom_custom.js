frappe.ui.form.on('BOM', {
    refresh: function(frm) {
        frm.set_df_property('title', 'label', 'Parts Kit');
        frm.set_df_property('bom_type', 'label', 'Kit Type');
        frm.set_df_property('item', 'label', 'Kit Assembly Item');
    }
});