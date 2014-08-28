from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _
from itcq.plugins.itcqpicture.models import ITCQPicture
# from cms.settings import CMS_MEDIA_URL
from django.conf import settings


class ITCQPicturePlugin(CMSPluginBase):
    model = ITCQPicture
    name = _("Picture (with postion and caption)")
    render_template = "itcq/plugins/itcqpicture.html"
    text_enabled = True
    
    def render(self, context, instance, placeholder):
        context.update({
            'picture':instance, 
            'placeholder':placeholder
        })
        return context 
    
    def icon_src(self, instance):
        # TODO - possibly use 'instance' and provide a thumbnail image
        return settings.MEDIA_URL + u"images/plugins/image.png"
 
plugin_pool.register_plugin(ITCQPicturePlugin)
