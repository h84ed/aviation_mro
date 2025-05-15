# Copyright (c) 2025, Ed Harrison and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Item(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from erpnext.stock.doctype.item_barcode.item_barcode import ItemBarcode
		from erpnext.stock.doctype.item_customer_detail.item_customer_detail import ItemCustomerDetail
		from erpnext.stock.doctype.item_default.item_default import ItemDefault
		from erpnext.stock.doctype.item_reorder.item_reorder import ItemReorder
		from erpnext.stock.doctype.item_supplier.item_supplier import ItemSupplier
		from erpnext.stock.doctype.item_tax.item_tax import ItemTax
		from erpnext.stock.doctype.item_variant_attribute.item_variant_attribute import ItemVariantAttribute
		from erpnext.stock.doctype.uom_conversion_detail.uom_conversion_detail import UOMConversionDetail
		from frappe.model.document import Document
		from frappe.types import DF

		allow_alternative_item: DF.Check
		allow_negative_stock: DF.Check
		asset_category: DF.Link | None
		asset_naming_series: DF.Literal[None]
		attributes: DF.Table[ItemVariantAttribute]
		auto_create_assets: DF.Check
		barcodes: DF.Table[ItemBarcode]
		batch_number_series: DF.Data | None
		brand: DF.Link | None
		condition_code: DF.Literal["NE (New)", "OH (Overhauled)", "SV (Serviceable)", "AR (As-Removed)", "RP (Repairable)", "SCR (Scrap)"]
		country_of_origin: DF.Link | None
		create_new_batch: DF.Check
		customer: DF.Link | None
		customer_code: DF.SmallText | None
		customer_items: DF.Table[ItemCustomerDetail]
		customs_tariff_number: DF.Link | None
		default_bom: DF.Link | None
		default_item_manufacturer: DF.Link | None
		default_manufacturer_part_no: DF.Data | None
		default_material_request_type: DF.Literal["Purchase", "Material-Transfer", "Material-Issue", "Manufacture", "Customer-Provided"]
		delivered_by_supplier: DF.Check
		description: DF.SmallText | None
		disabled: DF.Check
		enable_deferred_expense: DF.Check
		enable_deferred_revenue: DF.Check
		end_of_life: DF.Date | None
		engine_type: DF.Literal["", "PW100-Series", "PT6-Series", "Other-Turbine-Engine"]
		exchange_value: DF.Float
		grant_commission: DF.Check
		has_batch_no: DF.Check
		has_exchange_core: DF.Check
		has_expiry_date: DF.Check
		has_serial_no: DF.Check
		has_variants: DF.Check
		image: DF.AttachImage | None
		include_item_in_manufacturing: DF.Check
		inspection_required_before_delivery: DF.Check
		inspection_required_before_purchase: DF.Check
		is_customer_provided_item: DF.Check
		is_fixed_asset: DF.Check
		is_grouped_asset: DF.Check
		is_purchase_item: DF.Check
		is_sales_item: DF.Check
		is_stock_item: DF.Check
		is_sub_contracted_item: DF.Check
		item_ac: DF.Link | None
		item_code: DF.Data
		item_defaults: DF.Table[ItemDefault]
		item_group: DF.Link | None
		item_llp: DF.Table[Document]
		item_name: DF.Data | None
		last_purchase_rate: DF.Float
		lead_time_days: DF.Int
		linked_engine: DF.Link | None
		max_discount: DF.Float
		min_order_qty: DF.Float
		naming_series: DF.Literal[".{part_number}.-TT.#####"]
		no_of_months: DF.Int
		no_of_months_exp: DF.Int
		opening_stock: DF.Float
		over_billing_allowance: DF.Float
		over_delivery_receipt_allowance: DF.Float
		part_number: DF.Data
		part_type: DF.Literal["", "Component", "Engine Parts", "Airframe Parts", "Avionics", "Other"]
		purchase_uom: DF.Link | None
		quality_inspection_template: DF.Link | None
		release_type: DF.Literal["FAA 8130", "EASA Form 1", "CAAT Form 1", "CAAN Form 1", "DGCA", "Other", "None"]
		reorder_levels: DF.Table[ItemReorder]
		retain_sample: DF.Check
		safety_stock: DF.Float
		sales_uom: DF.Link | None
		sample_quantity: DF.Int
		serial_no_series: DF.Data | None
		shelf_life_in_days: DF.Int
		standard_rate: DF.Currency
		stock_uom: DF.Link
		supplier_items: DF.Table[ItemSupplier]
		taxes: DF.Table[ItemTax]
		total_projected_qty: DF.Float
		tracked_component: DF.Check
		tt_batch_number: DF.Data | None
		tt_serial_number: DF.Data | None
		uoms: DF.Table[UOMConversionDetail]
		valuation_method: DF.Literal["", "FIFO", "Moving Average", "LIFO"]
		valuation_rate: DF.Currency
		variant_based_on: DF.Literal["Item Attribute", "Manufacturer"]
		variant_of: DF.Link | None
		warranty_period: DF.Data | None
		weight_per_unit: DF.Float
		weight_uom: DF.Link | None
	# end: auto-generated types
	pass
