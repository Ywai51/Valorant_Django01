$(window).scroll(
    function() {
        var scroll = $(window).scrollTop();

        document.getElementById("body1").style.marginTop = (-100 - 0.5*scroll) + "px";
        
        if (scroll >= 100) {
            $("#navbarku").addClass("bg-dark");
        }else{
            $("#navbarku").removeClass("bg-dark");
        }
    });