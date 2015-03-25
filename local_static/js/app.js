// Foundation JavaScript
// Documentation can be found at: http://foundation.zurb.com/docs
$(document).foundation();

$(function() {
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

    // Disable image right-click
    $("body").on("contextmenu", "img", function(e) {
        return false;
    });
});
