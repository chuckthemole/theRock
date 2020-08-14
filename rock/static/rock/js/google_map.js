
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
    var main_marker = marker.getIcon();

    marker.addListener('mouseover', function() {
      //map.setZoom(8);
      //map.setCenter(marker.getPosition());

      marker.setIcon('https://img.icons8.com/doodle/48/000000/basketball--v1.png');
    });
    marker.addListener('mouseout', function() {
      marker.setIcon(main_marker);
    });
  };

  //google.maps.event.addDomListener(window, 'load', initialize);

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
    var marker = [];
    var main_marker = [];
    var i;

    for (i = 0; i < coordinates.length; i++) {
      marker[i] = new google.maps.Marker({
        position: new google.maps.LatLng(coordinates[i][0], coordinates[i][1]),
        map: map
      });
      main_marker[i] = marker[i].getIcon();

      marker[i].addListener('mouseover', function() {
        //map.setZoom(8);
        //map.setCenter(marker.getPosition());

        marker[i].setIcon('https://img.icons8.com/doodle/48/000000/basketball--v1.png');
      });
      marker[i].addListener('mouseout', function() {
        marker[i].setIcon(main_marker[i]);
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
  document.head.appendChild(script);
}
