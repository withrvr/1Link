// drag and drop feature
// using sortable.js
const dashboard_Links_Wrapper = document.getElementById(
	"dashboard-links-wrapper"
);
new Sortable(dashboard_Links_Wrapper, {
	animation: 200,
	ghostClass: "bg-warning",
});

// shows stats of links
// using chart.js
let links_clicks_stats = document
	.getElementById("links-clicks-stats")
	.getContext("2d");

new Chart(links_clicks_stats, {
	type: "pie",
	data: {
		labels: Object.keys(links_clicks_data),
		datasets: [
			{
				label: "# of Votes",
				data: Object.values(links_clicks_data),
				backgroundColor: [
					"rgba(255, 99, 132, 0.2)",
					"rgba(54, 162, 235, 0.2)",
					"rgba(255, 206, 86, 0.2)",
					"rgba(75, 192, 192, 0.2)",
					"rgba(153, 102, 255, 0.2)",
					"rgba(255, 159, 64, 0.2)",
				],
				borderColor: [
					"rgba(255, 99, 132, 1)",
					"rgba(54, 162, 235, 1)",
					"rgba(255, 206, 86, 1)",
					"rgba(75, 192, 192, 1)",
					"rgba(153, 102, 255, 1)",
					"rgba(255, 159, 64, 1)",
				],
				borderWidth: 1,
			},
		],
	},
	options: {
		scales: {
			y: {
				beginAtZero: true,
			},
		},
	},
});
