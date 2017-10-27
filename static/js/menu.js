function openMenu(evt, menuName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the link that opened the tab
    document.getElementById(menuName).style.display = "block";
    evt.currentTarget.className += " active";
    var ele=evt.currentTarget.className;
    var ele1=document.getElementsByClassName(ele)[0].parentElement;
    var var1=evt.currentTarget.innerHTML;
    var var2='&#9660';
    document.getElementsByClassName("dropbtn2")[0].innerHTML=var1.toUpperCase().concat(var2);
    if(ele1.className!="tab")
    {
        var childs=document.getElementsByClassName('tab')[0].childNodes;
        for(i=0;i<childs.length;i++)
        {
            if(childs[i].innerHTML==var1)
            {
                childs[i].className+=" active";
            }
        }
    }
    ele1.classList.remove("show");
}
$(".content a").click(function(e) {
   //do something
   e.stopPropagation();
})
