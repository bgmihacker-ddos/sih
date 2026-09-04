import React, { useEffect, useState } from 'react';
import ReactFlow from 'react-flow-renderer';
import { getGraph } from '../api/client';

const GraphView = ({ caseId }) => {
  const [elements, setElements] = useState([]);

  useEffect(() => {
    const fetchGraph = async () => {
      try {
        const response = await getGraph(caseId);
        const { nodes, edges } = response.data;
        // Transform backend nodes/edges to React Flow format
        const rfNodes = nodes.map(n => ({ id: n.id, data: { label: n.label }, position: { x: 100, y: 100 } }));
        const rfEdges = edges.map(e => ({ id: `${e.from}-${e.to}`, source: e.from, target: e.to }));
        setElements([...rfNodes, ...rfEdges]);
      } catch (err) {
        console.error("Failed to load graph", err);
      }
    };
    fetchGraph();
  }, [caseId]);

  return (
    <div style={{ height: '500px', width: '100%', border: '1px solid #ccc' }}>
      <ReactFlow elements={elements} />
    </div>
  );
};

export default GraphView;
