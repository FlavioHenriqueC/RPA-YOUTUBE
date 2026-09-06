import { useState } from 'react';

function App() {
  const [url, setUrl] = useState('');
  const [loading, setLoading] = useState(false);

  const handleDownload = async () => {
    if (!url) return alert("Insira o link!");
    
    setLoading(true);
    try {
      // Faz a chamada para a nossa API em Python
      const response = await fetch(`http://localhost:8000/baixar?url=${encodeURIComponent(url)}`);
      
      if (!response.ok) throw new Error("Erro ao baixar o áudio");

      // Transforma a resposta em um arquivo (Blob)
      const blob = await response.blob();
      
      // Cria um link temporário para forçar o download no navegador
      const downloadUrl = window.URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = downloadUrl;
      link.download = "musica.mp3"; // O navegador vai usar o nome original se definido no header
      document.body.appendChild(link);
      link.click();
      link.remove();

    } catch (error) {
      alert("Ocorreu um erro: " + error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '50px', fontFamily: 'sans-serif', maxWidth: '500px', margin: 'auto' }}>
      <h2>Downloader de Áudio do YouTube</h2>
      
      <input 
        type="text" 
        placeholder="Cole o link do YouTube aqui..." 
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        style={{ width: '100%', padding: '10px', marginBottom: '20px' }}
      />
      
      <button 
        onClick={handleDownload} 
        disabled={loading}
        style={{ width: '100%', padding: '15px', backgroundColor: '#3B8ED0', color: 'white', border: 'none', cursor: 'pointer' }}
      >
        {loading ? 'Baixando e Convertendo...' : 'Baixar Música'}
      </button>
    </div>
  );
}

export default App;