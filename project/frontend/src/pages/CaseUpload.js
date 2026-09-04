import React, { useState } from 'react';
import { uploadEvidence } from '../api/client';

const CaseUpload = () => {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState('');

  const handleUpload = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append('file', file);

    // Using a hardcoded case ID for demonstration
    const caseId = 'example-case-id';
    try {
      await uploadEvidence(caseId, formData);
      setStatus('Upload successful!');
    } catch (error) {
      setStatus('Upload failed.');
    }
  };

  return (
    <div className="p-4 bg-white rounded shadow">
      <h2 className="text-xl mb-4">Upload Evidence</h2>
      <input type="file" onChange={(e) => setFile(e.target.files[0])} className="mb-4" />
      <button onClick={handleUpload} className="bg-blue-500 text-white px-4 py-2 rounded">
        Upload
      </button>
      {status && <p className="mt-2">{status}</p>}
    </div>
  );
};

export default CaseUpload;
