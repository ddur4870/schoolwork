// Head Script


// select current location from current url shown in browser.
var currentLocation = document.location.pathname.toString().split("/").pop();

if (currentLocation == "home"){
    $("#home").toggleClass("active");
}else if (currentLocation == "profile"){
    $("#profile").toggleClass("active");
}else if (currentLocation == "message"){
    $("#messages").toggleClass("active");
}else if (["ht-cs","jas", "pyt"].includes(currentLocation)){ // Web Development Pages
    $("#webDev").toggleClass("active");
}else if (["apach", "ngin", "aws", "azure", "digoc"].includes(currentLocation)){ // Hosting Pages
    $("#hosting").toggleClass("active");
}else if (["net", "php", "frames", "stack", "ends"].includes(currentLocation)){ // Further information Pages
    $("#furtherInfo").toggleClass("active");
}