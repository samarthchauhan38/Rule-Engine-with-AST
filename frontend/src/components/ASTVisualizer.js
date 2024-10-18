import React from 'react';
import Tree from 'react-d3-tree';

const ASTVisualizer = ({ astData }) => {
  if (!astData) {
    return <p>No AST to display</p>;
  }

  const convertASTtoTree = (node) => {
    if (!node) return null;
    return {
      name: node.value || node.node_type,
      children: [convertASTtoTree(node.left), convertASTtoTree(node.right)].filter(Boolean)
    };
  };

  const treeData = convertASTtoTree(astData);

  return (
    <div id="treeWrapper" style={{ width: '100%', height: '500px' }}>
      <Tree data={treeData} orientation="vertical" translate={{ x: 400, y: 50 }} />
    </div>
  );
};

export default ASTVisualizer;
