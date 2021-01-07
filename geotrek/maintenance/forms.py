from django import forms
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.forms import FloatField
from django.utils.translation import gettext_lazy as _
from django.forms.models import inlineformset_factory

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout, Div, HTML

from geotrek.common.forms import CommonForm
from geotrek.core.fields import TopologyField
from geotrek.core.models import Topology
from geotrek.core.widgets import TopologyReadonlyWidget

from .models import Intervention, Project


class ManDayForm(forms.ModelForm):

    class Meta:
        fields = ('id', 'nb_days', 'job')

    def __init__(self, *args, **kwargs):
        super(ManDayForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout('id', 'nb_days', 'job')
        self.fields['nb_days'].widget.attrs['placeholder'] = _('Days')
        self.fields['nb_days'].label = ''
        self.fields['nb_days'].widget.attrs['class'] = 'input-mini'
        self.fields['job'].widget.attrs['class'] = 'input-medium'


ManDayFormSet = inlineformset_factory(Intervention, Intervention.jobs.through, form=ManDayForm, extra=1)


class FundingForm(forms.ModelForm):

    class Meta:
        fields = ('id', 'amount', 'organism')

    def __init__(self, *args, **kwargs):
        super(FundingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout('id', 'amount', 'organism')
        self.fields['organism'].widget.attrs['class'] = 'input-xlarge'


FundingFormSet = inlineformset_factory(Project, Project.founders.through, form=FundingForm, extra=1)


class InterventionForm(CommonForm):
    """ An intervention can be a Point or a Line """

    topology = TopologyField(label="")
    length = FloatField(required=False, label=_("Length"))
    project = forms.ModelChoiceField(required=False, label=_("Project"),
                                     queryset=Project.objects.existing())

    geomfields = ['topology']
    leftpanel_scrollable = False

    fieldslayout = [
        Div(
            HTML(
                """<ul class="nav nav-tabs">
    <li id="tab-main" class="nav-item">
        <a class="nav-link active" href="#main" data-toggle="tab"><i class="bi bi-card-list"></i> {0}</a>
    </li>
    <li id="tab-advanced" class="nav-item">
        <a class="nav-link" href="#advanced" data-toggle="tab"><i class="bi bi-list-ul"></i> {1}</a>
    </li>
</ul>""".format(_("Main"), _("Advanced"))),
            Div(
                Div(
                    'structure',
                    'name',
                    'date',
                    'status',
                    'disorders',
                    'type',
                    'subcontracting',
                    'length',
                    'width',
                    'height',
                    'stake',
                    'project',
                    'description',
                    css_id="main",
                    css_class="tab-pane active"
                ),
                Div(
                    'material_cost',
                    'heliport_cost',
                    'subcontract_cost',
                    Fieldset(_("Mandays")),
                    css_id="advanced",  # used in Javascript for activating tab if error
                    css_class="tab-pane"
                ),
                css_class="scrollable tab-content"
            ),
            css_class="tabbable"
        ),
    ]

    class Meta(CommonForm.Meta):
        model = Intervention
        fields = CommonForm.Meta.fields + \
            ['structure', 'name', 'date', 'status', 'disorders', 'type', 'description', 'subcontracting', 'length', 'width',
             'height', 'stake', 'project', 'material_cost', 'heliport_cost', 'subcontract_cost', 'topology']

    def __init__(self, *args, target_type=None, target_id=None, **kwargs):
        super(InterventionForm, self).__init__(*args, **kwargs)

        if not self.instance.pk:
            # New intervention. We have to set its target.
            if target_type and target_id:
                # Point target to an existing topology
                ct = ContentType.objects.get_for_id(target_type)
                self.instance.target = ct.get_object_for_this_type(id=target_id)
                # Set POST URL
                self.helper.form_action += '?target_type={}&target_id={}'.format(target_type, target_id)
            else:
                # Point target to a new topology
                self.instance.target = Topology()
        # Else: existing intervention. Target is already set

        self.fields['topology'].initial = self.instance.target

        if self.instance.target.__class__ == Topology:
            # Intervention has its own topology
            title = _("On {}".format(_("Paths")))
            self.fields['topology'].label = \
                '<img src="{prefix}images/path-16.png" title="{title}">{title}'.format(
                    prefix=settings.STATIC_URL, title=title
            )
        else:
            # Intervention on an existing topology
            icon = self.instance.target._meta.model_name
            title = _("On {}".format(str(self.instance.target)))
            self.fields['topology'].label = \
                '<img src="{prefix}images/{icon}-16.png" title="{title}"><a href="{url}">{title}</a>'.format(
                    prefix=settings.STATIC_URL, icon=icon, title=title,
                    url=self.instance.target.get_detail_url()
            )
            # Topology is readonly
            self.fields['topology'].required = False
            self.fields['topology'].widget = TopologyReadonlyWidget()

        # Length is not editable in AltimetryMixin
        self.fields['length'].initial = self.instance.length
        editable = bool(self.instance.geom and (self.instance.geom.geom_type == 'Point'
                        or self.instance.geom.geom_type == 'LineString'))
        self.fields['length'].widget.attrs['readonly'] = editable

    def save(self, *args, **kwargs):
        target = self.instance.target
        if not target.pk:
            target.save()
        topology = self.cleaned_data.pop('topology')
        if topology and topology.pk != target.pk:
            target.mutate(topology)
        intervention = super().save(*args, **kwargs, commit=False)
        intervention.target = target
        intervention.save()
        self.save_m2m()
        return intervention


class ProjectForm(CommonForm):
    fieldslayout = [
        Div(
            Div(
                Div('structure',
                    'name',
                    'type',
                    'domain',
                    'begin_year',
                    'end_year',
                    'constraint',
                    'global_cost',
                    'comments',

                    css_class="span6"),
                Div('project_owner',
                    'project_manager',
                    'contractors',
                    Fieldset(_("Fundings")),
                    css_class="span6"),
                css_class="row-fluid"
            ),
            css_class="container-fluid"
        ),
    ]

    class Meta(CommonForm.Meta):
        model = Project
        fields = CommonForm.Meta.fields + \
            ['structure', 'name', 'type', 'domain', 'begin_year', 'end_year', 'constraint',
             'global_cost', 'comments', 'project_owner', 'project_manager', 'contractors']

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.helper.form_tag = False
