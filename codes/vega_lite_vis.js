var vg_1 = "https://raw.githubusercontent.com/JackLin07/FIT3179-DataVisualisation_A2/main/codes/interest_rate.vg.json";
vegaEmbed("#Interest_rate_trend", vg_1).then(function(result) {
// Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);

var map_vg1 = "https://raw.githubusercontent.com/JackLin07/FIT3179-DataVisualisation_A2/main/codes/map.vg.json";
vegaEmbed("#Map_of_everything", map_vg1).then(function(result) {
// Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);

var wage_vs_house_vs_rent_vg = 'https://raw.githubusercontent.com/JackLin07/FIT3179-DataVisualisation_A2/main/codes/wage_vs_house_price_vs_rent_grouped_bar_chart.vg.json';
vegaEmbed("#WageVsHouseVsRent", wage_vs_house_vs_rent_vg).then(function(result) {
// Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);

var cpi_vs_wage_growth_vg = 'https://raw.githubusercontent.com/JackLin07/FIT3179-DataVisualisation_A2/main/codes/cpi_vs_wage_growth.vg.json';
vegaEmbed("#CPIvsWageGrowth", cpi_vs_wage_growth_vg).then(function(result) {
// Access the Vega view instance (https://vega.github.io/vega/docs/api/view/) as result.view
}).catch(console.error);
