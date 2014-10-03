# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Workout'
        db.delete_table(u'workout_workout')

        # Removing M2M table for field exercise_sets on 'Workout'
        db.delete_table('workout_workout_exercise_sets')

        # Adding model 'Routine'
        db.create_table(u'workout_routine', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Account'])),
            ('note', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'workout', ['Routine'])

        # Adding M2M table for field days on 'Routine'
        db.create_table(u'workout_routine_days', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('routine', models.ForeignKey(orm[u'workout.routine'], null=False)),
            ('day', models.ForeignKey(orm[u'workout.day'], null=False))
        ))
        db.create_unique(u'workout_routine_days', ['routine_id', 'day_id'])

        # Adding model 'Day'
        db.create_table(u'workout_day', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('due_date', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 10, 3, 0, 0))),
        ))
        db.send_create_signal(u'workout', ['Day'])

        # Adding M2M table for field exercise_sets on 'Day'
        db.create_table(u'workout_day_exercise_sets', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('day', models.ForeignKey(orm[u'workout.day'], null=False)),
            ('exerciseset', models.ForeignKey(orm[u'workout.exerciseset'], null=False))
        ))
        db.create_unique(u'workout_day_exercise_sets', ['day_id', 'exerciseset_id'])

        # Deleting field 'ExerciseSet.workout'
        db.delete_column(u'workout_exerciseset', 'workout_id')

        # Adding field 'ExerciseSet.day'
        db.add_column(u'workout_exerciseset', 'day',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['workout.Day']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Workout'
        db.create_table(u'workout_workout', (
            ('note', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('start', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 9, 30, 0, 0))),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['account.Account'])),
            ('end', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 9, 30, 0, 0))),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'workout', ['Workout'])

        # Adding M2M table for field exercise_sets on 'Workout'
        db.create_table(u'workout_workout_exercise_sets', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('workout', models.ForeignKey(orm[u'workout.workout'], null=False)),
            ('exerciseset', models.ForeignKey(orm[u'workout.exerciseset'], null=False))
        ))
        db.create_unique(u'workout_workout_exercise_sets', ['workout_id', 'exerciseset_id'])

        # Deleting model 'Routine'
        db.delete_table(u'workout_routine')

        # Removing M2M table for field days on 'Routine'
        db.delete_table('workout_routine_days')

        # Deleting model 'Day'
        db.delete_table(u'workout_day')

        # Removing M2M table for field exercise_sets on 'Day'
        db.delete_table('workout_day_exercise_sets')

        # Adding field 'ExerciseSet.workout'
        db.add_column(u'workout_exerciseset', 'workout',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['workout.Workout']),
                      keep_default=False)

        # Deleting field 'ExerciseSet.day'
        db.delete_column(u'workout_exerciseset', 'day_id')


    models = {
        u'account.account': {
            'Meta': {'ordering': "['-created_date']", 'object_name': 'Account'},
            'college': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 10, 3, 0, 0)'}),
            'grad_year': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'high_school': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
        u'workout.day': {
            'Meta': {'object_name': 'Day'},
            'due_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 10, 3, 0, 0)'}),
            'exercise_sets': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'ExerciseSet'", 'symmetrical': 'False', 'to': u"orm['workout.ExerciseSet']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'workout.exerciseset': {
            'Meta': {'object_name': 'ExerciseSet'},
            'day': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workout.Day']"}),
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['workout.ExerciseType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'minutes': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'rep_info': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'reps': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'rest_minutes': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'rest_seconds': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'result': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'seconds': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'set_number': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '4'}),
            'tempo': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'workout.exercisetype': {
            'Meta': {'object_name': 'ExerciseType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'workout.routine': {
            'Meta': {'object_name': 'Routine'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['account.Account']"}),
            'days': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Day'", 'symmetrical': 'False', 'to': u"orm['workout.Day']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['workout']