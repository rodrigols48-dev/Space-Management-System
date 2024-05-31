document.addEventListener("DOMContentLoaded", function() {
    const missionsCtx = document.getElementById('missionsChart').getContext('2d');
    const satellitesCtx = document.getElementById('satellitesChart').getContext('2d');

    const missionsChart = new Chart(missionsCtx, {
        type: 'bar',
        data: {
            labels: ['2020', '2021', '2022', '2023', '2024'],
            datasets: [{
                label: 'Missões',
                data: [5, 10, 15, 20, 25],
                backgroundColor: 'rgba(0, 123, 255, 0.5)',
                borderColor: 'rgba(0, 123, 255, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    const satellitesChart = new Chart(satellitesCtx, {
        type: 'pie',
        data: {
            labels: ['Operacional', 'Manutenção', 'Desativado'],
            datasets: [{
                label: 'Status dos Satélites',
                data: [10, 2, 1],
                backgroundColor: [
                    'rgba(0, 255, 0, 0.5)',
                    'rgba(255, 255, 0, 0.5)',
                    'rgba(255, 0, 0, 0.5)'
                ],
                borderColor: [
                    'rgba(0, 255, 0, 1)',
                    'rgba(255, 255, 0, 1)',
                    'rgba(255, 0, 0, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true
        }
    });
});
