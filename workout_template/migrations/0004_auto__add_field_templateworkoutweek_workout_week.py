# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TemplateWorkoutWeek.workout_week'
        db.add_column(u'workout_template_templateworkoutweek', 'workout_week',
                      self.gf('django.db.models.fields.CharField')(default='1', max_length=5),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TemplateWorkoutWeek.workout_week'
        db.delete_column(u'workout_template_templateworkoutweek', 'workout_week')


    models = {
        u'exercise.exercisename': {
            'Meta': {'ordering': "['name']", 'object_name': 'ExerciseName'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'workout_template.templateworkoutweek': {
            'Meta': {'object_name': 'TemplateWorkoutWeek'},
            'group': ('django.db.models.fields.CharField', [], {'default': "'A'", 'max_length': '1'}),
            'group_order': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exercise.ExerciseName']"}),
            'percent_of_max': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'reps': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'rest_time': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'set_number': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'tempo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workout_template.WorkoutSheetTemplate']"}),
            'workout_week': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '5'})
        },
        u'workout_template.workoutsheettemplate': {
            'Meta': {'ordering': "['-start_date']", 'object_name': 'WorkoutSheetTemplate'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 12, 9, 0, 0)'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'exercise_category': ('django.db.models.fields.CharField', [], {'default': "'GEN'", 'max_length': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 12, 9, 0, 0)', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['workout_template']