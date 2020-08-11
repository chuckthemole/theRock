
//https://developers.google.com/maps/documentation/javascript/overview#maps_map_simple-javascript

function create_map(lat, long, index) {
  var latitude = lat;
  var longitude = long;

  // Create the script tag, set the appropriate attributes
  var script = document.createElement('script');
  script.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyBLjXOk51pE-rRddkuHJeHIFVf_90rCYko&callback=initMap";
  script.defer = true;

  // Attach your callback function to the `window` object
  window.initMap = function() {
    // The location of Uluru
    var uluru = {lat: latitude, lng: longitude};
    // The map, centered at Uluru
    var map = new google.maps.Map(
        document.getElementById(index), {zoom: 17, center: uluru});
    // The marker, positioned at Uluru
    var marker = new google.maps.Marker({position: uluru, map: map});
  };

  // Append the 'script' element to 'head'
  document.head.appendChild(script);
}
