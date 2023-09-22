// movies.js

document.addEventListener("DOMContentLoaded", () => {
    // Get the movie list container
    const movieListContainer = document.getElementById("movie-list");
  
    // Fetch movie data from the JSON file 
    fetch("data/dog_movies.json")
      .then((response) => response.json())
      .then((movies) => {
        // Loop through the movies and create elements for each movie
        movies.forEach((movie) => {
          // Create a container for each movie
          const movieContainer = document.createElement("div");
          movieContainer.classList.add("movie-container");
  
          // Create an image element for the movie poster
          const posterImg = document.createElement("img");
          posterImg.src = movie.poster;
          posterImg.alt = movie.title;
          posterImg.classList.add("movie-poster");
  
          // Create a title element for the movie
          const titleElement = document.createElement("h2");
          titleElement.textContent = movie.title;
  
          // Create a rating element for the movie
          const ratingElement = document.createElement("p");
          ratingElement.textContent = `Rating: ${movie.movie_rating}`;
  
          // Create a comments element for the movie
          const commentsElement = document.createElement("p");
          commentsElement.textContent = `Comments: ${movie.comments}`;
  
          // Append elements to the movie container
          movieContainer.appendChild(posterImg);
          movieContainer.appendChild(titleElement);
          movieContainer.appendChild(ratingElement);
          movieContainer.appendChild(commentsElement);
  
          // Append the movie container to the movie list
          movieListContainer.appendChild(movieContainer);
        });
      })
      .catch((error) => {
        console.error("Error fetching movie data:", error);
      });
  });
  