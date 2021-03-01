from .mysqlcm import UseDataBase


class DbApiTeller:
    """
    Creates simple database queries using the context manager.
    """

    def __init__(self, config: dict,
                        user_id: int,
                        fields: list,
                        table_name: str='tasks') -> None:
        """
        Accepts DB configuration, user ID and data fields.
        """
        self.configuration = config
        self.user_id = user_id
        self.fields = fields
        self.table_name = table_name

    def get_data(self, task_id: int=0) -> dict:
        """
        Retrieves all data from the database or a single record
        """
        if not task_id:
            with UseDataBase(self.configuration) as cursor:
                _SQL = f"""
                        SELECT {', '.join(self.fields)}
                        FROM {self.table_name}
                        WHERE user_id = {self.user_id}"""
                cursor.execute(_SQL)
                data = cursor.fetchall()
        else:
            with UseDataBase(self.configuration) as cursor:
                _SQL = f"""
                        SELECT {', '.join(self.fields)}
                        FROM {self.table_name}
                        WHERE user_id = {self.user_id}
                        AND task_id = {task_id}"""
                cursor.execute(_SQL)
                data = cursor.fetchall()
        return data

    def post_data(self, values: dict) -> None:
        """
        Creates a new record in the database with the values
        specified in the dictionary.
        """
        with UseDataBase(self.configuration) as cursor:
            fields = sorted(values.keys())
            values_fields = [str(values[key])
                            for key in sorted(values.keys())]
            _SQL = f"""
                    INSERT INTO {self.table_name} ({', '.join(fields)})
                    VALUES
                    ({', '.join([("'" + value + "'")
                                if not value.isdigit()
                                else value
                                for value in values_fields])})

                    """
            #print(_SQL)
            cursor.execute(_SQL)

    def put_data(self, fields: dict) -> None:
        """
        Updates a record in the database by the specified fields.
        """
        with UseDataBase(self.configuration) as cursor:
            fields = sorted(values.keys())
            values_fields = [str(values[key])
                            for key in sorted(values.keys())]
            _SQL = f"""
                    UPDATE {self.table_name}
                    SET field = value, field2 ....
                    WHRER user and task_id

                    """
            #print(_SQL)
            cursor.execute(_SQL)
        

    def del_data(self, record: int) -> dict:
        """
        Deletes a record in the database at the specified number.
        """
        pass
