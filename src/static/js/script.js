function getWeather() {
    const city = document.getElementById("city").value;
    const weatherDiv = document.getElementById("weather")
    $.ajax({
        url: `/weather?city=${city}`,
        method: "GET",
        success: function (data) {
            console.log(data)
            $(weatherDiv).html(`<div class="city">${data.city}</div>
                                       <div class="date">Tuesday, April 16</div>
                                       <img class="weather-icon" src=${data.icon}>
                                       <div class="temperature">${data.temp}°C</div>
                                       <div class="description">${data.description}</div>
                                       <div class="details">
                                            <div>Humidity: 60%</div>
                                            <div>Wind: 5 km/h</div>
                                        </div>`);

        },
    });
}
