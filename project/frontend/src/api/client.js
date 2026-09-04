import axios from 'axios';

const client = axios.create({
  baseURL: 'http://localhost:8000/api',
});

export const uploadEvidence = (caseId, formData) => {
  return client.post(`/cases/${caseId}/evidence`, formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
  });
};

export const getGraph = (caseId) => {
  return client.get(`/graph/${caseId}/graph`);
};

export default client;
