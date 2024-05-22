document.getElementById('generate-plot-btn').addEventListener('click', function() {
    const xAxis = document.getElementById('x-axis').value;
    const yAxis = document.getElementById('y-axis').value;
    const plotType = document.getElementById('plot-type').value;
    const filename = this.getAttribute('data-filename');

    fetch('/generate_plot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ filename: filename, x_axis: xAxis, y_axis: yAxis })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            console.error('Error:', data.error);
            return;
        }
        const plotData = [{
            x: data.x,
            y: data.y,
            type: plotType
        }];

        Plotly.newPlot('plot', plotData);
    })
    .catch(error => {
        console.error('Error generating plot:', error);
    });
});
