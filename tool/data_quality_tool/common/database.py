import snowflake.connector
from snowflake.connector import DictCursor
import configparser
import hashlib

class Database(object):
    ACCOUNT = 'dropbox'
    SNOW_DATABASE = 'RDE'
    SNOW_SCHEMA = 'audit'
    SNOW_CONNECTION = None

    @staticmethod
    def initialize():
        config = configparser.ConfigParser()
        config.read('config/config.ini')
        snow_user = config['snowflake']['user']
        snow_pass = config['snowflake']['pass']

        Database.SNOW_CONNECTION = snowflake.connector.connect(
                                    user=snow_user,
                                    password=snow_pass,
                                    account=Database.ACCOUNT
                                    )

    @staticmethod
    def check_db_token_expired():
        try:
            cur = Database.SNOW_CONNECTION.cursor()
            cur.execute('SELECT 1 FROM DUAL')
        except snowflake.connector.errors.ProgrammingError as ex:
            Database.initialize()
        finally:
            cur.close()

    @staticmethod
    def insert(table_name, data):
        Database.check_db_token_expired()

        format_str = {'snow_database': Database.SNOW_DATABASE,
                      'snow_schema': Database.SNOW_SCHEMA,
                      'snow_table': table_name,
                      'data': data
                      }

        insert_sql = "INSERT INTO {snow_database}.{snow_schema}.{snow_table} {data}".format(**format_str)

        print('insert_sql: ' + insert_sql)
        cur = Database.SNOW_CONNECTION.cursor()
        try:
            cur.execute(insert_sql)
        except Exception as ex:
            err_msg = str(ex)
            return err_msg
        finally:
            cur.close()

        return 'Success'

    @staticmethod
    def update(table_name, key_field, data_field):
        Database.check_db_token_expired()

        format_str = {'snow_database': Database.SNOW_DATABASE,
                      'snow_schema': Database.SNOW_SCHEMA,
                      'table_name': table_name,
                      'key_field': key_field,
                      'data_field': data_field
                      }
        update_sql = 'UPDATE {snow_database}.{snow_schema}.{table_name} SET {data_field} WHERE {key_field}'.format(**format_str)

        print('update_sql: ' + update_sql)
        cur = Database.SNOW_CONNECTION.cursor()
        try:
            cur.execute(update_sql)
        except Exception as ex:
            err_msg = str(ex)
            return err_msg
        finally:
            cur.close()

        return 'Success'

    @staticmethod
    def delete(table_name, key_field):
        Database.check_db_token_expired()

        format_str = {'snow_database': Database.SNOW_DATABASE,
                      'snow_schema': Database.SNOW_SCHEMA,
                      'table_name': table_name,
                      'key_field': key_field
                      }

        delete_sql = 'DELETE FROM {snow_database}.{snow_schema}.{table_name} WHERE {key_field}'.format(**format_str)

        cur = Database.SNOW_CONNECTION.cursor()
        try:
            cur.execute(delete_sql)
        except Exception as ex:
            err_msg = str(ex)
            return err_msg
        finally:
            cur.close()

        return 'Success'

    @staticmethod
    def fetch_all(table_name):
        Database.check_db_token_expired()

        format_str = {'snow_database': Database.SNOW_DATABASE,
                      'snow_schema': Database.SNOW_SCHEMA,
                      'snow_table': table_name
                      }

        fetch_all_sql = "SELECT * FROM {snow_database}.{snow_schema}.{snow_table} ORDER BY PROCESS_TS DESC".format(**format_str)

        print('fetch_all_sql: ' + fetch_all_sql)
        cur = Database.SNOW_CONNECTION.cursor(DictCursor)
        try:
            cur.execute(fetch_all_sql)
            result = cur.fetchall()
        finally:
            cur.close()

        return result

    @staticmethod
    def fetch_one(table_name, query):
        Database.check_db_token_expired()

        format_str = {'snow_database': Database.SNOW_DATABASE,
                      'snow_schema': Database.SNOW_SCHEMA,
                      'snow_table': table_name,
                      'query': query
                      }

        fetch_one_sql = "SELECT * FROM {snow_database}.{snow_schema}.{snow_table} WHERE {query}".format(**format_str)

        print('fetch_one_sql: ' + fetch_one_sql)
        cur = Database.SNOW_CONNECTION.cursor(DictCursor)
        try:
            cur.execute(fetch_one_sql)
            result = cur.fetchall()
        finally:
            cur.close()

        return result

    @staticmethod
    def validate_sql(query):
        Database.check_db_token_expired()

        cur = Database.SNOW_CONNECTION.cursor(DictCursor)
        try:
            query_md5 = hashlib.md5(query).hexdigest()
            stmt = "CREATE OR REPLACE VIEW AUDIT.VALIDATE_{}  AS ".format(query_md5)
            print('validate sql:' + stmt + query)
            cur.execute(stmt + query)
            cur.execute("DROP VIEW AUDIT.VALIDATE_{}".format(query_md5))
            # result = cur.fetchall()
        except Exception as ex:
            # print('In the exception block')
            err_msg = str(ex)
            return 'Invalid SQL: ' + err_msg
        finally:
            cur.close()

        # if len(result) > 1:
        #    return 'Invalid SQL: Query returns more than one record'

        return 'Success'


    @staticmethod
    def get_database_name():
        Database.check_db_token_expired()

        cur = Database.SNOW_CONNECTION.cursor(DictCursor)

        try:
            cur.execute('SHOW DATABASES')
            results = cur.fetchall()
        finally:
            cur.close()

        # print(results)
        return [(result['name'], result['name']) for result in results]

    @staticmethod
    def get_schema_name(database_name):
        Database.check_db_token_expired()

        cur = Database.SNOW_CONNECTION.cursor(DictCursor)

        try:
            cur.execute('USE {}'.format(database_name))
            cur.execute('SHOW SCHEMAS')
            results = cur.fetchall()
        finally:
            cur.close()

        # print(results)
        return [(result['name'], result['name']) for result in results if result['database_name'] == database_name]

    @staticmethod
    def get_table_name(schema_name):
        Database.check_db_token_expired()

        cur = Database.SNOW_CONNECTION.cursor(DictCursor)
        table_views = []
        try:
            cur.execute('SHOW TABLES')
            table_results = cur.fetchall()

            cur.execute('SHOW VIEWS')
            view_results = cur.fetchall()

        finally:
            cur.close()

        for result in table_results:
            if result['schema_name'] == schema_name:
                table_views.append((result['name'], result['name']))

        for result in view_results:
            if result['schema_name'] == schema_name:
                table_views.append((result['name'], result['name']))

        return table_views

    @staticmethod
    def execute_query(query):
        Database.check_db_token_expired()

        cur = Database.SNOW_CONNECTION.cursor(DictCursor)

        try:
            cur.execute(query)
            result = cur.fetchall()
        except Exception as ex:
            raise ex
            err_msg = str(ex)
            return 'Error: ' + err_msg
        finally:
            cur.close()

        return result
