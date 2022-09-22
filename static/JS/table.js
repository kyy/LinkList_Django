function format(d) {
    console.log(d);
    var html ='<table class="table">';
    html+= '<thead>';
    html+= '<tr><th scope="col">Ссылки</th>';
    html+= '<th scope="col">Описание</th>';
    html+= '</thead>';
    html+= '<tbody>';
    html+= '<tr>';
    html+= '<td>'+d[2]+'</td>';
    html+= '<td>'+d[5]+'</td>';
    html+= '</tr>';
    html+= '</tbody>';
    return html;


}


$(document).ready(function () {
    var table = $('#table_db').DataTable( {
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
        {"targets": 0, "width": "10px", "searchable": false, "orderable": false, "className": 'dt-control', "data": null, "defaultContent": '',  },
        {"targets": 1, "width": "10px", "searchable": false, },
        {"targets": 2, "width": "350px", },
        {"targets": 3, "width": "50px", "searchable": false, "orderable": false, },
        {"targets": 4, "width": "50x", "searchable": false, "orderable": false, },
        {"targets": 5, "width": "50px", "searchable": false, },
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



});
// Add event listener for opening and closing details
    $('#table_db tbody').on('click', 'td.dt-control', function () {
        var tr = $(this).closest('tr');
        var row = table.row(tr);

        if (row.child.isShown()) {
            // This row is already open - close it
            row.child.hide();
            tr.removeClass('shown');
        } else {
            // Open this row
            row.child(format(row.data())).show();
            tr.addClass('shown');
        }
    });
});

/* Formatting function for row details - modify as you need */
