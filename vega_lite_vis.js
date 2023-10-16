var vg_1 = "https://raw.githubusercontent.com/JackLin07/FIT3179-DataVisualisation_A2/main/codes/test.vg.json";
vegaEmbed("#Interest_rate_trend", vg_1).then(function(result) {
// Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);

var map_vg = "https://raw.githubusercontent.com/JackLin07/FIT3179-DataVisualisation_A2/main/codes/globe_map.vg.json";
vegaEmbed("#Map_of_Interest_Rates", map_vg).then(function(result) {
// Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);

var map_vg1 = "https://raw.githubusercontent.com/JackLin07/FIT3179-DataVisualisation_A2/main/codes/map.vg.json";
vegaEmbed("#Map_of_everything", map_vg1).then(function(result) {
// Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);