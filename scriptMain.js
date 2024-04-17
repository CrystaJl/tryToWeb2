var timeDisplay = document.getElementById("time");


function refreshTime() {
  var dateString = new Date().toLocaleString("ru", {timeZone: "Europe/Moscow"});
  var formattedString = dateString.replace(", ", " - ");
  timeDisplay.innerHTML = formattedString;
}

setInterval(refreshTime, 1000);



function contacts(){
    window.location.href = 'contacts.html';
    return false;
}