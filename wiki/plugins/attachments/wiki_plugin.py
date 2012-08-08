# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url
from django.utils.translation import ugettext as _

from wiki.core import plugins_registry
from wiki.plugins.attachments import views
from wiki.plugins.attachments import settings

class AttachmentPlugin(plugins_registry.BasePlugin):
    
    #settings_form = 'wiki.plugins.notifications.forms.SubscriptionForm'
    
    slug = settings.SLUG
    urlpatterns = patterns('',
        url('^$', views.AttachmentView.as_view(), name='attachments_index'),
        url('^replace/(?P<attachment_id>\d+)/$', views.AttachmentReplaceView.as_view(), name='attachments_replace'),
        url('^history/(?P<attachment_id>\d+)/$', views.AttachmentHistoryView.as_view(), name='attachments_history'),
        url('^download/(?P<attachment_id>\d+)/$', views.AttachmentDownloadView.as_view(), name='attachments_download'),
        url('^delete/(?P<attachment_id>\d+)/$', views.AttachmentDeleteView.as_view(), name='attachments_delete'),
        url('^download/(?P<attachment_id>\d+)/revision/(?P<revision_id>\d+)/$', views.AttachmentDownloadView.as_view(), name='attachments_download'),
        url('^change/(?P<attachment_id>\d+)/revision/(?P<revision_id>\d+)/$', views.AttachmentChangeRevisionView.as_view(), name='attachments_revision_change'),
    )
    article_tab = (_(u'Attachments'), "icon-file")
    article_view = views.AttachmentView().dispatch
    article_template_append = 'wiki/plugins/attachments/append.html'
    
    def __init__(self):
        #print "I WAS LOADED!"
        pass
    
plugins_registry.register(AttachmentPlugin)
