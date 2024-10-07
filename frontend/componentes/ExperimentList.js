// Archivo ExperimentList.js para el proyecto Biospace

import React from 'react';

// Componente para mostrar la lista de experimentos
const ExperimentList = ({ experiments }) => {
    return (
        <section id="experiments" className="container my-5">
            <h2 className="text-center mb-4">Biological Experiments in Space</h2>
            <div className="row">
                {experiments.length > 0 ? (
                    experiments.map((experiment, index) => (
                        <div key={index} className="col-md-6">
                            <h3>{experiment.title || 'No Title Available'}</h3>
                            <p>{experiment.description || 'No Description Available'}</p>
                        </div>
                    ))
                ) : (
                    <p className="text-center">No experiments available.</p>
                )}
            </div>
        </section>
    );
};

export default ExperimentList;