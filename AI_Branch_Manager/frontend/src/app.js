import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [message, setMessage] = useState('');
    const [response, setResponse] = useState('');

    const handleConversation = async (e) => {
        e.preventDefault();
        
        const res = await axios.post('http://127.0.0.1:5000/conversation', { message });
        setResponse(res.data.response);
    };

    return (
        <div className="App">
            <h1>AI Branch Manager</h1>
            <form onSubmit={handleConversation}>
                <input 
                    type="text" 
                    value={message} 
                    onChange={(e) => setMessage(e.target.value)} 
                    placeholder="Ask a question..." 
                />
                <button type="submit">Send</button>
            </form>
            <div>
                <h2>Response:</h2>
                <p>{response}</p>
            </div>
        </div>
    );
}

export default App;
