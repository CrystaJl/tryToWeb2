var timeDisplay = document.getElementById("time");


function refreshTime() {
  var dateString = new Date().toLocaleString("ru", {timeZone: "Europe/Moscow"});
  var formattedString = dateString.replace(", ", "/");
  timeDisplay.innerHTML = formattedString;
}

setInterval(refreshTime, 1000);



function contacts(){
  window.location.href = 'contacts.html';

}
function journal(){
  window.location.href = 'journal.html';

}
function monitoring(){
  window.location.href = 'monitoring.html';
}
function engineeringMenu(){
  window.location.href = 'engineeringMenu.html';
}
function installationScheduler(){
  window.location.href = 'installationScheduler.html'
}

function stationSettings(){
  window.location.href = 'stationSettings.html'
}

function panelSettings(){
  window.location.href = 'panelSettings.html'
}

function specifications(){
  getSpecifications = document.getElementById('specifications')
  getSpecifications.innerHTML = navigator.platform;
}
specifications()

function getDateFunc(){
  var currentDate = new Date();
  var day = currentDate.getDate(); 
  var month = currentDate.getMonth() + 1; 
  var year = currentDate.getFullYear(); 

  var getDate = document.getElementById('getDate');
  getDate.innerHTML = day + '/' + month + '/' + year;
}
getDateFunc();

// можно это пофиксить пж
// function getDayFunc(){
//   var currentDate = new Date();
//   var day = currentDate.getDay(); 

//   var getDate = document.getElementById('getDay');
// }
// getDateFunc();















