# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WorkoutSet'
        db.create_table(u'workout_workoutset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('workout_week', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.WorkoutWeek'])),
            ('set_info', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('set_parent', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=4, null=True, blank=True)),
        ))
        db.send_create_signal(u'workout', ['WorkoutSet'])

        # Adding model 'WorkoutWeek'
        db.create_table(u'workout_workoutweek', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('set_number', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=3, null=True, blank=True)),
            ('percent_of_max', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('tempo', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('rest_time', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('reps', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=4, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=4, null=True, blank=True)),
            ('workout_week', self.gf('django.db.models.fields.CharField')(default='1', max_length=5)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Exercise'])),
            ('workout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Workout'])),
        ))
        db.send_create_signal(u'workout', ['WorkoutWeek'])

        # Adding model 'Exercise'
        db.create_table(u'workout_exercise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exercise.ExerciseName'])),
            ('workout', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Workout'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'workout', ['Exercise'])

        # Adding model 'Workout'
        db.create_table(u'workout_workout', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Account'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('created_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 10, 22, 0, 0))),
            ('exercise_category', self.gf('django.db.models.fields.CharField')(default='GEN', max_length=4)),
        ))
        db.send_create_signal(u'workout', ['Workout'])


    def backwards(self, orm):
        # Deleting model 'WorkoutSet'
        db.delete_table(u'workout_workoutset')

        # Deleting model 'WorkoutWeek'
        db.delete_table(u'workout_workoutweek')

        # Deleting model 'Exercise'
        db.delete_table(u'workout_exercise')

        # Deleting model 'Workout'
        db.delete_table(u'workout_workout')


    models = {
        u'account.account': {
            'Meta': {'ordering': "['-created_date']", 'object_name': 'Account'},
            'college': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 10, 22, 0, 0)'}),
            'grad_year': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'high_school': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'profile_image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'account'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
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
        u'exercise.exercisename': {
            'Meta': {'ordering': "['name']", 'object_name': 'ExerciseName'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'workout.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exercise.ExerciseName']"}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workout.Workout']"})
        },
        u'workout.workout': {
            'Meta': {'object_name': 'Workout'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Account']"}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 10, 22, 0, 0)'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'exercise_category': ('django.db.models.fields.CharField', [], {'default': "'GEN'", 'max_length': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'workout.workoutset': {
            'Meta': {'object_name': 'WorkoutSet'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'set_info': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'set_parent': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'workout_week': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workout.WorkoutWeek']"})
        },
        u'workout.workoutweek': {
            'Meta': {'object_name': 'WorkoutWeek'},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workout.Exercise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percent_of_max': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'reps': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'rest_time': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'set_number': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'tempo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'workout': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workout.Workout']"}),
            'workout_week': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '5'})
        }
    }

    complete_apps = ['workout']