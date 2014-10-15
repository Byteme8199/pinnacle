# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ExerciseName'
        db.create_table(u'workout_exercisename', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('video', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('exercise_category', self.gf('django.db.models.fields.CharField')(default='GEN', max_length=4)),
        ))
        db.send_create_signal(u'workout', ['ExerciseName'])

        # Adding model 'WorkoutSet'
        db.create_table(u'workout_workoutset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('set_number', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=3, null=True, blank=True)),
            ('result', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('percent_of_max', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('tempo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('rest_time', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('reps', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=4, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=4, null=True, blank=True)),
            ('workout_week', self.gf('django.db.models.fields.CharField')(default='1', max_length=5)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Exercise'])),
        ))
        db.send_create_signal(u'workout', ['WorkoutSet'])

        # Adding model 'Exercise'
        db.create_table(u'workout_exercise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.ExerciseName'])),
        ))
        db.send_create_signal(u'workout', ['Exercise'])

        # Adding M2M table for field workout on 'Exercise'
        db.create_table(u'workout_exercise_workout', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('exercise', models.ForeignKey(orm[u'workout.exercise'], null=False)),
            ('workout', models.ForeignKey(orm[u'workout.workout'], null=False))
        ))
        db.create_unique(u'workout_exercise_workout', ['exercise_id', 'workout_id'])

        # Adding model 'Workout'
        db.create_table(u'workout_workout', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'workout', ['Workout'])


    def backwards(self, orm):
        # Deleting model 'ExerciseName'
        db.delete_table(u'workout_exercisename')

        # Deleting model 'WorkoutSet'
        db.delete_table(u'workout_workoutset')

        # Deleting model 'Exercise'
        db.delete_table(u'workout_exercise')

        # Removing M2M table for field workout on 'Exercise'
        db.delete_table('workout_exercise_workout')

        # Deleting model 'Workout'
        db.delete_table(u'workout_workout')


    models = {
        u'workout.exercise': {
            'Meta': {'object_name': 'Exercise'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workout.ExerciseName']"}),
            'workout': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['workout.Workout']", 'symmetrical': 'False'})
        },
        u'workout.exercisename': {
            'Meta': {'object_name': 'ExerciseName'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'exercise_category': ('django.db.models.fields.CharField', [], {'default': "'GEN'", 'max_length': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'workout.workout': {
            'Meta': {'object_name': 'Workout'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'workout.workoutset': {
            'Meta': {'object_name': 'WorkoutSet'},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workout.Exercise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percent_of_max': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'reps': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'rest_time': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'result': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'set_number': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'tempo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'workout_week': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '5'})
        }
    }

    complete_apps = ['workout']