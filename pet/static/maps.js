// const position = { lat: 40.785091, lng: -73.968285 }; // New York City coordinates

// Initialize and add the map
let map;

async function initMap() {
  // The location of Uluru
  const position = { lat: 40.785091, lng: -73.968285 };
  // Request needed libraries.
  //@ts-ignore
  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  // The map, centered at Uluru
  map = new Map(document.getElementById("map"), {
    zoom: 20,
    center: position,
    mapId: "DEMO_MAP_ID",
  });

  // The marker, positioned at Uluru
  const marker = new AdvancedMarkerElement({
    map: map,
    position: position,
    title: "NYC",
  });
}

initMap();