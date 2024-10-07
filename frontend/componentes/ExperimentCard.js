// Archivo ExperimentCard.js para el proyecto Biospace

import React from 'react';

// Componente para mostrar una tarjeta de experimento
const ExperimentCard = ({ experiment }) => {
    return (
        <div className="card mb-4">
            <div className="card-body">
                <h5 className="card-title">{experiment.title || 'No Title Available'}</h5>
                <p className="card-text">{experiment.description || 'No Description Available'}</p>
            </div>
        </div>
    );
};

export default ExperimentCard;