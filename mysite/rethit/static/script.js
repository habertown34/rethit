for (var i = 1; i <= {{num}}; i++)
{
    $("#up" + i).click(function(){
        $.ajax({
            url: "{% url 'upvote' %}",
            success: function(result) {
                num = parseInteger($("#votes" + i).html);
                $("#votes" + i).html = num + 1;
            }
        });
    });
}