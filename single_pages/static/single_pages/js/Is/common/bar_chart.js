document.addEventListener('DOMContentLoaded', function () {
    // 차트 데이터
    var chartData = {
        labels: labels,
        datasets: [{
            label: chart_title,
            data: datas,
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }]
    };

    // 캔버스 선택
    var ctx = document.getElementById('myChart').getContext('2d');

    // 차트 생성
    var myChart = new Chart(ctx, {
        type: 'bar',  // 차트의 종류 (막대 그래프)
        data: chartData,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});