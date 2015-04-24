from __future__ import unicode_literals

from dateutil.parser import parse

from .helpers import (
    default_name_parser,
    oai_extract_url,
    oai_process_contributors,
    compose,
    single_result,
    format_tags,
    build_properties
)

CONSTANT = lambda x: lambda *_, **__: x


DOESCHEMA = {
    "description": ('//dc:description/node()', compose(lambda x: x.strip(), single_result)),
    "contributors": ('//dc:creator/node()', compose(default_name_parser, lambda x: x.split(';'), single_result)),
    "title": ('//dc:title/node()', compose(lambda x: x.strip(), single_result)),
    "providerUpdatedDateTime": ('//dc:dateEntry/node()', compose(lambda x: x.strip(), single_result)),
    "uris": {
        "canonicalUri": ('//dcq:identifier-citation/node()', compose(lambda x: x.strip(), single_result)),
    },
    "otherProperties": build_properties(
        ('coverage', '//dc:coverage/node()'),
        ('date', '//dc:date/node()'),
        ('format', '//dc:format/node()'),
        ('identifier', '//dc:identifier/node()'),
        ('identifierDOEcontract', '//dcq:identifierDOEcontract/node()'),
        ('identifierOther', '//dc:identifierOther/node()'),
        ('identifier-purl', '//dc:identifier-purl/node()'),
        ('identifierReport', '//dc:identifierReport/node()'),
        ('language', '//dc:language/node()'),
        ('publisher', '//dcq:publisher/node()'),
        ('publisherAvailability', '//dcq:publisherAvailability/node()'),
        ('publisherCountry', '//dcq:publisherCountry/node()'),
        ('publisherResearch', '//dcq:publisherResearch/node()'),
        ('publisherSponsor', '//dcq:publisherSponsor/node()'),
        ('relation', '//dc:relation/node()'),
        ('rights', '//dc:rights/node()'),
        ('type', '//dc:type/node()'),
        ('typeQualifier', '//dc:typeQualifier/node()')
    )
}

OAISCHEMA = {
    "contributors": ('//dc:creator/node()', '//dc:contributor/node()', oai_process_contributors),
    "uris": {
        "canonicalUri": ('//dc:identifier/node()', oai_extract_url)
    },
    'providerUpdatedDateTime': ('//ns0:header/ns0:datestamp/node()', lambda x: parse(x[0]).replace(tzinfo=None).isoformat()),
    'title': ('//dc:title/node()', single_result),
    'description': ('//dc:description/node()', single_result),
    'tags': ('//dc:subject/node()', format_tags)
}
