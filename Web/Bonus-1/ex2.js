function bodyLoaded() {
    console.log("Body Loaded")
}
var search = document.getElementById("searcheverything");
console.log(search);

var rects = document.getElementsByClassName("rect");
console.log(rects);

var buttons = document.getElementsByTagName("button");
console.log(buttons);

var favAni = document.getElementById("FavAni");
var favAnilist = favAni.getElementsByTagName("li");
console.log(favAnilist);

var searchBar = document.getElementById("searchbar")
console.log(searchBar.getAttribute(target))