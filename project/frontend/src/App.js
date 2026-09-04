import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import CaseUpload from './pages/CaseUpload';

function App() {
  return (
    <Router>
      <div className="flex h-screen bg-gray-100">
        <nav className="w-64 bg-gray-800 text-white p-4">
          <h1 className="text-xl font-bold mb-6">FORENSIGHT</h1>
          <ul>
            <li className="mb-2"><Link to="/">Dashboard</Link></li>
            <li className="mb-2"><Link to="/cases">Cases</Link></li>
            <li className="mb-2"><Link to="/upload">Upload Evidence</Link></li>
          </ul>
        </nav>
        <main className="flex-1 p-8">
          <Routes>
            <Route path="/" element={<h2>Dashboard</h2>} />
            <Route path="/cases" element={<h2>Case List</h2>} />
            <Route path="/upload" element={<CaseUpload />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
