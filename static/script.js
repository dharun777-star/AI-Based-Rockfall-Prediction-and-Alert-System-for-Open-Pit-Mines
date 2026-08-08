function predictRisk() {

    let rainfall = document.getElementById("rainfall").value;
    let slope = document.getElementById("slope").value;
    let crack = document.getElementById("crack").value;
    let moisture = document.getElementById("moisture").value;
    let temperature = document.getElementById("temperature").value;

    fetch("/predict", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            rainfall: rainfall,
            slope: slope,
            crack: crack,
            moisture: moisture,
            temperature: temperature
        })

    })

    .then(response => response.json())

    .then(data => {

        document.getElementById("result").innerHTML =
            "<h2>Risk: " + data.risk + "</h2>" +
            "<h3>Confidence: " + data.score + "%</h3>";

    });
}