var vg_1 = "test.vg.json";
vegaEmbed("#Interest_rate_trend", vg_1).then(function(result) {
// Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);

var map_vg = "globe_map.vg.json";
vegaEmbed("#Map_of_Interest_Rates", map_vg).then(function(result) {
// Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);

var map_vg1 = "map.vg.json";
vegaEmbed("#Map_of_everything", map_vg1).then(function(result) {
// Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);
