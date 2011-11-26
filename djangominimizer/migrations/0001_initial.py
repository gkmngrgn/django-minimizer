# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Minimizer'
        db.create_table('djangominimizer_minimizer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('script_name', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('djangominimizer', ['Minimizer'])


    def backwards(self, orm):
        
        # Deleting model 'Minimizer'
        db.delete_table('djangominimizer_minimizer')


    models = {
        'djangominimizer.minimizer': {
            'Meta': {'ordering': "('-created_at',)", 'object_name': 'Minimizer'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'script_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'})
        }
    }

    complete_apps = ['djangominimizer']
