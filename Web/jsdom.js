//check eventListener run
function startClick() {
    console.log("Clicked");
}

var srch = document.getElementById("srch");
srch.textContent = "Search";
srch.style.fontSize = "30px";
//srch.addEventListener("click",startClick)
srch.addEventListener("click",function(tryClick) {console.log("Clicked");})

//change the color of the input bar 
var searchBar = document.getElementById("searchbar")
searchBar.style.backgroundColor = "yellow";
searchBar.value = "";
searchBar.style.color = "red";

//add food in the menu
var menu = document.getElementById("menu");
var addLi = document.createElement("li");
addLi.innerText = "Chicken";
menu.appendChild(addLi);

//remove first food in the menu
// var foodlist = menu.getElementsByTagName("li");
// var firstLi = foodlist[0];
// firstLi.remove();

//remove food by clicking
var delButtons = document.getElementsByClassName("delfood");
for (var i = 0; i < delButtons.length; i++) {
    var delButt = delButtons[i]
    delButt.addEventListener("click",function(e) 
    {
        var srch = e.target;
        var div = srch.parentNode;
        console.log(div);
    })
}
