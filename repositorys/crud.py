class CRUDRepository:

    def __init__(self, model, session):
        self.model = model
        self.session = session

    def get(self, obj_id, *args, **kwargs):
        with self.session as session:
            result = session.query(self.model).get(obj_id)
            if result is not None:
                return result
            return session.query(self.model).filter(**kwargs).first

    def list(self, *args, **kwargs):
        with self.session as session:
            result = session.query(self.model).filter(**kwargs).all()
            return result

    def update(self, *args, **kwargs):
        with self.session as session:
            session.update(self.model).values(**kwargs)

    def create(self, *args, **kwargs):
        with self.session as session:
            new_obj_of_model = self.model(**kwargs)
            session.add(new_obj_of_model)

    def delete(self, obj_id):
        with self.session as session:
            session.query(self.model).filter(self.model.id == obj_id).delete()
