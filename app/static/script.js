document.addEventListener("DOMContentLoaded", function() {
    // Handle click event on the "Generate Plot" button
    document.getElementById("generate-plot-btn").addEventListener("click", function() {
        // Dummy data for demonstration
        var x = [1, 2, 3, 4, 5];
        var y = [10, 15, 13, 17, 18];

        // Create a Plotly trace
        var trace = {
            x: x,
            y: y,
            type: 'scatter'
        };

        // Create a Plotly data array
        var data = [trace];

        // Define Plotly layout
        var layout = {
            title: 'Sample Plot',
            xaxis: {
                title: 'X-axis'
            },
            yaxis: {
                title: 'Y-axis'
            }
        };

        // Plot the data
        Plotly.newPlot('plot', data, layout);
    });
});
