# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('manager_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=55)),
        ))
        db.send_create_signal('manager', ['Category'])

        # Adding model 'Item'
        db.create_table('manager_item', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_last_updated', self.gf('django.db.models.fields.DateTimeField')(blank=True, auto_now=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['manager.Category'], related_name='category')),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('purchased_for', self.gf('django.db.models.fields.DecimalField')(decimal_places=2, max_digits=10)),
            ('item_weight', self.gf('django.db.models.fields.DecimalField')(blank=True, null=True, decimal_places=2, max_digits=10)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(blank=True, null=True, max_length=100)),
            ('listing_url', self.gf('django.db.models.fields.URLField')(blank=True, max_length=200)),
            ('starting_bid', self.gf('django.db.models.fields.DecimalField')(blank=True, null=True, decimal_places=2, max_digits=10)),
            ('buy_it_now', self.gf('django.db.models.fields.DecimalField')(blank=True, null=True, decimal_places=2, max_digits=10)),
            ('shipping_estimate', self.gf('django.db.models.fields.DecimalField')(blank=True, null=True, decimal_places=2, max_digits=10)),
            ('sold_for', self.gf('django.db.models.fields.DecimalField')(blank=True, null=True, decimal_places=2, max_digits=10)),
            ('shipping_actual', self.gf('django.db.models.fields.DecimalField')(blank=True, null=True, decimal_places=2, max_digits=10)),
            ('total_weight', self.gf('django.db.models.fields.DecimalField')(blank=True, null=True, decimal_places=2, max_digits=10)),
        ))
        db.send_create_signal('manager', ['Item'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('manager_category')

        # Deleting model 'Item'
        db.delete_table('manager_item')


    models = {
        'manager.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '55'})
        },
        'manager.item': {
            'Meta': {'object_name': 'Item'},
            'buy_it_now': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'decimal_places': '2', 'max_digits': '10'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['manager.Category']", 'related_name': "'category'"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'date_last_updated': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'item_weight': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'decimal_places': '2', 'max_digits': '10'}),
            'listing_url': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'purchased_for': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'max_digits': '10'}),
            'shipping_actual': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'decimal_places': '2', 'max_digits': '10'}),
            'shipping_estimate': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'decimal_places': '2', 'max_digits': '10'}),
            'sold_for': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'decimal_places': '2', 'max_digits': '10'}),
            'starting_bid': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'decimal_places': '2', 'max_digits': '10'}),
            'total_weight': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'null': 'True', 'decimal_places': '2', 'max_digits': '10'})
        }
    }

    complete_apps = ['manager']