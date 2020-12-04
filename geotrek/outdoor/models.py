from django.conf import settings
from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from geotrek.authent.models import StructureRelated
from geotrek.common.mixins import NoDeleteMixin, TimeStampedModelMixin, AddPropertyMixin
from geotrek.common.utils import intersecting
from geotrek.core.models import Path, Topology, Trail
from geotrek.infrastructure.models import Infrastructure
from geotrek.signage.models import Signage
from geotrek.tourism.models import TouristicContent, TouristicEvent
from geotrek.trekking.models import Trek, POI
from geotrek.zoning.models import City, District, RestrictedArea
from mapentity.models import MapEntityMixin


class Site(AddPropertyMixin, MapEntityMixin, StructureRelated,
           TimeStampedModelMixin, NoDeleteMixin):
    geom = models.GeometryField(verbose_name=_("Location"), srid=settings.SRID)
    name = models.CharField(verbose_name=_("Name"), max_length=128)
    description = models.TextField(verbose_name=_("Description"), blank=True)
    eid = models.CharField(verbose_name=_("External id"), max_length=1024, blank=True, null=True)

    class Meta:
        verbose_name = _("Site")
        verbose_name_plural = _("Sites")
        ordering = ('name', )

    def __str__(self):
        return self.name

    @property
    def name_display(self):
        return '<a data-pk="{pk}" href="{url}" title="{name}">{name}</a>'.format(
            pk=self.pk,
            url=self.get_detail_url(),
            name=self.name
        )

    def distance(self, to_cls):
        """Distance to associate this site to another class"""
        return None


Path.add_property('sites', lambda self: intersecting(Site, self), _("Sites"))
Topology.add_property('sites', lambda self: intersecting(Site, self), _("Sites"))
TouristicContent.add_property('sites', lambda self: intersecting(Site, self), _("Sites"))
TouristicEvent.add_property('sites', lambda self: intersecting(Site, self), _("Sites"))

Site.add_property('sites', lambda self: intersecting(Site, self), _("Sites"))
Site.add_property('treks', lambda self: intersecting(Trek, self), _("Treks"))
Site.add_property('pois', lambda self: intersecting(POI, self), _("POIs"))
Site.add_property('trails', lambda self: intersecting(Trail, self), _("Trails"))
Site.add_property('infrastructures', lambda self: intersecting(Infrastructure, self), _("Infrastructures"))
Site.add_property('signages', lambda self: intersecting(Signage, self), _("Signages"))
Site.add_property('touristic_contents', lambda self: intersecting(TouristicContent, self), _("Touristic contents"))
Site.add_property('touristic_events', lambda self: intersecting(TouristicEvent, self), _("Touristic events"))
Site.add_property('cities', lambda self: intersecting(City, self, distance=0), _("Cities"))
Site.add_property('districts', lambda self: intersecting(District, self, distance=0), _("Districts"))
Site.add_property('areas', lambda self: intersecting(RestrictedArea, self, distance=0), _("Restricted areas"))
