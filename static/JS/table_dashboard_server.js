
$(document).ready(function() {
    var dt_table = $('.table').dataTable({
        ajax: DASHBOARD_SERVER_JSON_URL,
        searching: true,
        processing: true,
        serverSide: true,
        stateSave: true,
        language: dt_language,  // global variable defined in html
        order: [[ 0, "desc" ]],
        lengthMenu: [[5, 10, 20, -1], [5, 10, 20, 'all']],
        columns: [
            {data: 'name', orderable: true, searchable: true, className: "center"},
            {data: 'name', orderable: true, searchable: true, className: "center"},
            {data: 'data', orderable: true, searchable: true, className: "center"},
            {data: 'data', orderable: true, searchable: true, className: "center"},
        ],
    });
});