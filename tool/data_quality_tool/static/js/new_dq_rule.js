$(document).ready(function($) {
    let database_select = document.getElementById('database_select');
    let schema_select = document.getElementById('schema_select');
    let table_select = document.getElementById('table_select');
    let data_rule_select = document.getElementById('data_rule_select');
    let validation_query_text = document.getElementById('validation_query_text');
    let threshold_text = document.getElementById('threshold_text');
    let notification_message_text = document.getElementById('notification_message_text');
    let backfill_data_text = document.getElementById('backfill_data_text');


    data_rule_select.onchange = function(){
        let data_rule_type = data_rule_select.value;
        let database_name = database_select.value;
        let schema_name = schema_select.value;
        let table_name = table_select.value;

        if (data_rule_type == 'Duplicate Check') {
            validation_query_text.innerHTML = 'SELECT COUNT(*) \n FROM (SELECT\t<<replace with column names>>,\n\t\t\t\t COUNT(*) \n\t\tFROM\t' + database_name + '.' + schema_name + '.' + table_name + '\n\t\tGROUP BY <<replace with column names>> \n\t\tHAVING COUNT(*) > 1) AS TEMP';
            threshold_text.value = '0';
            threshold_text.disabled = true;
            notification_message_text.innerHTML = 'Duplicate records found in the table - ' + database_name + '.' + schema_name + '.' + table_name + ' for the key fields << REPLACE WITH COLUMN NAMES >>'
        } else if (data_rule_type == 'Metric Monitoring') {
            validation_query_text.innerHTML = 'SELECT SUM(<< REPLACE WITH COLUMN NAME >>) \n FROM\t' + database_name + '.' + schema_name + '.' + table_name + '\nWHERE \t<< REPLACE WITH DATE FIELD CONDITION >>';
            threshold_text.enabled = true;
            threshold_text.value = 5;
            notification_message_text.innerHTML = 'There is more than 5% variance in the metric << REPLACE WITH METRIC NAME >> in the table - ' + database_name + '.' + schema_name + '.' + table_name + '.'
       };
    };

    database_select.onchange = function() {
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

                        if (data_rule_type == 'Duplicate Check') {
                            validation_query_text.innerHTML = 'SELECT COUNT(*) \n FROM (SELECT\t<< REPLACE WITH COLUMN NAMES >>,\n\t\t\t\t COUNT(*) \n\t\tFROM\t' + database_name + '.' + first_schema + '.' + first_table + '\n\t\tGROUP BY << REPLACE WITH COLUMN NAMES >> \n\t\tHAVING COUNT(*) > 1) AS TEMP';
                            notification_message_text.innerHTML = 'Duplicate records found in the table - ' + database_name + '.' + first_schema + '.' + first_table + ' for the key fields << REPLACE WITH COLUMN NAMES >>'
                        } else if (data_rule_type == 'Metric Monitoring') {
                            validation_query_text.innerHTML = 'SELECT SUM(<< REPLACE WITH COLUMN NAME >>) \n FROM\t' + database_name + '.' + first_schema + '.' + first_table + '\nWHERE \t<< REPLACE WITH DATE FIELD CONDITION >>';
                            notification_message_text.innerHTML = 'There is more than 5% variance in the metric << REPLACE WITH METRIC NAME >> in the table - ' + database_name + '.' + first_schema + '.' + first_table + '.'
                        };
                    });
                });
            });
        });
   };


    schema_select.onchange = function() {
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

                if (data_rule_type == 'Duplicate Check') {
                    validation_query_text.innerHTML = 'SELECT COUNT(*) \n FROM (SELECT\t<<replace with column names>>,\n\t\t\t\t COUNT(*) \n\t\tFROM\t' + database_name + '.' + schema_name + '.' + first_table + '\n\t\tGROUP BY <<replace with column names>> \n\t\tHAVING COUNT(*) > 1) AS TEMP';
                    notification_message_text.innerHTML = 'Duplicate records found in the table - ' + database_name + '.' + schema_name + '.' + first_table + ' for the key fields << REPLACE WITH COLUMN NAMES >>'
                } else if (data_rule_type == 'Metric Monitoring') {
                    validation_query_text.innerHTML = 'SELECT SUM(<< REPLACE WITH COLUMN NAME >>) \n FROM\t' + database_name + '.' + schema_name + '.' + first_table + '\nWHERE \t<< REPLACE WITH DATE FIELD CONDITION >>';
                    notification_message_text.innerHTML = 'There is more than 5% variance in the metric << REPLACE WITH METRIC NAME >> in the table - ' + database_name + '.' + schema_name + '.' + first_table + '.'
                };
            });
        });


    };

    table_select.onchange = function() {
        let data_rule_type = data_rule_select.value;
        let database_name = database_select.value;
        let schema_name = schema_select.value;
        let table_name = table_select.value;

        if (data_rule_type == 'Duplicate Check') {
            validation_query_text.innerHTML = 'SELECT COUNT(*) \n FROM (SELECT\t<<REPLACE WITH COLUMN NAMES>>,\n\t\t\t\t COUNT(*) \n\t\tFROM\t' + database_name + '.' + schema_name + '.' + table_name + '\n\t\tGROUP BY << REPLACE WITH COLUMN NAMES >> \n\t\tHAVING COUNT(*) > 1) AS TEMP';
            notification_message_text.innerHTML = 'Duplicate records found in the table - ' + database_name + '.' + schema_name + '.' + table_name + ' for the key fields << REPLACE WITH COLUMN NAMES >>'
        } else if (data_rule_type == 'Metric Monitoring') {
            validation_query_text.innerHTML = 'SELECT SUM(<< REPLACE WITH COLUMN NAME >>) \n FROM\t' + database_name + '.' + schema_name + '.' + table_name + '\nWHERE \t<< REPLACE WITH DATE FIELD CONDITION >>';
            notification_message_text.innerHTML = 'There is more than 5% variance in the metric << REPLACE WITH METRIC NAME >> in the table - ' + database_name + '.' + schema_name + '.' + table_name + '.'
        };
    }


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
            threshold_feedback.textContent = 'Threshold has to be between 0 and 100.';
        } else if (threshold.length > 0 && (parseInt(threshold) < 0 || parseInt(threshold) > 100)) {
            has_error = true;
            threshold_text.className = "form-control is-invalid";
            threshold_feedback.textContent = 'Threshold has to be between 0 and 100.';
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
    })

})
