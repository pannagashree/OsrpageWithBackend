function myFunction() {
    var x = document.getElementById("myTopnav");

    /*if (x.className === "container") {*/
        x.className += " responsive";
    /*} else {
        x.className = "container";
    }
    /*document.getElementById("myTopnav").style.width = "100%";*/
}
function closeNav(){
    var x = document.getElementById("myTopnav");
        x.className = "container";
} 