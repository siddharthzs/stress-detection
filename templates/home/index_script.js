var visible = 0;
var allData;
const eda_xlabel = [];
const eda_ylabel = [];
const bvp_xlabel = [];
const bvp_ylabel = [];
const temp_xlabel = [];
const temp_ylabel = [];


function toggleToken() {
    var ele = document.getElementById('token');
    if (visible == 0) {
        ele.style.visibility = 'visible';
        visible = 1;
    }
    else {
        ele.style.visibility = 'hidden';
        visible = 0;
    }
}


function setBubble(re, str) {
    const rangeDiv = document.querySelector('.range-wrap');
    const range = rangeDiv.querySelector(".range");
    const bubble = rangeDiv.querySelector(".bubble");
    const val = re;
    const newVal = Number((val * 100) / 2);
    bubble.innerHTML = str;
    if (re == 2)
        bubble.style.left = `calc(${newVal}% - 6%)`;
    if (re == 1)
        bubble.style.left = `calc(${newVal}%)`;
    if (re == 0)
        bubble.style.left = `calc(${newVal}% + 6%)`;
}



async function getData(url, ch) {

    const response = await fetch(url);
    const data = await response.text();
    const table = data.split("\n").slice(1);
    // console.log(table.length);
    for (var i = 0; i < table.length - 1; i++) {
        const columns = table[i].split(',');
        const seconds = columns[0];
        const frequncy = columns[1];

        if (ch == 'eda') {
            eda_xlabel.push(seconds);
            if (frequncy == '')
                eda_ylabel.push(null);
            else
                eda_ylabel.push(frequncy);
        }
        if (ch == 'bvp') {
            bvp_xlabel.push(seconds);
            if (frequncy == '')
                bvp_ylabel.push(null);
            else
                bvp_ylabel.push(frequncy);
        }
    }
}






async function getEdaChart(id) {
    while (eda_xlabel.length > 0) {
        eda_xlabel.pop();
        eda_ylabel.pop();
    }
    var url = `https://raw.githubusercontent.com/siddharthzs/stress_management/master/eda/testcaseno_${id}.csv`;
    await getData(url, "eda");


    var chartColor = "#ffffff";

    var ctx = document.getElementById('myEdaChart').getContext('2d');
    var gradientStroke = ctx.createLinearGradient(0, 230, 0, 50);

    gradientStroke.addColorStop(1, 'rgba(72,72,176,0.2)');
    gradientStroke.addColorStop(0.2, 'rgba(72,72,176,0.0)');
    gradientStroke.addColorStop(0, 'rgb(119, 52, 169,0)'); //purple colors


    var myChart = new Chart(ctx, {

        type: 'line',
        responsive: true,
        data: {
            labels: eda_xlabel,
            datasets: [{
                label: 'Electrodermal Activity',
                data: eda_ylabel,
                spanGaps: true,
                fill: true,
                backgroundColor: gradientStroke,
                borderColor: '#d048b6',
                borderWidth: 2,
                borderDash: [],
                borderDashOffset: 0.0,
                pointBackgroundColor: '#d048b6',
                pointBorderColor: 'rgba(255,255,255,0)',
                pointHoverBackgroundColor: '#d048b6',
                pointBorderWidth: 20,
                pointHoverRadius: 4,
                pointHoverBorderWidth: 15,
                pointRadius: 4,
            }]
        },
        options: {
            maintainAspectRatio: false,
            legend: {
                display: false,
            },
            tooltips: {
                mode: 'point',
                xPadding: 12,
                backgroundColor: '#f5f5f5',
                titleFontColor: '#333',
                bodyFontColor: '#666',
                bodySpacing: 4,

            },
            response: true,
            scales: {
                yAxes: [{
                    barPercentage: 1.6,
                    gridLines: {
                        drawBorder: false,
                        color: 'rgba(29,140,248,0.0)',
                    },
                    ticks: {
                        fontColor: "#9a9a9a"
                    }
                }],

                xAxes: [{
                    barPercentage: 1.6,
                    gridLines: {
                        drawBorder: false,
                        color: 'rgba(225,78,202,0.1)',
                    },
                    ticks: {

                        fontColor: "#9a9a9a",
                        beginAtZero: true,
                        min: 0

                    }
                }]
            },
            legend: {
                display: true,
                fontColor: "#9a9a9a",
                labels: {
                    fontColor: "#9a9a9a",
                    fontSize: 12
                }

            },
        }
    });
}


