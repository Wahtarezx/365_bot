class CRUDRepository:

    def __init__(self, model, session):
        self.model = model
        self.session = session

    def get(self, obj_id, *args, **kwargs):
        with self.session as session:
            result = session.query(self.model).get(obj_id)
            return result

    def list(self, *args, **kwargs):
        ...

    def update(self, *args, **kwargs):
        with self.session as session:
            self.session.update(self.model).values(**kwargs)

    def create(self, *args, **kwargs):
        with self.session as session:
            new_obj_of_model = self.model(**kwargs)
            session.add(new_obj_of_model)

    def delete(self, obj_id):
        with self.session as session:
            session.query(self.model).filter(self.model.id == obj_id).delete()
