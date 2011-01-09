# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Grouping.content'
        db.add_column('djreddit_css_grouping', 'content', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)

        # Adding field 'Grouping.background_pos'
        db.add_column('djreddit_css_grouping', 'background_pos', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Grouping.content'
        db.delete_column('djreddit_css_grouping', 'content')

        # Deleting field 'Grouping.background_pos'
        db.delete_column('djreddit_css_grouping', 'background_pos')


    models = {
        'djreddit_css.grouping': {
            'Meta': {'object_name': 'Grouping'},
            'background_pos': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
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
