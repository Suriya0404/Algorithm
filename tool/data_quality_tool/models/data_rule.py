from common.database import Database
from datetime import datetime


class DataRule(object):
    def __init__(self,
                 data_rule_name,
                 data_rule_type,
                 database_type,
                 database_name,
                 schema_name,
                 table_name,
                 comparison='>',
                 threshold=0,
                 validation_sql=None,
                 validation_message=None,
                 sla_period=None,
                 priority='Low',
                 dri_email=None,
                 email_notify=None,
                 slack_channel=None,
                 backfill_data='No',
                 backfill_query=None,
                 active='Yes',
                 data_rule_id=None
                 ):
        self.database_type = database_type
        self.database_name = database_name
        self.schema_name = schema_name
        self.table_name = table_name
        self.data_rule_name = data_rule_name
        self.data_rule_type = data_rule_type
        self.comparison = comparison
        self.threshold = threshold
        self.validation_sql = validation_sql
        self.validation_message = validation_message
        self.sla_period = sla_period
        self.priority = priority
        self.dri_email = dri_email
        self.email_notify = email_notify
        self.slack_channel = slack_channel
        self.backfill_data = backfill_data
        self.backfill_query = backfill_query
        self.active = active
        self.data_rule_id = data_rule_id

    @classmethod
    def get_rule_by_id(cls, data_rule_id):
        records = Database.fetch_one(table_name="data_rule", query="data_rule_id = '{}'".format(data_rule_id))

        return [cls(record['DATA_RULE_NAME'],
                    record['DATA_RULE_TYPE'],
                    record['DATABASE_TYPE'],
                    record['DATABASE_NAME'],
                    record['SCHEMA_NAME'],
                    record['TABLE_NAME'],
                    record['COMPARISON'],
                    record['THRESHOLD'],
                    record['VALIDATION_SQL'],
                    record['VALIDATION_MESSAGE'],
                    record['SLA_PERIOD'],
                    record['PRIORITY'],
                    record['DRI_EMAIL'],
                    record['EMAIL_NOTIFY'],
                    record['SLACK_CHANNEL'],
                    record['BACKFILL_DATA'],
                    record['BACKFILL_QUERY'],
                    record['ACTIVE'],
                    record['DATA_RULE_ID']) for record in records]

    @classmethod
    def get_all_rules(cls):
        records = Database.fetch_all(table_name="data_rule")

        return [cls(record['DATA_RULE_NAME'],
                    record['DATA_RULE_TYPE'],
                    record['DATABASE_TYPE'],
                    record['DATABASE_NAME'],
                    record['SCHEMA_NAME'],
                    record['TABLE_NAME'],
                    record['COMPARISON'],
                    record['THRESHOLD'],
                    record['VALIDATION_SQL'],
                    record['VALIDATION_MESSAGE'],
                    record['SLA_PERIOD'],
                    record['PRIORITY'],
                    record['DRI_EMAIL'],
                    record['EMAIL_NOTIFY'],
                    record['SLACK_CHANNEL'],
                    record['BACKFILL_DATA'],
                    record['BACKFILL_QUERY'],
                    record['ACTIVE'],
                    record['DATA_RULE_ID']) for record in records]

    def save_to_db(self):
        return Database.insert('data_rule', self.format_data())

    def update_db(self):
        return Database.update('data_rule', 'data_rule_id={}'.format(self.data_rule_id), self.format_data('UPDATE'))

    def format_data(self, trans='INSERT'):
        format_str = {'database_type': self.database_type,
                      'database_name': self.database_name,
                      'schema_name': self.schema_name,
                      'table_name': self.table_name,
                      'data_rule_name': self.data_rule_name,
                      'data_rule_type': self.data_rule_type,
                      'comparison': self.comparison,
                      'threshold': self.threshold,
                      'validation_sql': self.validation_sql.replace("'", "''"),
                      'validation_message': self.validation_message.replace("'", "''"),
                      'sla_period': self.sla_period,
                      'priority': self.priority,
                      'dri_email': self.dri_email,
                      'email_notify': self.email_notify,
                      'slack_channel': self.slack_channel,
                      'backfill_data': self.backfill_data,
                      'backfill_query': self.backfill_query,
                      'active': self.active,
                      'process_ts': str(datetime.now())
                      }

        if trans == 'INSERT':
            return (""" (data_rule_name,
                        data_rule_type,
                        database_type,
                        database_name,
                        schema_name,
                        table_name,
                        comparison,
                        threshold,
                        validation_sql,
                        validation_message,
                        sla_period,
                        priority,
                        dri_email,
                        email_notify,
                        slack_channel,
                        backfill_data,
                        backfill_query,
                        active,
                        process_ts) VALUES (
                        '{data_rule_name}',
                        '{data_rule_type}',
                        '{database_type}',
                        '{database_name}',
                        '{schema_name}',
                        '{table_name}',
                        '{comparison}',
                         {threshold},
                        '{validation_sql}',
                        '{validation_message}',
                        '{sla_period}',
                        '{priority}',
                        '{dri_email}',
                        '{email_notify}',
                        '{slack_channel}',
                        '{backfill_data}',
                        '{backfill_query}',
                        '{active}',
                        '{process_ts}')
                        """.format(**format_str))
        elif trans == 'UPDATE':
            return (""" data_rule_name = '{data_rule_name}',
                        data_rule_type = '{data_rule_type}',
                        database_type = '{database_type}',
                        database_name = '{database_name}',
                        schema_name = '{schema_name}',
                        table_name = '{table_name}',
                        comparison =  '{comparison}',
                        threshold =  {threshold},
                        validation_sql = '{validation_sql}',
                        validation_message = '{validation_message}',
                        sla_period = '{sla_period}',
                        priority = '{priority}',
                        dri_email = '{dri_email}',
                        email_notify = '{email_notify}',
                        slack_channel = '{slack_channel}',
                        backfill_data = '{backfill_data}',
                        backfill_query = '{backfill_query}',
                        active = '{active}',
                        process_ts = '{process_ts}'
                        """.format(**format_str))

    @staticmethod
    def delete(data_rule_id):
        return Database.delete('data_rule', 'data_rule_id={}'.format(data_rule_id))

    @classmethod
    def get_data_rule_with_status(cls):
        dq_rules_with_status = """ SELECT   data_rule_id,
                                            data_rule_name,
                                            data_rule_type,
                                            database_name,
                                            schema_name,
                                            table_name,
                                            email_notify,
                                            Decode(validation_status,
                                                   'Passed', 'static/img/green_ball3.png',
                                                   'Failed', 'static/img/red_ball.png',
                                                   'static/img/yellow_ball4.png') as validation_status
                                    FROM    rde.audit.data_rule rule
                                    LEFT OUTER JOIN
                                    (SELECT validation_status,
                                            rule_id,
                                            ROW_NUMBER() OVER(PARTITION BY rule_id ORDER BY process_ts DESC) row_num
                                    FROM    RDE.AUDIT.DATA_VALIDATION_LOG
                                    ) log
                                    ON rule.data_rule_id = log.rule_id
                                    AND row_num = 1"""

        records = Database.execute_query(dq_rules_with_status)

        if 'Error' in records:
            return records
        else:
            return [{'data_rule_id': record['DATA_RULE_ID'],
                    'data_rule_name': record['DATA_RULE_NAME'],
                    'data_rule_type': record['DATA_RULE_TYPE'],
                    'database_name': record['DATABASE_NAME'],
                    'schema_name': record['SCHEMA_NAME'],
                    'table_name': record['TABLE_NAME'],
                    'email_notify': record['EMAIL_NOTIFY'],
                    'validation_status': record['VALIDATION_STATUS']} for record in records]

    @classmethod
    def get_plot_data(cls, data_rule_id):
        output = []

        plot_data_sql = """ SELECT  to_varchar(report_dt, 'YYYY-MM-DD') as report_dt,
                                    rule_id,
                                    NVL(actual,0) as actual,
                                    NVL(predicted,0) as predicted,
                                    NVL(predicted,0) + NVL(predicted,0) * (threshold/100) as upper_limit,
                                    NVL(predicted,0) - NVL(predicted,0) * (threshold/100) as lower_limit
                            FROM
                            (SELECT report.process_ts as report_dt,
                                    report.rule_id as rule_id,
                                    report.metric_value as actual,
                                    report.predicted_value as predicted,
                                    rule.threshold threshold,
                                    ROW_NUMBER() OVER(PARTITION BY to_date(report.process_ts)
                                                      ORDER BY report.process_ts DESC) as rownum
                            FROM    RDE.AUDIT.DATA_VALIDATION_REPORT_HACK report
                            LEFT OUTER JOIN AUDIT.DATA_RULE rule
                            ON report.rule_id = rule.data_rule_id
                            WHERE   report.rule_id = {0}
                            AND     report.process_ts >= current_date - 30) report
                            WHERE   rownum = 1 ORDER BY report_dt""".format(data_rule_id)

        records = Database.execute_query(plot_data_sql)

        # Set the header
        if len(records) > 0:
            output.append(['report_dt', 'actual', 'predicted', 'upper_limit', 'lower_limit'])

        # Append the data
        for record in records:
            output.append([record['REPORT_DT'],
                           float(record['ACTUAL']),
                           float(record['PREDICTED']),
                           float(record['UPPER_LIMIT']),
                           float(record['LOWER_LIMIT'])])

        return output
