// Initialize the map
function initMap() {
    // Create a map centered on New York City
    var map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 40.785091, lng: -73.968285 }, // New York City coordinates
        zoom: 14 // Adjust the zoom level as needed
    });

    // Create a Places Service object
    var placesService = new google.maps.places.PlacesService(map);

    // Define a request for nearby dog parks
    var request = {
        location: map.getCenter(),
        radius: 5000, // Search radius in meters
        keyword: 'dog park' // Keyword to search for dog parks
    };

    // Perform the nearby search
    placesService.nearbySearch(request, function (results, status) {
        if (status === google.maps.places.PlacesServiceStatus.OK) {
            // Handle the list of nearby dog parks (results)
            // You can display this information on the map or in a list
        }
    });
}
