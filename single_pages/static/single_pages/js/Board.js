document.addEventListener('DOMContentLoaded', function () {
    // 차트 데이터
    
    var chartList = []
    var color_list = ['rgba(255, 0, 0, 0.2)','rgba(0, 255, 0, 0.2)','rgba(0, 0, 255, 0.2)','rgba(255, 165, 0, 0.2)','rgba(128, 0, 128, 0.2)']
    var border_color_list = ['rgba(255, 0, 0, 1)','rgba(0, 255, 0, 1)','rgba(0, 0, 255, 1)','rgba(255, 165, 0, 1)','rgba(128, 0, 128, 1)']
    for (let i = 0; i < chart_title.length; i++) {
        chartList.push({
                    label: chart_title[i],
                    data: datas[i],
                    backgroundColor: color_list[i],
                    borderColor: border_color_list[i],
                    borderWidth: 1
                });
    }
    var chartData = {
        labels: labels,
        datasets: chartList
    };

    // 캔버스 선택
    var ctx = document.getElementById('myChart').getContext('2d');

    // 차트 생성
    var myChart = new Chart(ctx, {
        type: 'line',  // 차트의 종류 (막대 그래프)
        data: chartData,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            },
            maintainAspectRatio: false,  // 가로 및 세로 비율 고정 해제
            responsive: true  // 차트가 부모 컨테이너에 맞게 반응하도록 설정
        }
    });


    for(index in one_chart_data[0]){
        // 버튼을 생성하고 추가할 div 요소를 가져옵니다.
        var buttonContainer = document.getElementById("btn1");

        // 버튼 엘리먼트를 생성합니다.
        var addButton = document.createElement("button");

        // 버튼에 텍스트를 추가합니다.
        addButton.innerText = one_chart_data[0][index];
        addButton.className = 'chart-button';
        addButton.setAttribute('data-index', index);
        buttonContainer.appendChild(addButton)
    };
    for(index in one_chart_data[1]){
        // 버튼을 생성하고 추가할 div 요소를 가져옵니다.
        var buttonContainer = document.getElementById("btn2");

        // 버튼 엘리먼트를 생성합니다.
        var addButton = document.createElement("button");

        // 버튼에 텍스트를 추가합니다.
        addButton.innerText = one_chart_data[1][index];
        addButton.className = 'label-button';
        addButton.setAttribute('data-index', Number(index)+2);
        buttonContainer.appendChild(addButton)
    };
        
    // <button class="label-button" data-index="{{ forloop.counter0 }}">{{ label }}</button>
    // 원 그래프 생성
    var ctx = document.getElementById('myDynamicPieChart').getContext('2d');
    var myPieChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: one_chart_data[2][0],
            datasets: [{
                data: one_chart_data[2][1][0],  // 초기 데이터 사용
                backgroundColor: ['rgb(172,182,189)', 'rgb(104,146,165)'],  // 색상 설정
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
        }
    });
    let first_num = 2
    let second_num = 0
    // 버튼에 이벤트 리스너 추가
    var buttons = document.querySelectorAll('.chart-button');
    buttons.forEach(function (button) {
        button.addEventListener('click', function () {
            var index = this.dataset.index;
            updatePieChart(index);
        });
    });
    var buttons2 = document.querySelectorAll('.label-button');
    buttons2.forEach(function (button) {
        button.addEventListener('click', function () {
            var index = this.dataset.index;
            updatePielabel(index);
        });
    });

    function updatePieChart(index) {
        myPieChart.data.datasets[0].data = one_chart_data[first_num][1][index];
        second_num = index
        myPieChart.update();
    }
    function updatePielabel(index) {
        myPieChart.data.labels = one_chart_data[index][0];
        myPieChart.data.datasets[0].data = one_chart_data[index][1][0];
        first_num = index
        
        myPieChart.update();
    }

});