from django.views.generic import TemplateView

page1_view = TemplateView.as_view(template_name='sample/page1.html')
page2_view = TemplateView.as_view(template_name='sample/page2.html')
