$(document).ready(function () {
  $('#rule_table').DataTable({
    "bPaginate": true,
    "bLengthChange": false,
    "bFilter": true,
    "bInfo": true,
    "bAutoWidth": false,
    "pageLength": 25,
    "pagingType": "full", // "simple" option for 'Previous' and 'Next' buttons only
    "searching": true,
    "columns": [
        { "width": "5%" },
        { "width": "5%" },
        { "width": "5%" },
        { "width": "35%" },
        { "width": "15%" },
        { "width": "15%" },
        { "width": "20%" },
    ]
  });
  $('.dataTables_length').addClass('bs-select');
});