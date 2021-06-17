from flask import Flask, render_template, redirect, url_for,flash, request, jsonify, make_response
from flask_wtf import FlaskForm
from wtforms import (StringField, IntegerField, SelectField, TextAreaField,SubmitField, HiddenField)
from wtforms.validators import DataRequired, Length
from models.data_rule import DataRule
from common.database import Database
import configparser

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config/config.ini')
app.config['SECRET_KEY'] = config['secret_key']['key']


class InfoForm(FlaskForm):
    """
    Mainly a way to go through many of the WTForms Fields.
    """
    Database.initialize()

    data_rule_id = HiddenField('Data rule ID: ')

    data_rule_name = StringField('Data rule name: ', validators=[DataRequired('Please enter a valid data rule name!')])

    database_type = SelectField(u'Database Type: ',
                                choices=[('Snowflake', 'Snowflake')], default="Snowflake")

    database_name = SelectField(u'Database name: ',
                                choices=Database.get_database_name(), default="RDE")

    schema_name = SelectField(u'Schema name: ',
                              choices=Database.get_schema_name("RDE"), default="CX")

    table_name = SelectField(u'table name: ',
                             choices=Database.get_table_name("CX"))

    rule_type = SelectField(u'Data Rule Type',
                            choices=[('Duplicate key check', 'Duplicate key check'),
                                     ('Delay in table refresh', 'Delay in table refresh'),
                                     ('Missing records in a period', 'Missing records in a period'),
                                     ('Metric value check', 'Metric value check'),
                                     ('Metric anomaly detection', 'Metric anomaly detection'),
                                     ('Other custom Validations', 'Other custom Validation')],
                            default='Duplicate key check')

    validation_query = TextAreaField('Validation Query', validators=[DataRequired()])

    comparison = SelectField(u'Priority',
                             choices=[('Greater than', 'Greater than'),
                                      ('Less than', 'Less than'), ('Equals', 'Equals'),
                                      ('Greater than or equals', 'Greater than or equals'),
                                      ('Less than or equals', 'Less than or equals') ],
                             default='Greater than')

    threshold = IntegerField('Enter the threshold value', validators=[DataRequired()], default="0")

    sla_time_window = SelectField(u'Enter the time window value',
                                  choices=[('1', '1'),
                                           ('2', '2'),
                                           ('3', '3'),
                                           ('4', '4'),
                                           ('5', '5'),
                                           ('6', '6'),
                                           ('7', '7'),
                                           ('8', '8'),
                                           ('9', '9'),
                                           ('10', '10'),
                                           ('11', '11'),
                                           ('12', '12'),
                                           ('13', '13'),
                                           ('14', '14'),
                                           ('15', '15'),
                                           ('16', '16'),
                                           ('17', '17'),
                                           ('18', '18'),
                                           ('19', '19'),
                                           ('20', '20'),
                                           ('21', '21'),
                                           ('22', '22'),
                                           ('23', '23')], default='10')

    dri_email = StringField('DRI Email id', [
        Length(min=4, message=u'Little short for an email address?'),
        DataRequired(message='That\'s not a valid email address.')
    ], default='revenue_data_engineering')

    notification_email = StringField('Notification Email id', [
        Length(min=4, message=u'Little short for an email address?'),
        DataRequired(message='That\'s not a valid email address.')
    ])

    slack_channel = SelectField(u'Slack Channel: ',
                                choices=[('None', 'None'), ('#frostitron', '#frostitron')], default="None")

    notification_message = TextAreaField('Enter notification_message', validators=[DataRequired()])

    priority = SelectField(u'Priority',
                          choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')],
                          default='Low')

    active = SelectField(u'Active',
                          choices=[('Yes', 'Yes'), ('No', 'No')],
                          default='Yes')

    backfill_data = SelectField(u'Backfill data',
                                choices=[('Yes', 'Yes'), ('No', 'No')],
                                default='No')

    backfill_query = TextAreaField('Backfill Query')

    submit = SubmitField('Submit')


