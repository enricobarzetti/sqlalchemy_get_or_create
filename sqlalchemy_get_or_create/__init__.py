from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

__version__ = '0.1.2'


def _extract_model_params(defaults, **kwargs):
    defaults = defaults or {}
    ret = {}
    ret.update(kwargs)
    ret.update(defaults)
    return ret


def _create_object_from_params(session, model, lookup, params, lock=False):
    obj = model(**params)
    session.add(obj)
    try:
        with session.begin_nested():
            session.flush()
    except IntegrityError:
        session.rollback()
        query = session.query(model).filter_by(**lookup)
        if lock:
            query = query.with_for_update()
        try:
            obj = query.one()
        except NoResultFound:
            raise
        else:
            return obj, False
    else:
        return obj, True


def get_or_create(session,
                  model,
                  defaults=None,
                  **kwargs):
    try:
        return session.query(model).filter_by(**kwargs).one(), False
    except NoResultFound:
        params = _extract_model_params(defaults, **kwargs)
        return _create_object_from_params(session, model, kwargs, params)


def update_or_create(session, model, defaults=None, **kwargs):
    defaults = defaults or {}
    with session.begin_nested():
        try:
            obj = session.query(model).with_for_update().filter_by(**kwargs).one()
        except NoResultFound:
            params = _extract_model_params(defaults, **kwargs)
            obj, created = _create_object_from_params(session, model, kwargs, params, lock=True)
            if created:
                return obj, created
        for k, v in defaults.items():
            setattr(obj, k, v)
        session.add(obj)
        session.flush()
    return obj, False
