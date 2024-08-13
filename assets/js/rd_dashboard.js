function createRegionChart(data) {
    const ctx = document.getElementById('regionChart').getContext('2d');
    const regions = [...new Set(data.map(item => item.region))];
    const regionCounts = regions.map(region => data.filter(item => item.region === region).length);

    // Generate a unique color for each bar
    const backgroundColors = regions.map((_, index) => `hsl(${index * 360 / regions.length}, 70%, 50%)`);
    const borderColors = regions.map((_, index) => `hsl(${index * 360 / regions.length}, 70%, 40%)`);

    new Chart(ctx, {
        type: 'bar', 
        data: {
            labels: regions,
            datasets: [{
                label: 'No of R&D Activities',
                data: regionCounts,
                backgroundColor: backgroundColors,
                borderColor: borderColors,
                borderWidth: 1,
                barThickness: 10, 
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true, // Ensure y-axis starts at zero
                    min: 0, // Explicitly set the minimum value of the y-axis to 0
                    ticks: {
                        autoSkip: false, // Show all y-axis labels
                    }
                },
                x: {
                    ticks: {
                        autoSkip: false // Ensure all labels are shown on the x-axis
                    }
                }
            }
        }
    });
}



function createThemeChart(data) {
    const ctx = document.getElementById('themeChart').getContext('2d');
    const themes = [...new Set(data.map(item => item.Theme))];
    const themeCounts = themes.map(theme => data.filter(item => item.Theme === theme).length);

    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: themes,
            datasets: [{
                label: 'No of R&D Activities',
                data: themeCounts,
                backgroundColor: ['red', 'blue', 'green', 'yellow', 'purple', 'orange'],
            }]
        },
    });
}
