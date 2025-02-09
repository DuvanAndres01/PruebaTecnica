import React, { useState, useRef, useEffect } from "react";
import axios from "axios";

function App() {
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
      const response = await axios.post("http://127.0.0.1:8000/api/chatbot/", {
        pregunta: mensaje,
      });

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
      setHistorial((prevHistorial) => {
        const updatedHistorial = [...prevHistorial];
        updatedHistorial[updatedHistorial.length - 1] = {
          ...updatedHistorial[updatedHistorial.length - 1],
          respuesta: "Hubo un error al procesar tu pregunta.",
        };
        return updatedHistorial;
      });
    }
  };

  return (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100vh", backgroundColor: "#1e1e2e" }}>
      <div style={{ width: "100%", maxWidth: "800px", backgroundColor: "#2e2e3e", padding: "20px", borderRadius: "10px", boxShadow: "0 4px 10px rgba(0, 0, 0, 0.3)", display: "flex", flexDirection: "column" }}>
        <h1 style={{ textAlign: "center", marginBottom: "15px", fontSize: "2rem", fontWeight: "bold", color: "#ffffff", textTransform: "uppercase", letterSpacing: "2px" }}>ChatBot de DevSpark</h1>
        <div style={{ flexGrow: 1, overflowY: "auto", maxHeight: "600px", padding: "50px", border: "1px solid #444", borderRadius: "5px", backgroundColor: "#3e3e4e", color: "#ffffff", display: "flex", flexDirection: "column" }}>
          {historial.map((item, index) => (
            <div key={index} style={{ display: "flex", flexDirection: "column", marginBottom: "10px" }}>
              <div style={{
                alignSelf: "flex-end",
                padding: "10px",
                backgroundColor: "#007bff",
                borderRadius: "10px",
                color: "white",
                maxWidth: "70%",
              }}>
                <strong>Tú:</strong> {item.pregunta}
              </div>
              <div style={{
                alignSelf: "flex-start",
                padding: "10px",
                backgroundColor: "#28a745",
                borderRadius: "10px",
                color: "white",
                maxWidth: "70%",
                marginTop: "5px",
              }}>
                <strong>ChatBot:</strong> {item.respuesta}
              </div>
            </div>
          ))}
          <div ref={chatRef}></div>
        </div>
        <div style={{ display: "flex", gap: "10px", marginTop: "10px" }}>
          <input
            value={mensaje}
            onChange={(e) => setMensaje(e.target.value)}
            placeholder="Escribe tu pregunta..."
            style={{ flexGrow: 1, padding: "10px", border: "1px solid #666", borderRadius: "5px", backgroundColor: "#444", color: "white" }}
          />
          <button 
            onClick={enviarMensaje} 
            style={{ padding: "10px 15px", backgroundColor: "#007bff", color: "white", border: "none", borderRadius: "5px", cursor: "pointer" }}
          >
            Enviar
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;
