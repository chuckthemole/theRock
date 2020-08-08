function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
  }
}

function showPosition(position) {
  // Find coordinates
  var lat = position.coords.latitude;
  var long = position.coords.longitude;
}
//x.innerHTML = "( " + lat + ", " + long + " )\n"; // display coordinates
