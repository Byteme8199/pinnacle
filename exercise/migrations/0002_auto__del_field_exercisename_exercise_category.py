# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ExerciseName.exercise_category'
        db.delete_column(u'exercise_exercisename', 'exercise_category')


    def backwards(self, orm):
        # Adding field 'ExerciseName.exercise_category'
        db.add_column(u'exercise_exercisename', 'exercise_category',
                      self.gf('django.db.models.fields.CharField')(default='GEN', max_length=4),
                      keep_default=False)


    models = {
        u'exercise.exercisename': {
            'Meta': {'ordering': "['name']", 'object_name': 'ExerciseName'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['exercise']