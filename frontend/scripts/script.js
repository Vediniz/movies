document.addEventListener('DOMContentLoaded', function () {
    fetch('http://127.0.0.1:8000/movies')
        .then(response => response.json())
        .then(data => {
            const movieList = document.getElementById('movie-list');
            data.results.forEach(movie => {
                const movieItem = document.createElement('li');
                movieItem.textContent = movie.name; 
                movieList.appendChild(movieItem);
            });
        })
        .catch(error => console.error('Error fetching movies:', error));
});
