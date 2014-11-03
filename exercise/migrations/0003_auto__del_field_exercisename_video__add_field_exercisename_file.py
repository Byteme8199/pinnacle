# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ExerciseName.video'
        db.delete_column(u'exercise_exercisename', 'video')

        # Adding field 'ExerciseName.file'
        db.add_column(u'exercise_exercisename', 'file',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'ExerciseName.video'
        db.add_column(u'exercise_exercisename', 'video',
                      self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'ExerciseName.file'
        db.delete_column(u'exercise_exercisename', 'file')


    models = {
        u'exercise.exercisename': {
            'Meta': {'ordering': "['name']", 'object_name': 'ExerciseName'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['exercise']