def get_pp_nonce():
    # Returns the nonce code from HTTP header.
    return request.headers.get("X-PP-CSP-Nonce") or "c06f140377bd4706b69c04bb42e66173"


@app.route('/')
def index():
    return render_template('index.html', PP_NONCE=get_pp_nonce())


@app.before_first_request
def initialize_database():
    Database.initialize()


@app.route('/schema_name/<string:database_name>', methods=['GET'])
def schema_name(database_name):
    schemas = Database.get_schema_name(database_name)
    schema_list = []

    for schema in schemas:
        schema_dict = {'id': schema[0], 'name': schema[1]}
        schema_list.append(schema_dict)

    return jsonify({'schemas': schema_list})


@app.route('/table_name/<string:schema_name>', methods=['GET'])
def table_name(schema_name):
    tables = Database.get_table_name(schema_name)
    table_list = []

    for table in tables:
        table_dict = {'id': table[0], 'name': table[1]}
        table_list.append(table_dict)

    return jsonify({'tables': table_list})


@app.route('/delete_dq/<int:data_rule_id>', methods=['GET', 'POST'])
def delete_dq(data_rule_id=None):
    if data_rule_id:
        db_status = DataRule.delete(data_rule_id)

        if db_status != 'Success':
            flash("Errors Found -  " + db_status)
        else:
            flash("Data Quality Rule deleted !!")

    return redirect(url_for("dq_rules"))


@app.route('/plot_data/<int:data_rule_id>', methods=['GET', 'POST'])
def get_plot_data(data_rule_id=None):
    plot_data = DataRule.get_plot_data(data_rule_id)
    return jsonify({'plot': plot_data})


