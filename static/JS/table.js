$(document).ready(function () {
$('#table_db').DataTable( {
    "paging": true,
    "autoWidth": false,
    "ordering": true,
    "lengthMenu": [
        [5, 10, 25, 50, -1],
        [5, 10, 25, 50, 'All'],
    ],
    "columnDefs": [
        {"targets": 0, "width": "10px", },
        {"targets": 1, "width": "350px", "searchable": true, },
        {"targets": 2, "width": "50px", "orderable": false},
        {"targets": 3, "width": "50x", "orderable": false },
        {"targets": 4, "width": "220px", },
    ]
});} );