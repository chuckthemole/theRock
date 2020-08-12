
function load_map(latitude, longitude, index) {
  // Create the script tag, set the appropriate attributes
  var script = document.createElement('script');
  script.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyBLjXOk51pE-rRddkuHJeHIFVf_90rCYko&callback=initMap";
  script.defer = true;

  // Attach your callback function to the `window` object
  window.initMap = function() {
    // The location of Uluru
    var uluru = {lat: latitude, lng: longitude};
    // The map, centered at Uluru
    var map = new google.maps.Map(document.getElementById(index), {zoom: 17, center: uluru});

    // The marker, positioned at Uluru
    var marker = new google.maps.Marker({position: uluru, map: map});
  };

  // Append the 'script' element to 'head'
  document.head.appendChild(script);
}

function load_map_array(all_locations) {
  var maps = [];

  for(location in all_locations) {
    // Create the script tag, set the appropriate attributes
    var script = document.createElement('script');
    script.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyBLjXOk51pE-rRddkuHJeHIFVf_90rCYko&callback=initMap";
    script.defer = true;

    // Attach your callback function to the `window` object
    window.initMap = function() {
      // The location of Uluru
      var uluru = {lat: location.latitude, lng: location.longitude};
      // The map, centered at Uluru
      var map = new google.maps.Map(document.getElementById(location.id), {zoom: 17, center: uluru});
      maps.push(map);

      // The marker, positioned at Uluru
      var marker = new google.maps.Marker({position: uluru, map: map});
    };

    // Append the 'script' element to 'head'
    document.head.appendChild(script);
  }
}