async function getBvpChart(id) {
    while (bvp_xlabel.length > 0) {
        bvp_xlabel.pop();
        bvp_ylabel.pop();
    }
    var url = `https://raw.githubusercontent.com/siddharthzs/stress_management/master/bvp/testcaseno_${id}.csv`;
    await getData(url, "bvp");
    var gradientChart = {

        maintainAspectRatio: false,
        legend: {
            display: true
        },

        tooltips: {
            backgroundColor: '#f5f5f5',
            titleFontColor: '#333',
            bodyFontColor: '#666',
            bodySpacing: 4,
            xPadding: 12,
            mode: "point",


        },
        responsive: true,
        scales: {
            yAxes: [{
                barPercentage: 1,
                gridLines: {
                    drawBorder: false,
                    color: 'rgba(29,140,248,0.0)',
                },
                ticks: {
                    fontColor: "#9e9e9e"
                }
            }],

            xAxes: [{
                barPercentage: 1.1,
                gridLines: {
                    display: false,
                },
                ticks: {
                    fontColor: "#9e9e9e"
                }
            }]
        }
    };

    var ctx = document.getElementById('myBvpChart').getContext('2d');

    var gradientStroke = ctx.createLinearGradient(0, 230, 0, 50);
    gradientStroke.addColorStop(1, 'rgba(66,134,121,0.15)');
    gradientStroke.addColorStop(0.4, 'rgba(66,134,121,0.0)'); //green colors
    gradientStroke.addColorStop(0, 'rgba(66,134,121,0)'); //green colors

    var myChart = new Chart(ctx, {

        type: 'line',
        data: {
            labels: bvp_xlabel,
            datasets: [{
                label: 'Blood Volume Pulse',
                spanGaps: true,
                data: bvp_ylabel,
                fill: true,
                backgroundColor: gradientStroke,
                borderColor: '#00d6b4',
                borderWidth: 2,
                borderDash: [],
                borderDashOffset: 0.0,
                pointBackgroundColor: '#00d6b4',
                pointBorderColor: 'rgba(255,255,255,0)',
                pointHoverBackgroundColor: '#00d6b4',
                pointBorderWidth: 5,
                pointHoverRadius: 1,
                pointHoverBorderWidth: 5,
                pointRadius: 2,
            }]
        },
        options: gradientChart,
        legend: {
            display: true,
            fontColor: "#fff",
            labels: {
                fontColor: "white",
                fontSize: 12
            }

        }


    });

}

async function resultChart(allData) {
    var ctx = document.getElementById('myResultChart').getContext('2d');
    var myPieChart = new Chart(ctx, {
        type: 'pie',
        data: {
            datasets: [{

                data: allData,
                backgroundColor: [
                    "#3498db",
                    "#00d6b4",
                    "#d048b6"
                ]

            }],
            labels: [
                'Amusement' + ' (' + allData[0].toFixed(2) + ')',
                'Baseline' + ' (' + allData[1].toFixed(2) + ')',
                'Stress' + ' (' + allData[2].toFixed(2) + ')'
            ]
        },
        options: {
            title: {
                display: true,
                text: 'Result',
                fontSize: 20,
                fontColor: '#fff',

            },
            legend: {
                display: true,
                position: "left",
                fontColor: "#fff",
                labels: {
                    fontColor: "white",
                    fontSize: 12
                }

            },
        }
    });

}


