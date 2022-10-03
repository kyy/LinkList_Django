function format(d) {
    console.log(d);
    var html ='<table class="table">';
    html+= '<thead>';
    html+= '<tr><th scope="col">Записи</th>';
    html+= '</thead>';
    html+= '<tbody>';
    html+= '<tr>';
    html+= '<td>'+ d.URL_long +'</td>';
    html+= '</tr>';
    html+= '</tbody>';
    return html;
}

//
// Pipelining function for DataTables. To be used to the `ajax` option of DataTables
//
$.fn.dataTable.pipeline = function (opts) {
    // Configuration options
    var conf = $.extend(
        {
            pages: 5, // number of pages to cache
            url: '', // script url
            data: null, // function or object with parameters to send to the server
            // matching how `ajax.data` works in DataTables
            method: 'GET', // Ajax HTTP method
        },
        opts
    );

    // Private variables for storing the cache
    var cacheLower = -1;
    var cacheUpper = null;
    var cacheLastRequest = null;
    var cacheLastJson = null;

    return function (request, drawCallback, settings) {
        var ajax = false;
        var requestStart = request.start;
        var drawStart = request.start;
        var requestLength = request.length;
        var requestEnd = requestStart + requestLength;

        if (settings.clearCache) {
            // API requested that the cache be cleared
            ajax = true;
            settings.clearCache = false;
        } else if (cacheLower < 0 || requestStart < cacheLower || requestEnd > cacheUpper) {
            // outside cached data - need to make a request
            ajax = true;
        } else if (
            JSON.stringify(request.order) !== JSON.stringify(cacheLastRequest.order) ||
            JSON.stringify(request.columns) !== JSON.stringify(cacheLastRequest.columns) ||
            JSON.stringify(request.search) !== JSON.stringify(cacheLastRequest.search)
        ) {
            // properties changed (ordering, columns, searching)
            ajax = true;
        }

        // Store the request for checking next time around
        cacheLastRequest = $.extend(true, {}, request);

        if (ajax) {
            // Need data from the server
            if (requestStart < cacheLower) {
                requestStart = requestStart - requestLength * (conf.pages - 1);

                if (requestStart < 0) {
                    requestStart = 0;
                }
            }

            cacheLower = requestStart;
            cacheUpper = requestStart + requestLength * conf.pages;

            request.start = requestStart;
            request.length = requestLength * conf.pages;

            // Provide the same `data` options as DataTables.
            if (typeof conf.data === 'function') {
                // As a function it is executed with the data object as an arg
                // for manipulation. If an object is returned, it is used as the
                // data object to submit
                var d = conf.data(request);
                if (d) {
                    $.extend(request, d);
                }
            } else if ($.isPlainObject(conf.data)) {
                // As an object, the data given extends the default
                $.extend(request, conf.data);
            }

            return $.ajax({
                type: conf.method,
                url: conf.url,
                data: request,
                dataType: 'json',
                cache: false,
                success: function (json) {
                    cacheLastJson = $.extend(true, {}, json);

                    if (cacheLower != drawStart) {
                        json.data.splice(0, drawStart - cacheLower);
                    }
                    if (requestLength >= -1) {
                        json.data.splice(requestLength, json.data.length);
                    }

                    drawCallback(json);
                },
            });
        } else {
            json = $.extend(true, {}, cacheLastJson);
            json.draw = request.draw; // Update the echo for each response
            json.data.splice(0, requestStart - cacheLower);
            json.data.splice(requestLength, json.data.length);

            drawCallback(json);
        }
    };
};

// Register an API method that will empty the pipelined data, forcing an Ajax
// fetch on the next draw (i.e. `table.clearPipeline().draw()`)
$.fn.dataTable.Api.register('clearPipeline()', function () {
    return this.iterator('table', function (settings) {
        settings.clearCache = true;
    });
});

//
// DataTables initialisation
//

$(document).ready(function () {
    var table = $('#table_db').DataTable( {
        serverSide: true,
        ajax: $.fn.dataTable.pipeline({
            url: '/api/urls/?format=datatables',
            pages: 5, // number of pages to cache
            // type: 'POST',
        }),
        select: true,
        order: [[ 1, 'asc' ]],
        responsive: true,
        paging: true,
        autoWidth: false,
        searching: true,
        ordering: true,
        lengthMenu: [
            [5, 10, 25, 50, -1],
            [5, 10, 25, 50, 'All'],
        ],
        columnDefs: [
            {data: null, targets: 0, width: "10px", searchable: false, orderable: false, className: 'dt-control', defaultContent: '', },
            {data: null, targets: 1, width: "10px", searchable: false, defaultContent: ''},
            {data: 'name', targets: 2, width: "550px", },
            {data: null, targets: 3, width: "50px", searchable: false, orderable: false, defaultContent: 'edit'},
            {data: null, targets: 4, width: "50x", searchable: false, orderable: false, defaultContent: 'delete'},
            {data: 'data', targets: 5, width: "50x", searchable: false, },
            {data: 'URL_long', targets: 6, width: "0px", searchable: false, visible: false, },
        ],
        language: dt_language,
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

    // Handle click on "Expand All" button
    $('#btn-show-all-children').on('click', function(){
        // Enumerate all rows
        table.rows().every(function(){
            // If row has details collapsed
            if(!this.child.isShown()){
                // Open this row
                this.child(format(this.data())).show();
                $(this.node()).addClass('shown');
            }
        });
    });

    // Handle click on "Collapse All" button
    $('#btn-hide-all-children').on('click', function(){
        // Enumerate all rows
        table.rows().every(function(){
            // If row has details expanded
            if(this.child.isShown()){
                // Collapse row details
                this.child.hide();
                $(this.node()).removeClass('shown');
            }
        });
    });
});

/* Formatting function for row details - modify as you need */
