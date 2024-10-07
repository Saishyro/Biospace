// Archivo Navbar.js para el proyecto Biospace

import React from 'react';
import { Navbar, Nav, Container } from 'react-bootstrap';

// Componente de barra de navegación
const NavbarComponent = () => {
    return (
        <Navbar bg="light" expand="lg" className="shadow-sm">
            <Container>
                <Navbar.Brand href="#">Biospace</Navbar.Brand>
                <Navbar.Toggle aria-controls="navbarNav" />
                <Navbar.Collapse id="navbarNav">
                    <Nav className="ms-auto">
                        <Nav.Link href="#experiments">Experiments</Nav.Link>
                        <Nav.Link href="#data-visualization">Data Visualization</Nav.Link>
                        <Nav.Link href="#about">About</Nav.Link>
                        <Nav.Link href="#contact">Contact</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
};

export default NavbarComponent;