var ctx = document.getElementById("line-chart-2");
(Chart.defaults.global.defaultFontFamily = "iransans"), (Chart.defaults.global.defaultFontSize = 14), (Chart.defaults.global.defaultFontStyle = "500"), (Chart.defaults.global.defaultFontColor = "#233d63");
var chart = new Chart(ctx, {
    type: "line",
    data: {
        labels: ["اسفند", "بهمن", "دی", "آذر", "آبان", "مهر", "شهریور", "مرداد", "تیر", "خرداد", "اردیبهشت", "فروردین"],
        datasets: [
            {
                label: "فروش",
                data: [10, 40, 38, 35, 50, 55, 40, 43, 60, 50, 60, 70],
                backgroundColor: "rgba(56, 127, 12, 0.05)",
                borderColor: "#38BB0C",
                pointBorderColor: "#ffffff",
                pointBackgroundColor: "#38BB0C",
                pointBorderWidth: 2,
                pointRadius: 4,
            },
        ],
    },
    options: {
        tooltips: { xPadding: 12, yPadding: 12, backgroundColor: "#2e3d62" },
        legend: { display: !1, tooltips: { displayColors: !1 } },
        scales: { xAxes: [{ display: !0, gridLines: { color: "#eee" } }], yAxes: [{ display: !0, gridLines: { color: "#eee" }, ticks: { fontSize: 14 } }] },
    },
});
