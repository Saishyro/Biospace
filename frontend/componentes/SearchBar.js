// Archivo SearchBar.js para el proyecto Biospace

import React, { useState } from 'react';

// Componente de barra de búsqueda
const SearchBar = ({ onSearch }) => {
    const [query, setQuery] = useState('');

    // Manejar el cambio en el campo de búsqueda
    const handleInputChange = (event) => {
        setQuery(event.target.value);
    };

    // Manejar el envío del formulario de búsqueda
    const handleSearch = (event) => {
        event.preventDefault();
        if (query.trim()) {
            onSearch(query);
        }
    };

    return (
        <div className="container my-5">
            <form onSubmit={handleSearch} className="d-flex justify-content-center">
                <input
                    type="text"
                    className="form-control me-2"
                    placeholder="Search for experiments..."
                    value={query}
                    onChange={handleInputChange}
                />
                <button type="submit" className="btn btn-primary">Search</button>
            </form>
        </div>
    );
};

export default SearchBar;