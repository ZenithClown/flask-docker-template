# -*- encoding: utf-8 -*-

# define base model schema for all basic models

class ModelSchema(object):
    """Base Model Schema

    The base model schema can be inherited by any `db.model` class, 
    as this provides some functions helpful for development,
    representation and fetching records from `repository`.

    ```python
      class NewTableView(db.Model, ModelSchema):
        '''docstring'''

        __tablename__ = 'my_table'

        # provide field defination here


        def __init__(self):
            ModelSchema().__init__()

      class Repository(object):
        '''docstring'''

        def get(self) -> list:
            return [record.__to_dict__() for record in NewTableView.query.all()]
    ```

    The base class exposes two dunder methods: `repr` and `str` for any
    class, that can be used by developers and any members of the class
    respectively for debugging purposes. In addition, the method `__to_dict__`
    can be used to replace schema design with a function call. However,
    this will always return all the columns for any particular table,
    and proper care has to be maintained if anything else is required.
    """


    def __repr__(self):
        # can be used by developers - for debugging
        # recomended to update the `repr(NewTableView)` as required
        return f"{self.__name__} | Columns: {self.__table__.columns}"

    def __str__(self):
        # can be used by anyone to understand the class
        # recomended to update the `str(NewTableView)` as required
        return f"Model Class: {self.__name__}"

    def __to_dict__(self):
        return { c.key : getattr(self, c.key) for c in self.__table__.columns }