@app.route('/new_dq', methods=['GET', 'POST'])
@app.route('/new_dq/<int:data_rule_id>', methods=['GET', 'POST'])
def new_dq(data_rule_id=None):
    form = InfoForm()

    if request.method == 'GET':
        if data_rule_id:
            rule = DataRule.get_rule_by_id(data_rule_id)[0]
            notify_email_formatted = ','.join([email.split('@')[0] for email in rule.email_notify.split(',')])
            dri_email_formatted = ','.join([email.split('@')[0] for email in rule.dri_email.split(',')])

            form.data_rule_name.data = rule.data_rule_name
            form.rule_type.data = rule.data_rule_type
            form.database_type.data = rule.database_type
            form.database_name.data = rule.database_name
            form.schema_name.data = rule.schema_name
            form.table_name.data = rule.table_name
            form.comparison.data = rule.comparison
            form.threshold.data = rule.threshold
            form.validation_query.data = rule.validation_sql
            form.notification_message.data = rule.validation_message
            form.sla_time_window.data = rule.sla_period
            form.priority.data = rule.priority
            form.dri_email.data = dri_email_formatted
            form.notification_email.data = notify_email_formatted
            form.slack_channel.data = rule.slack_channel
            form.backfill_data.data = rule.backfill_data
            form.backfill_query.data = rule.backfill_query
            form.active.data = rule.active
            form.data_rule_id.data = rule.data_rule_id

            form.rule_type.choices = [(rule.data_rule_type, rule.data_rule_type)]
            form.database_name.choices = [(rule.database_name, rule.database_name)]
            form.database_type.choices = [(rule.database_type, rule.database_type)]
            form.schema_name.choices = [(rule.schema_name, rule.schema_name)]
            form.table_name.choices = [(rule.table_name, rule.table_name)]

        return render_template('new_dq.html', form=form, PP_NONCE=get_pp_nonce())
    elif request.method == "POST":

        if data_rule_id:
            notify_email_formatted = ','.join([email + '@dropbox.com' for email in form.notification_email.data.split(',')])
            dri_email_formatted = ','.join([email + '@dropbox.com' for email in form.dri_email.data.split(',')])
            update_rule = DataRule(data_rule_name=form.data_rule_name.data,
                                   data_rule_type=form.rule_type.data,
                                   database_type=form.database_type.data,
                                   database_name=form.database_name.data,
                                   schema_name=form.schema_name.data,
                                   table_name=form.table_name.data,
                                   comparison=form.comparison.data,
                                   threshold=form.threshold.data,
                                   validation_sql=form.validation_query.data,
                                   validation_message=form.notification_message.data,
                                   sla_period=form.sla_time_window.data,
                                   priority=form.priority.data,
                                   dri_email=dri_email_formatted,
                                   email_notify=notify_email_formatted,
                                   slack_channel=form.slack_channel.data,
                                   backfill_data=form.backfill_data.data,
                                   backfill_query=form.backfill_query.data,
                                   active=form.active.data,
                                   data_rule_id=data_rule_id)

            validate_sql = Database.validate_sql(form.validation_query.data)

            if validate_sql != 'Success':
                flash("Errors Found -  " + validate_sql)
                return render_template('new_dq.html', form=form, PP_NONCE=get_pp_nonce())
            else:
                db_status = update_rule.update_db()

                if db_status != 'Success':
                    flash("Errors Found -  " + db_status)
                    return render_template('new_dq.html', form=form, PP_NONCE=get_pp_nonce())
                else:
                    flash("Data Quality Rule Updated !!")

        else:
            notify_email_formatted = ','.join([email + '@dropbox.com' for email in form.notification_email.data.split(',')])
            dri_email_formatted = ','.join([email + '@dropbox.com' for email in form.dri_email.data.split(',')])
            new_rule = DataRule(data_rule_name=form.data_rule_name.data,
                                data_rule_type=form.rule_type.data,
                                database_type=form.database_type.data,
                                database_name=form.database_name.data,
                                schema_name=form.schema_name.data,
                                table_name=form.table_name.data,
                                comparison=form.comparison.data,
                                threshold=form.threshold.data,
                                validation_sql=form.validation_query.data,
                                validation_message=form.notification_message.data,
                                sla_period=form.sla_time_window.data,
                                priority=form.priority.data,
                                dri_email=dri_email_formatted,
                                email_notify=notify_email_formatted,
                                slack_channel=form.slack_channel.data,
                                backfill_data=form.backfill_data.data,
                                backfill_query=form.backfill_query.data,
                                active=form.active.data)

            validate_sql = Database.validate_sql(form.validation_query.data)

            if validate_sql != 'Success':
                flash("Errors Found -  " + validate_sql)
                database_name_err = form.database_name.data
                schema_name_err = form.schema_name.data
                form.schema_name.choices = Database.get_schema_name(database_name_err)
                form.table_name.choices = Database.get_table_name(schema_name_err)
                return render_template('new_dq.html', form=form, PP_NONCE=get_pp_nonce())
            else:
                db_status = new_rule.save_to_db()
                if db_status != 'Success':
                    flash("Errors Found -  " + db_status)
                    database_name_err = form.database_name.data
                    schema_name_err = form.schema_name.data
                    form.schema_name.choices = Database.get_schema_name(database_name_err)
                    form.table_name.choices = Database.get_table_name(schema_name_err)
                    return render_template('new_dq.html', form=form, PP_NONCE=get_pp_nonce())
                else:
                    flash("Data Quality Rule Submitted !!")

        return redirect(url_for("dq_rules"))


@app.route('/dq_rule_submitted')
def dq_rule_submitted():
    return render_template('dq_entered_succ.html')


@app.route('/dq_rules')
def dq_rules():
    rules = DataRule.get_data_rule_with_status()
    if 'Error:' in rules:
        flash("Errors Found -  " + rules)
    else:
        return render_template('dq_rules.html', rules=rules, PP_NONCE=get_pp_nonce())


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', PP_NONCE=get_pp_nonce())


@app.route('/metric_monitoring')
def metric_monitoring():
    return render_template('metric_monitoring.html', PP_NONCE=get_pp_nonce())


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, port=5020)