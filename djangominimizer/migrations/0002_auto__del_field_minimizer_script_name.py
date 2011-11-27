# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Minimizer.script_name'
        db.delete_column('djangominimizer_minimizer', 'script_name')


    def backwards(self, orm):
        
        # Adding field 'Minimizer.script_name'
        db.add_column('djangominimizer_minimizer', 'script_name', self.gf('django.db.models.fields.CharField')(default='', max_length=128, blank=True), keep_default=False)


    models = {
        'djangominimizer.minimizer': {
            'Meta': {'ordering': "('-created_at',)", 'object_name': 'Minimizer'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['djangominimizer']
