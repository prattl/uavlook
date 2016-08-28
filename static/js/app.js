// Foundation JavaScript
// Documentation can be found at: http://foundation.zurb.com/docs

// Expand home page height to use the full page
$( window ).resize(function() {
    var nav_height = $(".top-bar").height();
    var screen_height = $(window).height();
    console.log('Got screen height: ' + screen_height)
    if (screen_height > 650) {
        $(".home-page-plugin").height(screen_height - nav_height);
        $(".home-page-plugin").find(".content-container").height(screen_height - nav_height);
    }
});

$(function() {
    $(document).foundation();

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    // Expand the height of the contact form message textarea to fill the entire
    // height, only if it is present on the page
    var $contact_form_plugin = $(".contact-form-plugin");
    if ($contact_form_plugin.length > 0) {
        var $container_height = $contact_form_plugin.height();
        var $message_label_height = $("#id_message_label").height();
        var $phone_margin_bottom = $("#id_phone").css("margin-bottom").replace("px", "");

        $("#id_message_label").height();
        console.log("Got vars:");
        console.log($container_height);
        console.log($message_label_height);
        console.log($phone_margin_bottom);
    }

    $(window).resize();

    // Add a class to any <p> elements that contain an image
    $("img").parent("p").addClass("img-container");

    $("body").on("contextmenu", "img", function(e) {
      return false;
    });

    // Contact Form Ajax Submit
    var $contact_form = $("form.contact-form");
    var $contact_submit = $(".contact-submit");

    function submit_contact_form() {
        var json_data = {
            "name": $("#id_name").val(),
            "email": $("#id_email").val(),
            "phone": $("#id_phone").val(),
            "message": $("#id_message").val(),
            "inquiry_type": $("#id_inquiry_type").val(),
            "contact_form": $("#contact-form-id").val()
        };
        var data = json_data;//JSON.stringify(json_data);
        console.log('Submitting data: ' + data);
        console.log('Submitting to url: ' + $contact_form.attr("action"));
        return $.ajax({
            type: "POST",
            //contentType: "application/json;charset=UTF-8",
            data: data,
            //dataType: "json",
            url: $contact_form.attr("action")
        });
    }

    // Contact form submit handler
    $contact_form.submit(function(e) {
        e.preventDefault();
        $contact_submit.attr("disabled", true);
        submit_contact_form().done(contact_form_callback);
    });

    // Contact form Ajax callback
    function contact_form_callback(result) {
        if (result['status'] == 1) {
            // Hide the form elements and display a thank you message.
            $contact_form.hide();
            $(".contact-thank-you").show();
            console.log('Sucess.')
        } else {
            // Display an error message
            console.log('Error.');
            $(".errors").show();
            var error;
            for (error in result['errors']) {
                $(".errors-list").append("<li>" + error + "</li>");
            }
        }

        $contact_submit.removeAttr("disabled");
    }

});

