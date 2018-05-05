var names_url = "/names";
var otu_url = "/otu";

Plotly.d3.json(names_url,function(error, names) {
    if (error) return console.log(error);

    var SELECT = document.getElementById("selDataset")
    var option = document.createElement("option")

    function add_option(item) {
        option.innerHTML = item;
        SELECT.append(option);
    }

    names.forEach(add_option)
})

