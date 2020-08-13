
function load_map(latitude, longitude) {
  // Create the script tag, set the appropriate attributes
  var script = document.createElement('script');
  script.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyBLjXOk51pE-rRddkuHJeHIFVf_90rCYko&callback=initMap";
  script.defer = true;

  // Attach your callback function to the `window` object
  window.initMap = function() {
    // The location of Uluru
    var uluru = {lat: latitude, lng: longitude};
    // The map, centered at Uluru
    var map = new google.maps.Map(document.getElementById("map"), {zoom: 17, center: uluru});
    // The marker, positioned at Uluru
    var marker = new google.maps.Marker({position: uluru, map: map});
  };

  // Append the 'script' element to 'head'
  document.head.appendChild(script);
}

function load_map_multiple_markers(coordinates) {
  // Create the script tag, set the appropriate attributes
  var script = document.createElement('script');
  script.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyBLjXOk51pE-rRddkuHJeHIFVf_90rCYko&callback=initMap";
  script.defer = true;

  window.initMap = function() {
    var uluru = {lat: coordinates[0][0], lng: coordinates[0][1]};
    var map = new google.maps.Map(document.getElementById("map"), {zoom: 17, center: uluru});
    var marker, i;
      for (i = 0; i < coordinates.length; i++) {
        marker = new google.maps.Marker({
          position: new google.maps.LatLng(coordinates[i][0], coordinates[i][1]),
          map: map
        });

        google.maps.event.addListener(marker, 'click', (function(marker, i) {
          return function() {
            //infowindow.setContent(coordinates[i][2]);
            infowindow.open(map, marker);
          }
        })(marker, i));
      }
    }
  document.head.appendChild(script);
}
