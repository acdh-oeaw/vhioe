from rest_framework import renderers
from django.template.loader import render_to_string


class RDFRenderer(renderers.BaseRenderer):
    media_type = 'application/xml+rdf'
    format = 'xml'

    def render(self, data, media_type=None, renderer_context=None):
        data = render_to_string(
            "vocabs/RDF_renderer.xml", {'data': data, 'renderer_context': renderer_context})

        return data
