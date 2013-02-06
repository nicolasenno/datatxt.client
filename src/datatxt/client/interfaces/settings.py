from datatxt.client import DatatxtMessageFactory as _
from zope.interface import Interface
from zope.schema import TextLine

class IDatatxtSettings(Interface):
    """
    Datatxt Preference Panel Interface
    """
    app_key = TextLine (
        title=u'Datatxt app key',
        description=_('help_datatxt_app_key',
            default=u"Please enter your application key"
        ),
        required=True,
        default=u'',
    )
    app_id = TextLine (
        title=u'Datatxt app id',
        description=_('help_datatxt_app_id',
            default=u"Please enter your application id"
        ),
        required=True,
        default=u'',
    )
    app_lang = TextLine (
        title=u'Datatxt language',
        description=_('help_datattx_lang',
            default=u'Please enter language for the enancher'
        ),
        required=True,
        default=u'it',
    )
    api_url = TextLine (
        title=u'Datatxt url',
        description=_('help_datatxt_url',
            default=u'Please enter Datatxt url'
        ),
        required=True,
        default=u'http://spaziodati.eu/datatxt/v3/',
    )
    rho = TextLine (
        title=u'Datatxt rho',
        description=_('help_datatxt_rho',
            default=u'Please enter rho number'
        ),
        required=True,
        default=u'0.1',
    )
    epsilon = TextLine (
        title=u'Datatxt epsilonIDatatxtSettings',
        description=_('help_datatxt_epsilon',
            default=u'Please enter epsilon'
        ),
        required=True,
        default=u'0.3',
    )
    long_text = TextLine (
        title=u'Datatxt long text',
        description=_('help_datatxt_long_text',
            default=u'Please enter lenght'
        ),
        required=True,
        default=u'0',
    )
    dbpedia = TextLine (
        title=u'Datatxt server port',
        description=_('help_dbpedia_url',
            default=u'Please enter DBpedia url'
        ),
        required=True,
        default=u'http://it.dbpedia.org',
    )

