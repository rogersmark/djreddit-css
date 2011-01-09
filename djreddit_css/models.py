from django.db import models

class SubReddit(models.Model):
    """
    Everything is grouped into SubReddits. This allows one instance to 
    support multiple SubReddits in the future.
    
    name: Name of the SubReddit
    css_start_chunk: Start of the CSS
    css_end_chunk: End of the CSS
    
    The idea is we'll dynamically fill in the meaty middle.
    """
    
    name = models.CharField(max_length=128)
    css_start_chunk = models.TextField()
    css_end_chunk = models.TextField()
    
    def __unicode__(self):
        return u'%s' % self.name
        
    @models.permalink
    def get_absolute_url(self):
        return ('display_css', (), {'css_id': self.id})

class Grouping(models.Model):
    """
    For example, in /r/mls, users have crests based off their team's crest.
    We group users by their crests to build the CSS
    """
    
    name = models.CharField(max_length=128)
    subreddit = models.ForeignKey(SubReddit)
    content_href = models.CharField(max_length=128)
    content = models.CharField(max_length=128, blank=True, null=True)
    background_pos = models.CharField(max_length=128, blank=True, null=True)
    
    def __unicode__(self):
        return u'%s' % self.name
        
class RedditUser(models.Model):
    """
    Our user, and what 'bucket' they belong in.
    """
    
    name = models.CharField(max_length=128)
    grouping = models.ForeignKey(Grouping)
    
    def __unicode__(self):
        return u'%s' % self.name