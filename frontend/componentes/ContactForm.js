// Archivo ContactForm.js para el proyecto Biospace

import React, { useState } from 'react';

// Componente del formulario de contacto
const ContactForm = () => {
    const [formData, setFormData] = useState({ name: '', email: '', message: '' });
    const [submitted, setSubmitted] = useState(false);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Lógica para enviar el formulario (simulada en este caso)
        console.log('Formulario enviado:', formData);
        setSubmitted(true);
    };

    return (
        <section id="contact" className="bg-dark text-white py-5">
            <div className="container">
                <h2 className="text-center mb-4">Contact Us</h2>
                {submitted ? (
                    <p className="text-center">Thank you for your message! We will get back to you soon.</p>
                ) : (
                    <div className="row justify-content-center">
                        <div className="col-md-6">
                            <form onSubmit={handleSubmit}>
                                <div className="mb-3">
                                    <label htmlFor="name" className="form-label">Name</label>
                                    <input
                                        type="text"
                                        className="form-control"
                                        id="name"
                                        name="name"
                                        value={formData.name}
                                        onChange={handleChange}
                                        required
                                    />
                                </div>
                                <div className="mb-3">
                                    <label htmlFor="email" className="form-label">Email</label>
                                    <input
                                        type="email"
                                        className="form-control"
                                        id="email"
                                        name="email"
                                        value={formData.email}
                                        onChange={handleChange}
                                        required
                                    />
                                </div>
                                <div className="mb-3">
                                    <label htmlFor="message" className="form-label">Message</label>
                                    <textarea
                                        className="form-control"
                                        id="message"
                                        name="message"
                                        rows="3"
                                        value={formData.message}
                                        onChange={handleChange}
                                        required
                                    />
                                </div>
                                <button type="submit" className="btn btn-primary">Send Message</button>
                            </form>
                        </div>
                    </div>
                )}
            </div>
        </section>
    );
};

export default ContactForm;