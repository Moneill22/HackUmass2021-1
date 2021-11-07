document.addEventListener('DOMContentLoaded', () => {

    // set the dimensions and margins of the graph
    var margin = {top: 10, right: 30, bottom: 40, left: 50},
        width = window.innerWidth/3 - margin.left - margin.right,
        height = window.innerWidth/3 - margin.top - margin.bottom;

    // append the svg object to the body of the page
    var svg = d3.select("#plot")
    .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")")

    // Add the grey background that makes ggplot2 famous
    svg
    .append("rect")
        .attr("x",0)
        .attr("y",0)
        .attr("height", height)
        .attr("width", height)
        .style("fill", "snow")

    //Read the data
    d3.json("https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/iris.json", function(data) {

        // Add X axis
        var x = d3.scaleLinear()
            .domain([0, 4])
            .range([ 0, width ])
        svg.append("g")
            .attr("transform", "translate(0," + height + ")")
            .call(d3.axisBottom(x).tickSize(-height*1.3).ticks(10))
            .select(".domain").remove()

        // Add Y axis
        var y = d3.scaleLinear()
            .domain([0, 4])
            .range([ height, 0])
            .nice()
        svg.append("g")
            .call(d3.axisLeft(y).tickSize(-width*1.3).ticks(7))
            .select(".domain").remove()

        // Customization
        svg.selectAll(".tick line").attr("stroke", "#EEE9E9")

        // Add X axis label:
        svg.append("text")
            .attr("text-anchor", "end")
            .attr("x", width/2 + margin.left)
            .attr("y", height + margin.top + 20)
            .text("Hours worked at internship");

        // Y axis label:
        svg.append("text")
            .attr("text-anchor", "end")
            .attr("transform", "rotate(-90)")
            .attr("y", -margin.left + 20)
            .attr("x", -margin.top - height/2 + 20)
            .text("GPA")

        // Color scale: give me a specie name, I return a color
        var color = d3.scaleOrdinal()
            .domain(["accepted", "rejected", "pending" ])
            .range([ "00FF00", "#FF0000", "#FFFF00"])

        // Add dots
        svg.append('g')
            .selectAll("dot")
            .data(data)
            .enter()
            .append("circle")
            .attr("cx", function (d) { return x(d.GPA); } )
            .attr("cy", function (d) { return y(d.College_Prestige); } )
            .attr("r", 5)
            .style("fill", function (d) { return color(d.Species) } )

    });
});