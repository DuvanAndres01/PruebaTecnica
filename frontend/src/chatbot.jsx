import React, { useState, useEffect, useRef } from "react";
import axios from "axios";

const Chatbot = () => {
  const [mensaje, setMensaje] = useState("");
  const [historial, setHistorial] = useState([]);
  const chatRef = useRef(null);

  useEffect(() => {
    if (chatRef.current) {
      chatRef.current.scrollIntoView({ behavior: "smooth" });
    }
  }, [historial]);

  const enviarMensaje = async () => {
    if (!mensaje.trim()) return;

    const nuevoMensaje = { pregunta: mensaje, respuesta: "" };
    setHistorial((prev) => [...prev, nuevoMensaje]);
    setMensaje("");

    try {
      const response = await axios.post("http://127.0.0.1:8000/api/chatbot/", { pregunta: mensaje });

      setHistorial((prevHistorial) => {
        const updatedHistorial = [...prevHistorial];
        updatedHistorial[updatedHistorial.length - 1] = {
          ...updatedHistorial[updatedHistorial.length - 1],
          respuesta: response.data.respuesta || "No tengo una respuesta.",
        };
        return updatedHistorial;
      });
    } catch (error) {
      console.error("Error al enviar la pregunta:", error);
    }
  };

  return (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center", height: "100vh", backgroundColor: "#1e1e2e" }}>
      <h1 style={{ color: "white" }}>ChatBot de DevSpark</h1>
      <div style={{ width: "400px", backgroundColor: "#2e2e3e", padding: "20px", borderRadius: "10px", color: "white" }}>
        {historial.map((item, index) => (
          <div key={index} style={{ marginBottom: "10px" }}>
            <strong>Tú:</strong> {item.pregunta}
            <br />
            <strong>ChatBot:</strong> {item.respuesta}
          </div>
        ))}
        <div ref={chatRef}></div>
      </div>
      <input value={mensaje} onChange={(e) => setMensaje(e.target.value)} placeholder="Escribe tu pregunta..." />
      <button onClick={enviarMensaje}>Enviar</button>
    </div>
  );
};

export default Chatbot;
