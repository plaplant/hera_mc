import logging

from sqlalchemy import inspect
from sqlalchemy.ext.declarative.clsregistry import _ModuleMarker
from sqlalchemy.orm import RelationshipProperty

from hera_mc.mc import DEC_BASE

logger = logging.getLogger(__name__)


def is_sane_database(DEC_BASE, session):
    """
    Check whether the current database matches the models declared in model
    base.

    Currently we check that all tables exist with all columns.

    What is not checked:

    * Column types are not verified

    * Relationships are not verified at all (TODO)

    Parameters
    ----------
    DEC_BASE: Declarative Base for SQLAlchemy models to check

    session: SQLAlchemy session bound to an engine

    Returns
    ----------
    True if all declared models have corresponding tables and columns.
    """

    engine = session.get_bind()
    iengine = inspect(engine)

    errors = False

    tables = iengine.get_table_names()

    # Go through all SQLAlchemy models
    for name, klass in DEC_BASE._decl_class_registry.items():

        if isinstance(klass, _ModuleMarker):
            # Not a model
            continue

        table = klass.__tablename__
        if table in tables:
            # Check all columns are found
            # Looks like [{'default':
            #                  "nextval('sanity_check_test_id_seq'::regclass)",
            #              'autoincrement': True, 'nullable': False,
            #              'type': INTEGER(), 'name': 'id'}]

            columns = [c["name"] for c in iengine.get_columns(table)]
            mapper = inspect(klass)

            for column_prop in mapper.attrs:
                if isinstance(column_prop, RelationshipProperty):
                    # TODO: Add sanity checks for relations
                    pass
                else:
                    for column in column_prop.columns:
                        # Assume normal flat column
                        if column.key not in columns:
                            logger.error("Model %s declares column %s " +
                                         "which does not exist in database %s",
                                         klass, column.key, engine)
                            errors = True
        else:
            logger.error("Model %s declares table %s which does not exist " +
                         "in database %s", klass, table, engine)
            errors = True

    return not errors
