
function load_map_basketball(latitude, longitude) {
  // Attach your callback function to the `window` object
  window.initMap = function() {
    // The location of Uluru
    var uluru = {lat: latitude, lng: longitude};
    // The map, centered at Uluru
    var map = new google.maps.Map(document.getElementById("map"), {zoom: 17, center: uluru});
    // The marker, positioned at Uluru
    var marker = new google.maps.Marker({position: uluru, map: map});
    var main_marker = marker.getIcon();

    marker.addListener('mouseover', function() {
      //map.setZoom(8);
      //map.setCenter(marker.getPosition());

      marker.setIcon('https://img.icons8.com/doodle/48/000000/basketball--v1.png');
      //marker.setIcon('https://img.icons8.com/doodle/48/000000/basketball--v1.png');

    });
    marker.addListener('mouseout', function() {
      marker.setIcon(main_marker);
    });
  };

  //google.maps.event.addDomListener(window, 'load', initialize);

  // Create the script tag, set the appropriate attributes
  var script = document.createElement('script');
  script.defer = true;
  script.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyBLjXOk51pE-rRddkuHJeHIFVf_90rCYko&callback=initMap";

  // Append the 'script' element to 'head'
  document.head.appendChild(script);
}

function load_map_baseball(latitude, longitude) {
  // Attach your callback function to the `window` object
  window.initMap = function() {
    // The location of Uluru
    var uluru = {lat: latitude, lng: longitude};
    // The map, centered at Uluru
    var map = new google.maps.Map(document.getElementById("map"), {zoom: 17, center: uluru});
    // The marker, positioned at Uluru
    var marker = new google.maps.Marker({position: uluru, map: map});
    var main_marker = marker.getIcon();

    marker.addListener('mouseover', function() {
      //map.setZoom(8);
      //map.setCenter(marker.getPosition());

      marker.setIcon('https://img.icons8.com/dusk/64/000000/baseball.png');
      //marker.setIcon('https://img.icons8.com/doodle/48/000000/basketball--v1.png');

    });
    marker.addListener('mouseout', function() {
      marker.setIcon(main_marker);
    });
  };

  //google.maps.event.addDomListener(window, 'load', initialize);

  // Create the script tag, set the appropriate attributes
  var script = document.createElement('script');
  script.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyBLjXOk51pE-rRddkuHJeHIFVf_90rCYko&callback=initMap";
  script.defer = true;

  // Append the 'script' element to 'head'
  document.head.appendChild(script);
}

function load_map_tennis(latitude, longitude) {
  // Attach your callback function to the `window` object
  window.initMap = function() {
    // The location of Uluru
    var uluru = {lat: latitude, lng: longitude};
    // The map, centered at Uluru
    var map = new google.maps.Map(document.getElementById("map"), {zoom: 17, center: uluru});
    // The marker, positioned at Uluru
    var marker = new google.maps.Marker({position: uluru, map: map});
    var main_marker = marker.getIcon();

    marker.addListener('mouseover', function() {
      //map.setZoom(8);
      //map.setCenter(marker.getPosition());

      marker.setIcon('https://img.icons8.com/dusk/64/000000/tennis.png');
      //marker.setIcon('https://img.icons8.com/doodle/48/000000/basketball--v1.png');

    });
    marker.addListener('mouseout', function() {
      marker.setIcon(main_marker);
    });
  };

  //google.maps.event.addDomListener(window, 'load', initialize);

  // Create the script tag, set the appropriate attributes
  var script = document.createElement('script');
  script.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyBLjXOk51pE-rRddkuHJeHIFVf_90rCYko&callback=initMap";
  script.defer = true;
  // Append the 'script' element to 'head'
  document.head.appendChild(script);
}

function load_map_multiple_markers(coordinates, sports) {
  window.initMap = function() {
    var uluru = {lat: coordinates[0][0], lng: coordinates[0][1]};
    var map = new google.maps.Map(document.getElementById("map"), {zoom: 17, center: uluru});
    var marker;
    var main_marker;
    var i;

    for (i = 0; i < coordinates.length; i++) {
      marker = new google.maps.Marker({
        position: new google.maps.LatLng(coordinates[i][0], coordinates[i][1]),
        map: map
      });

      if (sports[i] == 'basketball') {
        marker.setIcon('https://img.icons8.com/doodle/48/000000/basketball--v1.png');
      }
      else if (sports[i] == 'baseball') {
        marker.setIcon('https://img.icons8.com/dusk/64/000000/baseball.png');
      }
      else if (sports[i] == 'tennis') {
        marker.setIcon('https://img.icons8.com/dusk/64/000000/tennis.png');
      }
      else {}

      main_marker = marker.getIcon();

      marker.addListener('mouseover', function() {
        //map.setZoom(8);
        //map.setCenter(marker.getPosition());

        marker.setIcon(main_marker);
      });
      marker.addListener('mouseout', function() {
        marker.setIcon(main_marker);
      });

//        google.maps.event.addListener(marker[i], 'click', (function(marker[i], i) {
//        return function() {
          // To do: if clicked move to that location in window
          //infowindow.setContent(coordinates[i][2]);
  //        infowindow.open(map, marker[i]);
    //    }
      //})(marker[i], i));
    }
  }

  // Create the script tag, set the appropriate attributes
  var script = document.createElement('script');
  script.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyBLjXOk51pE-rRddkuHJeHIFVf_90rCYko&callback=initMap";
  script.defer = true;

  document.head.appendChild(script);
}
