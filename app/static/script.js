var ctxUSDEUR = document.getElementById("myChartUSDEUR");

var myChartUSDEUR = new Chart(ctxUSDEUR, {
  type: 'line',
  data: {
    labels: years,
    datasets: [
      {
        data: USD_EUR_data,
        label: "Actual",
        borderColor: "#c69486",
        fill: false,
        pointHoverBorderColor: "#ff0000"

      },
      {
        data: USD_EUR_predicted,
        label: "Predicted",
        borderColor: "#fff",
        fill: false,
        pointHoverBorderColor: "#ff0000"
      }
    ]
  },
  options: {
        legend: {
            labels: {
                fontColor: "#b3b3b3",
                fontSize: 14
            }
        },
        scales: {
            xAxes: [{
                gridLines: {
                    fontColor: "#fff",
                    zeroLineColor: "#fff",
                },
                ticks: {
                  fontColor: "#fff", // this here
                },
            }],
            yAxes: [{
                gridLines: {
                    fontColor: "#fff",
                    zeroLineColor: "#fff",
                },
                ticks: {
                  fontColor: "#fff", // this here
                },
            }],
        }
    }
});

var ctxEURUSD = document.getElementById("myChartEURUSD");

var myChartEURUSD = new Chart(ctxEURUSD, {
  type: 'line',
  data: {
    labels: years,
    datasets: [
      {
        data: EUR_USD_data,
        label: "Actual",
        borderColor: "#c69486",
        fill: false,
        pointHoverBorderColor: "#ff0000"

      },
      {
        data: EUR_USD_predicted,
        label: "Predicted",
        borderColor: "#fff",
        fill: false,
        pointHoverBorderColor: "#ff0000"
      }
    ]
  },
  options: {
        legend: {
            labels: {
                fontColor: "#b3b3b3",
                fontSize: 14
            }
        },
        scales: {
            xAxes: [{
                gridLines: {
                    fontColor: "#fff",
                    zeroLineColor: "#fff",
                },
                ticks: {
                  fontColor: "#fff", // this here
                },
            }],
            yAxes: [{
                gridLines: {
                    fontColor: "#fff",
                    zeroLineColor: "#fff",
                },
                ticks: {
                  fontColor: "#fff", // this here
                },
            }],
        }
    }
});


var ctxUSDGBP = document.getElementById("myChartUSDGBP");

var myChartUSDGBP = new Chart(ctxUSDGBP, {
  type: 'line',
  data: {
    labels: years,
    datasets: [
      {
        data: USD_GBP_data,
        label: "Actual",
        borderColor: "#c69486",
        fill: false,
        pointHoverBorderColor: "#ff0000"

      },
      {
        data: USD_GBP_predicted,
        label: "Predicted",
        borderColor: "#fff",
        fill: false,
        pointHoverBorderColor: "#ff0000"
      }
    ]
  },
  options: {
        legend: {
            labels: {
                fontColor: "#b3b3b3",
                fontSize: 14
            }
        },
        scales: {
            xAxes: [{
                gridLines: {
                    fontColor: "#fff",
                    zeroLineColor: "#fff",
                },
                ticks: {
                  fontColor: "#fff", // this here
                },
            }],
            yAxes: [{
                gridLines: {
                    fontColor: "#fff",
                    zeroLineColor: "#fff",
                },
                ticks: {
                  fontColor: "#fff", // this here
                },
            }],
        }
    }
});

var ctxGBPUSD = document.getElementById("myChartGBPUSD");

var myChartGBPUSD = new Chart(ctxGBPUSD, {
  type: 'line',
  data: {
    labels: years,
    datasets: [
      {
        data: GBP_USD_data,
        label: "Actual",
        borderColor: "#c69486",
        fill: false,
        pointHoverBorderColor: "#ff0000"

      },
      {
        data: GBP_USD_predicted,
        label: "Predicted",
        borderColor: "#fff",
        fill: false,
        pointHoverBorderColor: "#ff0000"
      }
    ]
  },
  options: {
        legend: {
            labels: {
                fontColor: "#b3b3b3",
                fontSize: 14
            }
        },
        scales: {
            xAxes: [{
                gridLines: {
                    fontColor: "#fff",
                    zeroLineColor: "#fff",
                },
                ticks: {
                  fontColor: "#fff", // this here
                },
            }],
            yAxes: [{
                gridLines: {
                    fontColor: "#fff",
                    zeroLineColor: "#fff",
                },
                ticks: {
                  fontColor: "#fff", // this here
                },
            }],
        }
    }
});


