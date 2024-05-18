document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("generate-plot-btn").addEventListener("click", function() {
        var plotType = document.getElementById("plot-type").value;
        var xColumn = document.getElementById("x-axis").value;
        var yColumn = document.getElementById("y-axis").value;

        var x = jsonData.map(row => row[xColumn]);
        var y = jsonData.map(row => row[yColumn]);

        var trace;
        if (plotType === 'scatter') {
            trace = {
                x: x,
                y: y,
                mode: 'markers',
                type: 'scatter'
            };
        } else if (plotType === 'bar') {
            trace = {
                x: x,
                y: y,
                type: 'bar'
            };
        } else if (plotType === 'line') {
            trace = {
                x: x,
                y: y,
                type: 'scatter',
                mode: 'lines'
            };
        } else if (plotType === 'pie') {
            trace = {
                labels: x,
                values: y,
                type: 'pie'
            };
        }

        var plotData = [trace];
        var layout = {
            title: 'Generated Plot',
            xaxis: {
                title: xColumn
            },
            yaxis: {
                title: yColumn
            }
        };

        Plotly.newPlot('plot', plotData, layout);
    });
});
