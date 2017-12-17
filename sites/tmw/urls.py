from django import urls as _urls

from . import views as _views

urlpatterns = [
    _urls.path('', _views.index, name='index'),
    _urls.path('sites/', _views.index, name='index'),
    _urls.path('sites/<int:site_id>/', _views.detail, name='detail'),
    _urls.path('summary', _views.summary_sum, name='sum'),
    _urls.path('summary-average', _views.summary_average, name='average'),
]

