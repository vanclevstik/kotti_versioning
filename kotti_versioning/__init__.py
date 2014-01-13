from pyramid.i18n import TranslationStringFactory

from kotti import DBSession
from kotti.resources import Node
from kotti_versioning.history_meta import versioned_session, Versioned

from logging import getLogger
log = getLogger('kotti_versioning: ')

_ = TranslationStringFactory('kotti_versioning')






def kotti_configure(settings):

    Node.__bases__ += (Versioned)
    versioned_session(DBSession)

    settings['pyramid.includes'] += ' kotti_versioning.include_versioning'

    # We override nav.pt.
    settings['kotti.asset_overrides'] = 'kotti_versioning:kotti-overrides/'


def include_versioning(config):  # pragma: no cover

    config.add_translation_dirs('kotti_versioning:locale')
    config.scan(__name__)
