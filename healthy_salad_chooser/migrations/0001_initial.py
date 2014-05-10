# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ingredient'
        db.create_table(u'healthy_salad_chooser_ingredient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('serving_size', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('serving_unit', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('calories', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('weight_in_oz', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('nutrient_density', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal(u'healthy_salad_chooser', ['Ingredient'])

        # Adding model 'Salad'
        db.create_table(u'healthy_salad_chooser_salad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal(u'healthy_salad_chooser', ['Salad'])

        # Adding unique constraint on 'Salad', fields ['user', 'name']
        db.create_unique(u'healthy_salad_chooser_salad', ['user_id', 'name'])

        # Adding model 'SaladIngredient'
        db.create_table(u'healthy_salad_chooser_saladingredient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ingredient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['healthy_salad_chooser.Ingredient'])),
            ('salad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['healthy_salad_chooser.Salad'])),
        ))
        db.send_create_signal(u'healthy_salad_chooser', ['SaladIngredient'])


    def backwards(self, orm):
        # Removing unique constraint on 'Salad', fields ['user', 'name']
        db.delete_unique(u'healthy_salad_chooser_salad', ['user_id', 'name'])

        # Deleting model 'Ingredient'
        db.delete_table(u'healthy_salad_chooser_ingredient')

        # Deleting model 'Salad'
        db.delete_table(u'healthy_salad_chooser_salad')

        # Deleting model 'SaladIngredient'
        db.delete_table(u'healthy_salad_chooser_saladingredient')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'healthy_salad_chooser.ingredient': {
            'Meta': {'object_name': 'Ingredient'},
            'calories': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nutrient_density': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'serving_size': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'serving_unit': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'weight_in_oz': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        u'healthy_salad_chooser.salad': {
            'Meta': {'unique_together': "(('user', 'name'),)", 'object_name': 'Salad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'healthy_salad_chooser.saladingredient': {
            'Meta': {'object_name': 'SaladIngredient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['healthy_salad_chooser.Ingredient']"}),
            'salad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['healthy_salad_chooser.Salad']"})
        }
    }

    complete_apps = ['healthy_salad_chooser']