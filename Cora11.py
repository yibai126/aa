import os
import torch
from torch.utils.data import Dataset
import pandas as pd
import numpy as np

class CoraDataset(Dataset):
    def __init__(self, data_dir='./cora', mode='train'):
        self.mode = mode
        # 加载数据
        nodes_df = pd.read_csv(f'{data_dir}/cora.content', sep='\t', header=None)
        edges_df = pd.read_csv(f'{data_dir}/cora.cites', sep='\t', header=None)
        # 处理节点特征和标签
        self.features = nodes_df.iloc[:, 1:-1].values.astype(np.float32)
        self.labels = pd.Categorical(nodes_df.iloc[:, -1]).codes
        # 处理边
        node_map = {id: idx for idx, id in enumerate(nodes_df[0])}
        self.edges = torch.tensor([[node_map[src], node_map[dst]] for src, dst in edges_df.values if src in node_map and dst in node_map]).t()
        # 划分数据集
        n = len(self.features)
        idx = np.random.permutation(n)
        split = {'train': idx[:140], 'val': idx[140:640], 'test': idx[640:1640]}
        self.indices = split[mode]
        
    def __len__(self):
        return len(self.indices)
    
    def __getitem__(self, idx):
        i = self.indices[idx]
        return torch.tensor(self.features[i]), torch.tensor(self.labels[i])
if __name__ == "__main__":
    dataset = CoraDataset('./cora')
    print(f"数据集大小：{len(dataset)}")
    print(F"特征维度：{dataset.features.shape[1]}")