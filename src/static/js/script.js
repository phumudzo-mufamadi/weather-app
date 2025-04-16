function getWeather() {
    const city = document.getElementById("city").value;
    const weatherDiv = document.getElementById("weather")
    $.ajax({
        url: `/weather?city=${city}`,
        method: "GET",
        success: function (data) {
            $(weatherDiv).html(data);
        },
    });
}
