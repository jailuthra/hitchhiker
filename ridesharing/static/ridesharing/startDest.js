$(document).ready(function(){

    //document.getElementById('dest').style.visibility = "hidden";
    $('#submit-button').prop('disabled', true);

    $("#startPt").change(function() {

        var startPt = document.getElementById("startPt").value;
        if(startPt === "Home")
            opt = "IIIT-Delhi";
        else
            opt = "Home";

        var $dest = $("#dest")
        $dest.empty()
        $dest.append("<option>" + opt + "</option>");
        //document.getElementById('dest').style.visibility = "visible";
        $('#submit-button').prop('disabled', false);

    });

});

        
