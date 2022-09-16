from odoo import api, fields, models


class kelompokbarang(models.Model):
    _name = 'abymart.kelompokbarang'
    _description = 'New Description'

    name = fields.Selection([
        ('motor', 'Motor'),
        ('mobil', 'Mobil'),
        ('sepeda', 'Sepeda')
    ], string='Nama Kelompok')

    @api.onchange('name')
    def _onchange_kode_kelompok(self):
        if self.name == 'motor':
            self.kode_kelompok = 'MOT1'
        elif self.name == 'mobil':
            self.kode_kelompok = 'MOB2'
        elif self.name == 'sepeda':
            self.kode_kelompok = 'SEP1'
            
    kode_kelompok = fields.Char(string='Kode Kelompok')        
    kode_Gudang = fields.Char(string='Kode Gudang')
    barang_ids = fields.One2many(comodel_name='abymart.barang',
                                inverse_name='kelompokbarang_id',
                                string='Daftar Barang')

    jml_item = fields.Char(compute='_compute_jml_item', string='Jml Item')

    @api.depends('barang_ids')
    def _compute_jml_item(self):
        for record in self:
            a = self.env['abymart.barang'].search([('kelompokbarang_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.jml_item = b
            record.daftar = a
    
    daftar = fields.Char(string='Daftar isi')