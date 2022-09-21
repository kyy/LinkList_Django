$(document).ready(function () {
$('#table_db').DataTable( {
    // "processing": true,   https://pypi.org/project/django-serverside-datatable/
    // "serverSide": true,   pip install django-serverside-datatable
    "paging": true,
    "autoWidth": false,
    "searching": true,
    "ordering": true,
    "lengthMenu": [
        [5, 10, 25, 50, -1],
        [5, 10, 25, 50, 'All'],
    ],
    "columnDefs": [
        {"targets": 0, "width": "10px", "searchable": false, },
        {"targets": 1, "width": "350px", },
        {"targets": 2, "width": "50px", "searchable": false, "orderable": false},
        {"targets": 3, "width": "50x", "searchable": false, "orderable": false },
        {"targets": 4, "width": "220px", "searchable": false, },
    ],
    "language": {
        "decimal":        "",
        "emptyTable":     "No data available in table",
        "info":           "Showing _START_ to _END_ of _TOTAL_ entries",
        "infoEmpty":      "Showing 0 to 0 of 0 entries",
        "infoFiltered":   "(filtered from _MAX_ total entries)",
        "infoPostFix":    "",
        "thousands":      ",",
        "lengthMenu":     "Show _MENU_ entries",
        "loadingRecords": "Loading...",
        "processing":     "",
        "search":         "Search:",
        "zeroRecords":    "No matching records found",
        "paginate": {
            "first":      "First",
            "last":       "Last",
            "next":       "Next",
            "previous":   "Previous"
        },
        "aria": {
            "sortAscending":  ": activate to sort column ascending",
            "sortDescending": ": activate to sort column descending"
        }
    }



});} );