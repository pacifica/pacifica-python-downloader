#!/usr/bin/python
"""Cloud Event Parser."""
from os.path import join


class CloudEvent(object):
    """Cloud Event Parser."""

    @staticmethod
    def yield_files(cloudevent):
        """returned lambda method for yield files."""
        def ce_yield_files():
            """yield files from a cloudevent object."""
            for obj in cloudevent.get('data', []):
                if obj.get('destinationTable', False) == 'Files':
                    yield {
                        'id': obj.get('_id', False),
                        'path': '{}/{}'.format(obj.get('subdir', ''), obj.get('name', False)),
                        'hashsum': obj.get('hashsum', False),
                        'hashtype': obj.get('hashtype', False)
                    }
        return ce_yield_files
