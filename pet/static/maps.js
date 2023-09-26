// Initialize and add the map
let map;

async function initMap() {
 console.log("Map is running")
  // Define an array of locations with their names and coordinates
  const locations = [
    {
      name: 'Jones Beach',
      coords: {
        lat: 40.645425,
        lng: -73.293392,
      },
    },
    {
      name: 'Bar Beach',
      coords: {
        lat: 40.762489,
        lng: -73.687405,
      },
    },
    {
      name: 'Central Park',
      coords: {
        lat: 40.785091,
        lng: -73.968285,
      },
    },
    {
      name: 'Montauk Beach',
      coords: {
        lat: 41.067741,
        lng: -71.851374,
      },
    },
    {
      name: 'Long Island City Dog Park',
      coords: {
        lat: 40.785091,
        lng: -73.968285,
      },
    },
    {
      name: 'Throg Neck Dog Park',
      coords: {
        lat: 40.785091,
        lng: -73.968285,
      },
    },
    {
      name: 'Rockaway Beach',
      coords: {
        lat: 40.577222,
        lng: -73.806889,
      },
    },
  ];

  // Request needed libraries.
  
  
  //@ts-ignore
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  // The map, centered at NY my fav dog park coordinates         lat: 40.785091,lng: -73.968285,
  const mapCenter = { lat: 40.785091,lng: -73.968285 };
  map = new Map(document.getElementById("map"), {
    zoom: 15,
    center: mapCenter,
    mapId: "Dogfriendly_Park_MAP_ID",
  });

  // Create markers for each location
  locations.forEach(location => {
    const marker = new AdvancedMarkerElement({
      map: map,
      position: location.coords,
      title: location.name,
    });
  });
}

initMap();
