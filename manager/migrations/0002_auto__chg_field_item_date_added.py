# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Item.date_added'
        db.alter_column('manager_item', 'date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    def backwards(self, orm):

        # Changing field 'Item.date_added'
        db.alter_column('manager_item', 'date_added', self.gf('django.db.models.fields.DateTimeField')())

    models = {
        'manager.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '55'})
        },
        'manager.item': {
            'Meta': {'object_name': 'Item'},
            'buy_it_now': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'max_digits': '10', 'null': 'True', 'decimal_places': '2'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['manager.Category']", 'related_name': "'category'"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_last_updated': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'item_weight': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'max_digits': '10', 'null': 'True', 'decimal_places': '2'}),
            'listing_url': ('django.db.models.fields.URLField', [], {'blank': 'True', 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'purchased_for': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'shipping_actual': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'max_digits': '10', 'null': 'True', 'decimal_places': '2'}),
            'shipping_estimate': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'max_digits': '10', 'null': 'True', 'decimal_places': '2'}),
            'sold_for': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'max_digits': '10', 'null': 'True', 'decimal_places': '2'}),
            'starting_bid': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'max_digits': '10', 'null': 'True', 'decimal_places': '2'}),
            'total_weight': ('django.db.models.fields.DecimalField', [], {'blank': 'True', 'max_digits': '10', 'null': 'True', 'decimal_places': '2'})
        }
    }

    complete_apps = ['manager']