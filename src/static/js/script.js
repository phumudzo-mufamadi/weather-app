function getWeather() {
    const city = document.getElementById("city").value;
    const weatherDiv = document.getElementById("weather");

    $.ajax({
        url: `/weather?city=${city}`,
        method: "GET",
        success: function (data) {
            if (Object.keys(data).length === 0 && data.constructor === Object) {
                $(weatherDiv).html('<div class="error">No weather data found for the specified city. Please try a different city.</div>');
            } else {
                $(weatherDiv).html(`
                    <div class="city">${data.city}</div>
                    <div class="date">${data.weather_date}</div>
                    <img class="weather-icon" src=${data.icon}>
                    <div class="temperature">${data.temp}°C</div>
                    <div class="description">${data.description}</div>
                    <div class="details">
                        <div>Humidity: ${data.humidity}%</div>
                        <div>Wind: ${data.wind_speed} km/h</div>
                    </div>
                `);
            }
        },
        error: function () {
            $(weatherDiv).html('<div class="error">Unable to fetch weather data at the moment. Please check your network or try again later.</div>');
        }
    });
}
