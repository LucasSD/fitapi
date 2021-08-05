// Create the namespace instance
let ns = {};

// Create the model instance
ns.model = (function() {
    'use strict';

    let $event_pump = $('body');

    // Return the API
    return {
        'read': function() {
            let ajax_options = {
                type: 'GET',
                url: 'api/daily',
                accepts: 'application/json',
                dataType: 'json'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_read_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        create: function(endDate, startDate) {
            let ajax_options = {
                type: 'POST',
                url: 'api/daily',
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    'endDate': endDate,
                    'startDate': startDate
                })
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_create_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        update: function(endDate, startDate) {
            let ajax_options = {
                type: 'PUT',
                url: 'api/daily/' + startDate,
                accepts: 'application/json',
                contentType: 'application/json',
                dataType: 'json',
                data: JSON.stringify({
                    'endDate': endDate,
                    'startDate': startDate
                })
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_update_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        },
        'delete': function(startDate) {
            let ajax_options = {
                type: 'DELETE',
                url: 'api/daily/' + startDate,
                accepts: 'application/json',
                contentType: 'plain/text'
            };
            $.ajax(ajax_options)
            .done(function(data) {
                $event_pump.trigger('model_delete_success', [data]);
            })
            .fail(function(xhr, textStatus, errorThrown) {
                $event_pump.trigger('model_error', [xhr, textStatus, errorThrown]);
            })
        }
    };
}());

// Create the view instance
ns.view = (function() {
    'use strict';

    let $endDate = $('#endDate'),
        $startDate = $('#startDate');

    // return the API
    return {
        reset: function() {
            $startDate.val('');
            $endDate.val('').focus();
        },
        update_editor: function(endDate, startDate) {
            $startDate.val(startDate);
            $endDate.val(endDate).focus();
        },
        build_table: function(dailyInfo) { // dailyInfo was people
            let rows = ''

            // clear the table
            $('.dailyInfo table > tbody').empty();

            // did we get a dailyInfo array?
            if (dailyInfo) {
                for (let i=0, l=dailyInfo.length; i < l; i++) {
                    rows += `<tr><td class="endDate">${dailyInfo[i].endDate}</td><td class="startDate">${dailyInfo[i].startDate}</td><td>${dailyInfo[i].timestamp}</td></tr>`;
                }
                $('table > tbody').append(rows);
            }
        },
        error: function(error_msg) {
            $('.error')
                .text(error_msg)
                .css('visibility', 'visible');
            setTimeout(function() {
                $('.error').css('visibility', 'hidden');
            }, 3000)
        }
    };
}());

// Create the controller
ns.controller = (function(m, v) {
    'use strict';

    let model = m,
        view = v,
        $event_pump = $('body'),
        $endDate = $('#endDate'),
        $startDate = $('#startDate');

    // Get the data from the model after the controller is done initializing
    setTimeout(function() {
        model.read();
    }, 100)

    // Validate input
    function validate(endDate, startDate) {
        return endDate !== "" && startDate !== "";
    }

    // Create our event handlers
    $('#create').click(function(e) {
        let endDate = $endDate.val(),
            startDate = $startDate.val();

        e.preventDefault();

        if (validate(endDate, startDate)) {
            model.create(endDate, startDate)
        } else {
            alert('Problem with startDate or endDate input');
        }
    });

    $('#update').click(function(e) {
        let endDate = $endDate.val(),
            startDate = $startDate.val();

        e.preventDefault();

        if (validate(endDate, startDate)) {
            model.update(endDate, startDate)
        } else {
            alert('Problem with startDate or endDate input');
        }
        e.preventDefault();
    });

    $('#delete').click(function(e) {
        let startDate = $startDate.val();

        e.preventDefault();

        if (validate('placeholder', startDate)) {
            model.delete(startDate)
        } else {
            alert('Problem with startDate or endDate input');
        }
        e.preventDefault();
    });

    $('#reset').click(function() {
        view.reset();
    })

    $('table > tbody').on('dblclick', 'tr', function(e) {
        let $target = $(e.target),
            endDate,
            startDate;

        endDate = $target
            .parent()
            .find('td.endDate')
            .text();

        startDate = $target
            .parent()
            .find('td.startDate')
            .text();

        view.update_editor(endDate, startDate);
    });

    // Handle the model events
    $event_pump.on('model_read_success', function(e, data) {
        view.build_table(data);
        view.reset();
    });

    $event_pump.on('model_create_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_update_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_delete_success', function(e, data) {
        model.read();
    });

    $event_pump.on('model_error', function(e, xhr, textStatus, errorThrown) {
        let error_msg = textStatus + ': ' + errorThrown + ' - ' + xhr.responseJSON.detail;
        view.error(error_msg);
        console.log(error_msg);
    })
}(ns.model, ns.view));
