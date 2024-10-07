import fetch from 'node-fetch';
import Chart from 'chart.js/auto';
import { createElement } from './domUtils'; // Asumiendo que hay una utilidad para crear elementos del DOM

// Función completa de visualización para obtener y mostrar datos desde la API de NASA OSDR
export async function fetchExperimentData(experimentId) {
    try {
        const endpoint = `https://osdr.nasa.gov/osdr/data/osd/files/${experimentId}`;
        const response = await fetch(endpoint);
        if (!response.ok) {
            throw new Error('Error al obtener los datos del experimento');
        }
        const data = await response.json();
        
        // Registrar la respuesta para propósitos de depuración
        console.log('Datos del Experimento:', data);
        
        // Extrayendo campos útiles de la respuesta de datos
        const experimentFiles = data?.studies?.[`OSD-${experimentId}`]?.archivos_de_estudio || [];
        
        // Lógica de ejemplo para analizar y mostrar los datos
        const container = document.getElementById('visualization-container');
        container.innerHTML = '';

        experimentFiles.forEach((file) => {
            const fileUrl = `https://osdr.nasa.gov${file.url_remota}`;
            const fileElement = createElement('div', { className: 'file-info' }, [
                createElement('p', {}, `Archivo: ${file.nombre_de_archivo}`),
                createElement('a', { href: fileUrl, target: '_blank' }, 'Descargar Archivo')
            ]);
            container.appendChild(fileElement);
        });

        // Ejemplo de visualización de gráficos usando Chart.js
        const labels = experimentFiles.map((file) => file.nombre_de_archivo);
        const fileSizes = experimentFiles.map((file) => file.tamaño_de_archivo);

        const ctx = document.getElementById('chart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Tamaños de Archivos (bytes)',
                    data: fileSizes,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
        
    } catch (error) {
        console.error('Error:', error.message);
    }
}

// La lógica anterior ahora incluye una visualización básica usando Chart.js para crear un gráfico de barras
// que muestra los tamaños de los archivos para el experimento dado. Se pueden agregar más personalizaciones según sea necesario.