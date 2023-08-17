function searchRestaurants() {
    const location = document.getElementById("location").value;
    const url = `/search?location=${location}`;

    const restaurantsDiv = document.getElementById("restaurants");
    restaurantsDiv.innerHTML = "<p>Loading...</p>";

    fetch(url)
        .then(response => response.json())
        .then(data => {
            restaurantsDiv.innerHTML = "";

            data.forEach(restaurant => {
                const restaurantDiv = document.createElement("div");
                restaurantDiv.className = "restaurant";

                const restaurantInfo = `
                    <h2>${restaurant.name}</h2>
                    <p>Address: ${restaurant.address}</p>
                    <p>Rating: ${restaurant.rating}</p>
                `;

                restaurantDiv.innerHTML = restaurantInfo;
                restaurantsDiv.appendChild(restaurantDiv);
            });
        })
        .catch(error => {
            restaurantsDiv.innerHTML = "<p>Error fetching data.</p>";
            console.error("Error fetching data:", error);
        });
}
