// Show spinner when button is clicked
document.getElementById("button").addEventListener("click", function () {
    // Show spinner created with boostrap
    document.querySelector(".spinner-border").style.display = "block";
    // Show text --> Loadin please wait
    document.querySelector(".loading_spin").style.display = "block";
});