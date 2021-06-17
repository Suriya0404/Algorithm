$(document).ready(function($) {
    let database_select = document.getElementById('database_select');
    let schema_select = document.getElementById('schema_select');
    let table_select = document.getElementById('table_select');
    let data_rule_select = document.getElementById('data_rule_select');
    let validation_query_text = document.getElementById('validation_query_text');
    let threshold_text = document.getElementById('threshold_text');
    let notification_message_text = document.getElementById('notification_message_text');
    let backfill_data_text = document.getElementById('backfill_data_text');
    let backfill_query_text = document.getElementById('backfill_query_text');

    if (data_rule_select.value == 'Metric anomaly detection') {
        backfill_data_text.disabled=false;
        backfill_query_text.disabled=false;
    } else {
        backfill_data_text.disabled=true;
        backfill_query_text.disabled=true;
    }

    function set_default_field_values(data_rule_type, database_name, schema_name, table_name)  {
        if (data_rule_type == 'Duplicate key check') {
            validation_query_text.innerHTML =   'SELECT COUNT(*) as col1 \n FROM (SELECT\t<< REPLACE WITH COLUMN NAME >>,\n\t\t COUNT(*) \n\tFROM\t'
                                                + database_name + '.' + schema_name + '.' + table_name +
                                                '\n\tGROUP BY << REPLACE WITH COLUMN NAME >> \n\tHAVING COUNT(*) > 1) AS TEMP';
            threshold_text.value = 0;
            backfill_data_text.value='No';
            backfill_data_text.disabled=true;
            backfill_query_text.disabled=true;
            notification_message_text.innerHTML = 'Duplicate records found in the table - ' + database_name + '.'
                                                  + schema_name + '.' + table_name + ' for the key fields << REPLACE WITH COLUMN NAMES >>';
        } else if (data_rule_type == 'Delay in table refresh') {
            validation_query_text.innerHTML =   'SELECT  DATEDIFF("day", MAX(<< REPLACE WITH DATE FIELD >>), current_date) as col1, ' +
                                                '\n\tMAX(<< REPLACE WITH DATE FIELD >>) as col2' +
                                                '\nFROM\t' + database_name + '.' + schema_name + '.' + table_name;
            threshold_text.value = 3;
            backfill_data_text.value='No';
            backfill_data_text.disabled=true;
            backfill_query_text.disabled=true;
            notification_message_text.innerHTML = 'Table ' + schema_name + '.' + table_name + ' has been delayed for {col1} days. The latest available data is on {col2}.';
        } else if (data_rule_type == 'Missing records in a period') {
            validation_query_text.innerHTML = 'SELECT  COUNT(DISTINCT << REPLACE WITH DATE FIELD >>) as col1, ' +
                                              '\n\tCURRENT_DATE() as col2, ' +
                                              '\n\tCURRENT_DATE() - 10 as col3 ' +
                                              '\nFROM\t' + database_name + '.' + schema_name + '.' + table_name +
                                              '\nWHERE\t<< REPLACE WITH DATE FIELD >> BETWEEN CURRENT_DATE() AND CURRENT_DATE() - 10';
            threshold_text.value = 10;
            backfill_data_text.value='No';
            backfill_data_text.disabled=true;
            backfill_query_text.disabled=true;
            notification_message_text.innerHTML = 'There are missing data in the table - ' +
                                                  database_name + '.' + schema_name + '.' + table_name + ' for the days between {col2} and {col3}.';
        } else if (data_rule_type == 'Metric value check') {

            validation_query_text.innerHTML = 'SELECT  SUM(<< REPLACE WITH METRIC NAME>>) as col1, ' +
                                              '\n\tCURRENT_DATE() as col2, ' +
                                              '\n\tCURRENT_DATE() - 10 as col3, ' +
                                              "\n\t'<< REPLACE WITH METRIC NAME >>' as col4 " +
                                              '\nFROM\t' + database_name + '.' + schema_name + '.' + table_name +
                                              '\nWHERE\t<< REPLACE WITH DATE FIELD >> BETWEEN CURRENT_DATE() AND CURRENT_DATE() - 10';
            threshold_text.value = 1000;
            backfill_data_text.value='No';
            backfill_data_text.disabled=true;
            backfill_query_text.disabled=true;
            notification_message_text.innerHTML = 'The {col4} for the period between {col3} and {col2} is {col1} cross the set threshold of {threshold}.';

        } else if (data_rule_type == 'Metric anomaly detection') {
            validation_query_text.innerHTML = 'SELECT  SUM(<< REPLACE WITH METRIC NAME>>) as col1, ' +
                                              '\n\tCURRENT_DATE() as col2, ' +
                                              '\n\tCURRENT_DATE() - 1 as col3, ' +
                                              "\n\t'<< REPLACE WITH METRIC NAME >>' as col4 " +
                                              '\nFROM\t' + database_name + '.' + schema_name + '.' + table_name +
                                              '\nWHERE\t<< REPLACE WITH DATE FIELD >> BETWEEN CURRENT_DATE() - 1  AND CURRENT_DATE()';
            threshold_text.value = 10;
            backfill_data_text.value='Yes';
            backfill_data_text.disabled=false;
            backfill_query_text.disabled=false;
            notification_message_text.innerHTML = 'Anomaly detected for the metric - {col4} for the period {col3} and {col2}.';

            backfill_query_text.innerHTML = 'SELECT  to_date(<< REPLACE WITH DATE FIELD >>) as col1, ' +
                                            '\n\tSUM(<< REPLACE WITH METRIC NAME>>) as col2 ' +
                                            '\nFROM\t' + database_name + '.' + schema_name + '.' + table_name +
                                            '\nWHERE << REPLACE WITH DATE FIELD >> BETWEEN CURRENT_DATE() - 360 AND CURRENT_DATE() ' +
                                            '\nGROUP BY to_date(<< REPLACE WITH DATE FIELD >>) ';

       } else if (data_rule_type == 'Metric trend monitoring') {
            validation_query_text.innerHTML = 'SELECT  SUM(<< REPLACE WITH METRIC NAME>>) as col1, ' +
                                              '\n\tCURRENT_DATE() as col2, ' +
                                              '\n\tCURRENT_DATE() - 1 as col3, ' +
                                              "\n\t'<< REPLACE WITH METRIC NAME >>' as col4 " +
                                              '\nFROM\t' + database_name + '.' + schema_name + '.' + table_name +
                                              '\nWHERE\t<< REPLACE WITH DATE FIELD >> BETWEEN CURRENT_DATE() - 1 AND CURRENT_DATE()';
            threshold_text.value = 10;
            backfill_data_text.value='Yes';
            backfill_data_text.disabled=false;
            backfill_query_text.disabled=false;
            notification_message_text.innerHTML = 'There is a change in trend in the metric - {col4} for the period {col3} and {col2}.';
        } else if (data_rule_type == 'Other custom Validations') {
            validation_query_text.innerHTML = '';
            threshold_text.value = 10;
            notification_message_text.innerHTML = '';
            backfill_data_text.disabled=true;
            backfill_query_text.disabled=true;
       };

    }

    data_rule_select.addEventListener("change", function(){
        let data_rule_type = data_rule_select.value;
        let database_name = database_select.value;
        let schema_name = schema_select.value;
        let table_name = table_select.value;

        set_default_field_values(data_rule_type, database_name, schema_name, table_name);
    });

    database_select.addEventListener("change", function(){
        let database_name = database_select.value;
        let first_schema = '';
        let first_table = '';

        fetch('/schema_name/' + database_name).then(function(response) {
            response.json().then(function(data) {
                let optionHTML = '';
                for (let schema of data.schemas) {
                    if (first_schema == '') {
                      first_schema = schema.name;
                    };

                    optionHTML += '<option value = "' + schema.id + '"> ' + schema.name + '</option>';

                    console.log(first_schema)
                }
                schema_select.innerHTML = optionHTML;

                fetch('/table_name/' + first_schema).then(function(response) {
                    response.json().then(function(data) {
                        let optionHTML = '';

                        for (let table of data.tables) {
                            if (first_table == '') {
                                first_table = table.name
                            }


                            optionHTML += '<option value = "' + table.id + '"> ' + table.name + '</option>';
                        }
                        table_select.innerHTML = optionHTML;

                        let data_rule_type = data_rule_select.value;

                        console.log('schema name:' + first_schema);
                        console.log('Table name:' + first_table);
                        set_default_field_values(data_rule_type, database_name, first_schema, first_table);

                    });
                });
            });
        });
   });


    schema_select.addEventListener("change", function(){
        let schema_name = schema_select.value;
        let first_table = ''

        fetch('/table_name/' + schema_name).then(function(response) {
            response.json().then(function(data) {
                let optionHTML = '';
                for (let table of data.tables) {
                    if (first_table == '') {
                        first_table = table.name;
                    };


                    optionHTML += '<option value = "' + table.id + '"> ' + table.name + '</option>';
                }
                table_select.innerHTML = optionHTML;

                let data_rule_type = data_rule_select.value;
                let database_name = database_select.value;

                set_default_field_values(data_rule_type, database_name, schema_name, first_table);
            });
        });
    });

    table_select.addEventListener("change", function(){
        let data_rule_type = data_rule_select.value;
        let database_name = database_select.value;
        let schema_name = schema_select.value;
        let table_name = table_select.value;

        set_default_field_values(data_rule_type, database_name, schema_name, table_name);
    });


    let form = document.querySelector('form')

    form.addEventListener('submit', function(event) {
        let has_error = false;
        let email_notify_text = document.getElementById('email_notify_text');
        let email_feedback = document.getElementById('email_feedback');
        let email_notify = email_notify_text.value;

        if (email_notify.length > 0 && email_notify.includes('@')) {
            has_error = true;
            email_notify_text.className = "form-control is-invalid";
            email_feedback.textContent = '@dropbox.com is included by default. Please dont include @ in notification email';
        } else if (email_notify.length == 0) {
            has_error = true;
            email_notify_text.className = "form-control is-invalid";
            email_feedback.textContent = 'Please enter a notification email address';
        } else {
            email_notify_text.className = "form-control";
            email_feedback.textContent = 'Please enter a notification email address';
        }

        let threshold_text = document.getElementById('threshold_text');
        let threshold_feedback = document.getElementById('threshold_feedback');

        let threshold = threshold_text.value;

        if (threshold.length > 0 && isNaN(parseInt(threshold))) {
            has_error = true;
            threshold_text.className = "form-control is-invalid";
            threshold_feedback.textContent = 'Please enter a valid threshold.';
        } else if (threshold.length == 0) {
            has_error = true;
            threshold_text.className = "form-control is-invalid";
            threshold_feedback.textContent = 'Please enter a valid threshold';
        } else {
            threshold_text.className = "form-control";
            threshold_feedback.textContent = 'Please enter a valid threshold';
        }

        let notification_message_text = document.getElementById('notification_message_text');
        let notification_message_feedback = document.getElementById('notification_message_feedback');
        let notification_message = notification_message_text.value;

        if (notification_message.includes('<< REPLACE')) {
            has_error = true;
            notification_message_text.className = "form-control is-invalid";
            notification_message_feedback.textContent = "Please input column names in the replace tag";
        } else {
            notification_message_text.className = "form-control";
            notification_message_feedback.textContent = "Please enter the validation message";
        }

        let validation_query_text = document.getElementById('validation_query_text');
        let validation_query_feedback = document.getElementById('validation_query_feedback');
        let validation_query = validation_query_text.value;

        if (validation_query.includes('<< REPLACE')) {
            has_error = true;
            validation_query_text.className = "form-control is-invalid";
            validation_query_feedback.textContent = "Please input column names in the replace tag";
        } else {
            validation_query_text.className = "form-control";
            validation_query_feedback.textContent = "Please enter the validation query";
        }

        if (has_error === true || form.checkValidity() === false) {
            event.preventDefault();
            event.stopPropagation();
        }

        form.classList.add('was-validated');
    });

});
