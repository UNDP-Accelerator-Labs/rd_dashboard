---
layout: default
title: R&D Dashboard
---

<h6>Guage Chart</h6>
<p>
These gauges represent the current activity levels for different themes such as "Cities," "Circular Economy," "Food Systems," "Civic Engagement," and "Tourism." The needle indicates the exact count of R&D activities under each theme, with a maximum scale set at 200. As the activity count increases, the needle moves across the colored spectrum, which transitions from yellow to green, symbolizing low to high levels of engagement. This visualization provides a quick snapshot of which themes are most actively pursued.
</p>
<br/>
<div id="canvas-holder" style="display: flex; flex-wrap: wrap; justify-content: space-around; margin-botton: 10px;">
</div>

<div class="grid-x" style="margin-top: 5rem;">
    <div class="cell large-6 small-12 generic-content">
        <h6>  Bar Chart - R&D Activities Across Regions </h6>
        <p>
        The bar chart provides a visual comparison of the number of R&D activities across different regions, specifically "RBAS," "RBAP," "RBLAC," "RBA," and "RBEC." Each bar's height corresponds to the activity count, with different colors representing each region. This chart helps identify regions with the highest and lowest levels of R&D engagement, making it easier to understand geographical distribution of activities.
        </p>
        <canvas id="regionChart"></canvas>
    </div>
    <div class="cell large-6 small-12 generic-content">
    <h6>Pie Chart - Topics Across Themes </h6>
    <p>
    This pie chart breaks down the distribution of topics across various themes within the R&D activities. Each slice of the pie represents a theme, with the size of the slice proportional to the number of activities under that theme. The percentages on the slices provide an easy-to-read understanding of how the activities are distributed among themes such as "Circular Economy," "Cities," "Civic Engagement," "Food Systems," and "Tourism." The legend identifies each theme by color, ensuring clarity in understanding the chart.
    </p>
        <canvas id="topicsThemeChart"></canvas>
    </div>
</div>

<div class="cell large-6 small-12 generic-content" style="margin-top: 5rem;">
    <h6>Heatmap - Themes Across Countries </h6>
    <p>
    This heatmap visualizes the distribution of various R&D themes across different countries. Each row represents a country, while each column corresponds to a specific theme. The intensity of the color within each cell indicates the number of activities related to that theme in the respective country.
    It allows for quick identification of countries that are particularly active in specific R&D themes. It also highlights countries where certain themes might be underrepresented, potentially guiding future research efforts or resource allocation.
    </p>
    <div id="themes-country"></div>
</div>

