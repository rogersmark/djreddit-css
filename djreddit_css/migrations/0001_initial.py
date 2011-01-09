# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SubReddit'
        db.create_table('djreddit_css_subreddit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('css_start_chunk', self.gf('django.db.models.fields.TextField')()),
            ('css_end_chunk', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('djreddit_css', ['SubReddit'])

        # Adding model 'Grouping'
        db.create_table('djreddit_css_grouping', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('subreddit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['djreddit_css.SubReddit'])),
            ('content_href', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('djreddit_css', ['Grouping'])

        # Adding model 'RedditUser'
        db.create_table('djreddit_css_reddituser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('grouping', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['djreddit_css.Grouping'])),
        ))
        db.send_create_signal('djreddit_css', ['RedditUser'])


    def backwards(self, orm):
        
        # Deleting model 'SubReddit'
        db.delete_table('djreddit_css_subreddit')

        # Deleting model 'Grouping'
        db.delete_table('djreddit_css_grouping')

        # Deleting model 'RedditUser'
        db.delete_table('djreddit_css_reddituser')


    models = {
        'djreddit_css.grouping': {
            'Meta': {'object_name': 'Grouping'},
            'content_href': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'subreddit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['djreddit_css.SubReddit']"})
        },
        'djreddit_css.reddituser': {
            'Meta': {'object_name': 'RedditUser'},
            'grouping': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['djreddit_css.Grouping']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'djreddit_css.subreddit': {
            'Meta': {'object_name': 'SubReddit'},
            'css_end_chunk': ('django.db.models.fields.TextField', [], {}),
            'css_start_chunk': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['djreddit_css']
