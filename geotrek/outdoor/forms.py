from crispy_forms.layout import Div
from geotrek.common.forms import CommonForm
from geotrek.outdoor.models import Site


class SiteForm(CommonForm):
    geomfields = ['geom']

    fieldslayout = [
        Div(
            'structure',
            'name',
            'parent',
            'review',
            'published',
            'practice',
            'description',
            'description_teaser',
            'ambiance',
            'advice',
            'period',
            'orientation',
            'wind',
            'labels',
            'themes',
            'portal',
            'source',
            'information_desks',
            'web_links',
            'type',
            'eid',
        )
    ]

    class Meta:
        fields = ['geom', 'structure', 'name', 'review', 'published', 'practice', 'description',
                  'description_teaser', 'ambiance', 'advice', 'period', 'labels', 'themes',
                  'portal', 'source', 'information_desks', 'web_links', 'type', 'parent', 'eid',
                  'orientation', 'wind']
        model = Site

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            descendants = self.instance.get_descendants(include_self=True).values_list('pk', flat=True)
            self.fields['parent'].queryset = Site.objects.exclude(pk__in=descendants)
