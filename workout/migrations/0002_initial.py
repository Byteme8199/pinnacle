# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ExerciseType'
        db.create_table(u'workout_exercisetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'workout', ['ExerciseType'])

        # Adding model 'Exercise'
        db.create_table(u'workout_exercise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('movement_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.ExerciseType'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 9, 25, 0, 0))),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'workout', ['Exercise'])

        # Adding model 'ExerciseSet'
        db.create_table(u'workout_exerciseset', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('set_number', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=4)),
            ('reps', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=4, null=True, blank=True)),
            ('rep_info', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('minutes', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=3, null=True, blank=True)),
            ('seconds', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=2, null=True, blank=True)),
            ('rest_minutes', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=3, null=True, blank=True)),
            ('rest_seconds', self.gf('django.db.models.fields.PositiveSmallIntegerField')(max_length=2, null=True, blank=True)),
            ('tempo', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('result', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('note', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['workout.Exercise'])),
        ))
        db.send_create_signal(u'workout', ['ExerciseSet'])

        # Adding model 'Workout'
        db.create_table(u'workout_workout', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Account'])),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('note', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'workout', ['Workout'])

        # Adding M2M table for field exercise_sets on 'Workout'
        db.create_table(u'workout_workout_exercise_sets', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('workout', models.ForeignKey(orm[u'workout.workout'], null=False)),
            ('exerciseset', models.ForeignKey(orm[u'workout.exerciseset'], null=False))
        ))
        db.create_unique(u'workout_workout_exercise_sets', ['workout_id', 'exerciseset_id'])


    def backwards(self, orm):
        # Deleting model 'ExerciseType'
        db.delete_table(u'workout_exercisetype')

        # Deleting model 'Exercise'
        db.delete_table(u'workout_exercise')

        # Deleting model 'ExerciseSet'
        db.delete_table(u'workout_exerciseset')

        # Deleting model 'Workout'
        db.delete_table(u'workout_workout')

        # Removing M2M table for field exercise_sets on 'Workout'
        db.delete_table('workout_workout_exercise_sets')


    models = {
        u'account.account': {
            'Meta': {'ordering': "['-created_date']", 'object_name': 'Account'},
            'college': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 25, 0, 0)'}),
            'grad_year': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'high_school': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
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
        u'workout.exercise': {
            'Meta': {'object_name': 'Exercise'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 9, 25, 0, 0)'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movement_name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workout.ExerciseType']"})
        },
        u'workout.exerciseset': {
            'Meta': {'object_name': 'ExerciseSet'},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workout.Exercise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minutes': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'rep_info': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'reps': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'rest_minutes': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'rest_seconds': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'result': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'seconds': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'set_number': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '4'}),
            'tempo': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'workout.exercisetype': {
            'Meta': {'object_name': 'ExerciseType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'workout.workout': {
            'Meta': {'object_name': 'Workout'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Account']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'exercise_sets': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['workout.ExerciseSet']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['workout']