var ctxGBPEUR = document.getElementById("myChartGBPEUR");

var myChartGBPEUR = new Chart(ctxGBPEUR, {
  type: 'line',
  data: {
    labels: years,
    datasets: [
      {
        data: GBP_EUR_data,
        label: "Actual",
        borderColor: "#c69486",
        fill: false,
        pointHoverBorderColor: "#ff0000"

      },
      {
        data: GBP_EUR_predicted,
        label: "Predicted",
        borderColor: "#fff",
        fill: false,
        pointHoverBorderColor: "#ff0000"
      }
    ]
  },
  options: {
        legend: {
            labels: {
                fontColor: "#b3b3b3",
                fontSize: 14
            }
        },
        scales: {
            xAxes: [{
                gridLines: {
                    fontColor: "#fff",
                    zeroLineColor: "#fff",
                },
                ticks: {
                  fontColor: "#fff", // this here
                },
            }],
            yAxes: [{
                gridLines: {
                    fontColor: "#fff",
                    zeroLineColor: "#fff",
                },
                ticks: {
                  fontColor: "#fff", // this here
                },
            }],
        }
    }
});

var ctxEURGBP = document.getElementById("myChartEURGBP");

var myChartEURGBP = new Chart(ctxEURGBP, {
  type: 'line',
  data: {
    labels: years,
    datasets: [
      {
        data: EUR_GBP_data,
        label: "Actual",
        borderColor: "#c69486",
        fill: false,
        pointHoverBorderColor: "#ff0000"

      },
      {
        data: EUR_GBP_predicted,
        label: "Predicted",
        borderColor: "#fff",
        fill: false,
        pointHoverBorderColor: "#ff0000"
      }
    ]
  },
  options: {
        legend: {
            labels: {
                fontColor: "#b3b3b3",
                fontSize: 14
            }
        },
        scales: {
            xAxes: [{
                gridLines: {
                    fontColor: "#fff",
                    zeroLineColor: "#fff",
                },
                ticks: {
                  fontColor: "#fff", // this here
                },
            }],
            yAxes: [{
                gridLines: {
                    fontColor: "#fff",
                    zeroLineColor: "#fff",
                },
                ticks: {
                  fontColor: "#fff", // this here
                },
            }],
        }
    }
});

var empty = [];
var ctxEmpty = document.getElementById("myChartEmpty");
var myChartEmpty = new Chart(ctxEmpty, {
  type: 'line',
  data: {
    labels: years,
    datasets: [
      {
        data: empty,
        borderColor: "#c69486",
        fill: false,
        pointHoverBorderColor: "#ff0000"

      }
    ]
  },
  options: {
        legend: {
            labels: {
                fontColor: "#b3b3b3",
                fontSize: 14
            }
        },
        scales: {
            xAxes: [{
                gridLines: {
                    fontColor: "#000",
                    zeroLineColor: "#000",
                },
                ticks: {
                  fontColor: "#000", // this here
                },
            }],
            yAxes: [{
                gridLines: {
                    fontColor: "#000",
                    zeroLineColor: "#000",
                },
                ticks: {
                  fontColor: "#000", // this here
                },
            }],
        }
    }
});

function cycle(to_show1, to_show2) {
  if (to_show1 == "empty" || to_show2 == "empty" || to_show1 == to_show2) {
    $(".project").hide();
    $(".chartTest").show();
  }
  $(".project").hide();
  $("." + to_show1 + to_show2).show();
  $("." + to_show1 + to_show2).css("opacity", "0");
  $("." + to_show1 + to_show2).animate({opacity: 1}, 900);
};
cycle();

$("select#currency1").change(
  function(){
  var currency1 = $(this).val();
  $("select#currency2").change(function(){
    var currency2 = $(this).val();
    $(".chartTest").hide();
    cycle(currency1, currency2);
   })
})

$("select#currency2").change(
  function(){
  var currency2 = $(this).val();
  $("select#currency1").change(function(){
    var currency1 = $(this).val();
    $(".chartTest").hide();
    cycle(currency1, currency2);
   })
})
