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

    // Expand contact form message height


});

