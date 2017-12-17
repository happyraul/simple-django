import operator as _op

from django import http as _http
from django import shortcuts as _shortcuts

from . import models as _models

def index(request):
    sites = _models.Site.objects.order_by('id')
    context = dict(sites=sites, active='sites')
    return _shortcuts.render(request, 'tmw/index.html', context)

def detail(request, site_id):
    site = _shortcuts.get_object_or_404(_models.Site, pk=site_id)
    context = dict(site=site, active='sites')
    return _shortcuts.render(request, 'tmw/site.html', context)

def summary_sum(request):
    sites = _models.Site.objects.raw(
        'select s.*, sum(a) as a, sum(b) as b '
        'from tmw_site s join tmw_value v on s.id = v.site_id '
        'group by name '
        'order by s.id'
    )
    context = dict(sites=sites, active='sum')
    return _shortcuts.render(request, 'tmw/summary.html', context)

def summary_average(request):
    def _get_values(col, site):
        return list(map(_op.attrgetter(col), site.value_set.all()))

    sites = _models.Site.objects.order_by('id')
    sites = [
        dict(name=site.name, 
             a=sum(_get_values('a', site)) / len(_get_values('a', site)),
             b=sum(_get_values('b', site)) / len(_get_values('b', site)))
        for site in sites
    ]
    context = dict(sites=sites, active='average')
    return _shortcuts.render(request, 'tmw/summary.html', context)

