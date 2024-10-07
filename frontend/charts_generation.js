// Archivo: frontend/chart_generation.js

// Importamos Chart.js para crear gráficos interactivos
import Chart from 'chart.js/auto';

// Función para generar gráficos interactivos
export function generateCharts(data) {
    // Verificamos si el contenedor del gráfico existe
    const ctx = document.getElementById('chart');
    if (!ctx) {
        console.error('No se pudo encontrar el contenedor del gráfico');
        return;
    }

    // Creamos un nuevo gráfico de barras con los datos
    const chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.labels,
            datasets: [
                {
                    label: 'Experimental Data',
                    data: data.values,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1,
                },
            ],
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Results of Space Experiments',
                },
            },
        },
    });
}

// Conectar al botón 'Start Visualizing'
document.getElementById('start-visualizing-button').addEventListener('click', () => {
    // Fetch data desde el backend y crear el gráfico
    fetch('/api/get_processed_data')
        .then((response) => response.json())
        .then((data) => {
            generateCharts(data);
        })
        .catch((error) => {
            console.error('Error al obtener los datos procesados:', error);
        });
});