async function predict() {
    var id = document.getElementById("mytext").value;
    if (id == '')
        id = 1;
    var re = document.getElementById("result");
    var url = `http://127.0.0.1:8000/api/model/${id}/predict/{{token}}/`;
    console.log(url);
    getEdaChart(id);
    getBvpChart(id);
    fetch(url)
        .then((resp) => resp.json())
        .then(function (data) {
            re.innerHTML = JSON.stringify(data);
            var allData = [];
            for (var i = 0; i < data.gradBoost.probability.length; i++) {
                allData.push(data.gradBoost.probability[i] * 100);

            }
            var str = '';
            var reNo = data.gradBoost.result[0];
            if (reNo == 0)
                str = 'Amusemed!';
            else if (reNo == 1)
                str = 'Neutral';
            else
                str = 'Stressed!';

            setBubble(reNo, str);
            resultChart(allData);


        });
}







var textareas = document.getElementsByClassName('Box');
var count = textareas.length;
for (var i = 0; i < count; i++) {
    var flag = 0;

    textareas[i].onkeydown = function (e) {

        if (e.keyCode == 9 || e.which == 9) {
            e.preventDefault();
            document.execCommand("insertHTML", false, "&nbsp;&nbsp;&nbsp;&nbsp;");

        }
        if (e.keyCode == 186 || e.which == 186) { // for colon :

        }
        if (e.keyCode == 222 || e.which == 222) {// for quote "'
            document.execCommand("foreColor", false, "#e04ecb");
            flag++;
        }
        else if (flag >= 2) {
            document.execCommand("foreColor", false, "#fff");
            flag = 0;
        }
    }
}








function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');


var predata = `<pre>{

"BVP_mean" : -0.181673262,
"BVP_std" : 107.648359,
"EDA_phasic_mean" : 1.824289,
"EDA_phasic_min" : 0.367977083,
"EDA_smna_min" : 5.22965803e-08,
"EDA_tonic_mean" : 1.23216412,
"Resp_mean" : 0.148183977,
"Resp_std" : 2.93561681,
"TEMP_mean" : 35.8170909,
"TEMP_std" : 0.0126739141,
"TEMP_slope" : -0.000169059802,
"BVP_peak_freq" : 0.13566987,
"age" : 27.0,
"height" : 175.0,
"weight" : 80.0
}</pre>`;

document.getElementsByClassName('inputBox')[0].innerHTML = predata;
document.body.setAttribute("spellcheck", false);


async function callapi() {
    var url = "{% url 'web-model-api' token %}";
    var re = document.getElementById('inputapi').textContent;
    re = re.replace("<pre>", "");
    re = re.replace("</pre>", "");
    let response = await fetch(url, {
        method: 'POST',
        mode: 'cors',
        headers: {
            "Content-type": "application/json",
            "Accept": "application/json",
            "X-CSRFToken": csrftoken
        },
        body: re
    });
    let result = await response.json();
    var target = document.getElementById('outputapi');
    var re = JSON.stringify(result);
    // var dup = re;
    // re = re.replaceAll("{","{</br>");
    // re = re.replaceAll(",",",");
    // re = re.replaceAll("}","</br>}");
    // target.innerHTML = re;

    // target.innerText+="\n\n"+dup;
    var dup = "";
    var tcnt = 1;
    for (var i = 0; i < re.length - 1; i++) {
        if (re[i] == "{") {
            tcnt++;
            var space = "&nbsp;&nbsp;";
            for (var j = 0; j < tcnt; j++)
                space += space;
            dup += "{" + "<br>" + space;
        }
        else if (re[i] == "}") {
            tcnt--;
            var space = "&nbsp;&nbsp;";
            for (var j = 0; j < tcnt; j++)
                space += space;
            dup += "<br>" + space + "}";
        }
        else if (re[i] == "," && re[i + 1] == '\"') {
            var space = "&nbsp;&nbsp;";
            for (var j = 0; j < tcnt; j++)
                space += space;
            dup += re[i] + "<br>" + space;
        }
        else
            dup += re[i];

    }
    dup += "<br>}"
    target.innerHTML = dup;

}










