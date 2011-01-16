from django.conf.urls.defaults import patterns

urlpatterns = patterns('djreddit_css.views',
    (r'^$', 'css_index', None, 'css_index'),
    (r'^add_user/$', 'add_user', None, 'add_user'),
    (r'^list_css/$', 'list_css', None, 'list_css'),
    (r'^display_css/(?P<css_id>[-\d+])/$', 'display_css', None,
        'display_css'
    ),
)