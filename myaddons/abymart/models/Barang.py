from odoo import api, fields, models


class Barang(models.Model):
    _name = 'abymart.barang'
    _description = 'New Description'

    name = fields.Char(string='Nama Barang')
    Harga_Beli = fields.Integer(string='Harga Modal', required=True)
    Harga_Jual = fields.Integer(string='Harga Jual', required=True)
    kelompokbarang_id = fields.Many2one(comodel_name='abymart.kelompokbarang',
                                        string='Kelompok Barang',
                                        ondelete='cascade')
    supplier_id = fields.Many2many(comodel_name='abymart.supplier', string='Supplier')