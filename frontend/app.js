// Asegurarse de que el DOM esté completamente cargado antes de añadir los event listeners
document.addEventListener("DOMContentLoaded", function () {

    // Añadir un event listener al formulario de búsqueda
    const searchForm = document.getElementById("search-form");
    searchForm.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevenir la recarga de la página

        // Obtener el valor del input del experimento
        const experimentId = document.getElementById("search-input").value.trim();

        // Validar que se haya ingresado un ID de experimento
        if (experimentId === "") {
            alert("Please enter a valid experiment name or keyword.");
            return;
        }

        // Realizar la solicitud fetch hacia el backend Flask para obtener datos del experimento
        fetch(`/api/search_experiment/${experimentId}`)
            .then(response => response.json())
            .then(data => {
                // Manejo de los datos obtenidos
                if (data.error) {
                    alert(data.error); // Mostrar mensaje de error si la API devuelve un error
                } else {
                    console.log(data);
                    // Mostrar los datos obtenidos en el frontend
                    displayExperimentData(data);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert("There was an issue fetching the experiment details. Please try again.");
            });
    });

    // Función para mostrar los datos del experimento en el DOM
    function displayExperimentData(data) {
        const resultsContainer = document.getElementById("search-results");
        resultsContainer.innerHTML = ""; // Limpiar resultados anteriores

        // Ejemplo de cómo podrías mostrar los resultados
        if (data.studies) {
            for (const studyId in data.studies) {
                const study = data.studies[studyId];
                const studyElement = document.createElement("div");
                studyElement.classList.add("experiment-result", "card", "p-3", "mb-3");

                studyElement.innerHTML = `
                    <h3>Study ID: ${studyId}</h3>
                    <p>File Count: ${study.file_count}</p>
                    <p>Files:</p>
                    <ul>
                        ${study.study_files.map(file => `
                            <li>
                                <strong>${file.file_name}</strong> - ${file.organization}
                                <br>
                                <a href="https://osdr.nasa.gov${file.remote_url}" target="_blank">Download</a>
                            </li>
                        `).join('')}
                    </ul>
                `;

                resultsContainer.appendChild(studyElement);
            }
        } else {
            resultsContainer.innerHTML = "<p>No data found for the specified experiment ID.</p>";
        }
    }
});
