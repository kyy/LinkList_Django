$(document).ready(function () {
$('#table_db').DataTable( {
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
    ]
});} );