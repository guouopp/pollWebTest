# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'poll_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'poll', ['Category'])

        # Adding model 'Items'
        db.create_table(u'poll_items', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['poll.Category'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('point', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal(u'poll', ['Items'])

        # Adding model 'Evaluation'
        db.create_table(u'poll_evaluation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('is_used', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'poll', ['Evaluation'])

        # Adding model 'EvaluationItems'
        db.create_table(u'poll_evaluationitems', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('evaluation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['poll.Evaluation'])),
            ('items', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['poll.Items'])),
        ))
        db.send_create_signal(u'poll', ['EvaluationItems'])

        # Adding model 'StaffEvaluation'
        db.create_table(u'poll_staffevaluation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('staff', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['staff.Staff'])),
            ('evaluation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['poll.Evaluation'])),
            ('items', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['poll.Items'])),
            ('point', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal(u'poll', ['StaffEvaluation'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'poll_category')

        # Deleting model 'Items'
        db.delete_table(u'poll_items')

        # Deleting model 'Evaluation'
        db.delete_table(u'poll_evaluation')

        # Deleting model 'EvaluationItems'
        db.delete_table(u'poll_evaluationitems')

        # Deleting model 'StaffEvaluation'
        db.delete_table(u'poll_staffevaluation')


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
        u'poll.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'poll.evaluation': {
            'Meta': {'object_name': 'Evaluation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_used': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'poll.evaluationitems': {
            'Meta': {'object_name': 'EvaluationItems'},
            'evaluation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poll.Evaluation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poll.Items']"})
        },
        u'poll.items': {
            'Meta': {'object_name': 'Items'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poll.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'point': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        u'poll.staffevaluation': {
            'Meta': {'object_name': 'StaffEvaluation'},
            'evaluation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poll.Evaluation']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['poll.Items']"}),
            'point': ('django.db.models.fields.SmallIntegerField', [], {}),
            'staff': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['staff.Staff']"})
        },
        u'staff.staff': {
            'Meta': {'object_name': 'Staff'},
            'had_poll': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'poll_num': ('django.db.models.fields.SmallIntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'poll_right': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'score': ('django.db.models.fields.FloatField', [], {'default': '0.0', 'null': 'True', 'blank': 'True'}),
            'score_right': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'scored_right': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'vote_right': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        }
    }

    complete_apps = ['poll']