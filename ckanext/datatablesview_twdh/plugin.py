# encoding: utf-8

import ckan.plugins as p
import ckan.plugins.toolkit as toolkit
from ckanext.datatablesview_twdh import blueprint

default = toolkit.get_validator(u'default')
boolean_validator = toolkit.get_validator(u'boolean_validator')
ignore_missing = toolkit.get_validator(u'ignore_missing')


class DatatablesviewPlusPlugin(p.SingletonPlugin):
    u'''
    DataTables table view plugin using v1.12.1 of DataTables
    '''
    p.implements(p.IConfigurer, inherit=True)
    p.implements(p.IResourceView, inherit=True)
    p.implements(p.IBlueprint)

    # IBlueprint

    def get_blueprint(self):
        return blueprint.datatablesview_twdh

    # IConfigurer

    def update_config(self, config):
        u'''
        Set up the resource library, public directory and
        template directory for the view
        '''
        toolkit.add_template_directory(config, u'templates')
        toolkit.add_public_directory(config, 'public')
        toolkit.add_resource(u'assets', u'ckanext-datatablesview_twdh')

    # IResourceView

    def can_view(self, data_dict):
        resource = data_dict['resource']
        return resource.get(u'datastore_active')

    def view_template(self, context, data_dict):
        return u'datatables/datatables_view.html'

    def form_template(self, context, data_dict):
        return u'datatables/datatables_form.html'

    def info(self):
        return {
            u'name': u'datatablesview_twdh',
            u'title': u'Table',
            u'filterable': True,
            u'icon': u'table',
            u'requires_datastore': True,
            u'default_title': p.toolkit._(u'Table'),
            u'schema': {
                u'responsive': [default(False), boolean_validator],
                u'show_fields': [ignore_missing],
                u'filterable': [default(True), boolean_validator],
            }
        }

