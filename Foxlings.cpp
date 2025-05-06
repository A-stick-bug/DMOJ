// https://dmoj.ca/problem/foxl
// Count number of components
// Note that most nodes are not connected to anything so we just coord compress the ones that are

#include <bits/stdc++.h>

using namespace std;

class DisjointSet {
public:
    vector<int> parent, size;

    DisjointSet(int N) {
        parent.resize(N);
        size.assign(N, 1);
        for (int i = 0; i < N; ++i)
            parent[i] = i;
    }

    int find(int node) {
        if (parent[node] != node)
            parent[node] = find(parent[node]);
        return parent[node];
    }

    void unite(int a, int b) {
        int root_a = find(a);
        int root_b = find(b);
        if (root_a == root_b) return;
        if (size[root_b] > size[root_a])
            swap(root_a, root_b);
        parent[root_b] = root_a;
        size[root_a] += size[root_b];
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<pair<int, int>> queries(m);
    vector<int> nodes;

    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        queries[i] = {a, b};
        nodes.push_back(a);
        nodes.push_back(b);
    }

    sort(nodes.begin(), nodes.end());  // coordinate compression
    nodes.erase(unique(nodes.begin(), nodes.end()), nodes.end());
    int c_n = nodes.size();

    DisjointSet ds(c_n);
    int components = c_n;

    for (auto [a, b] : queries) {
        int idx_a = lower_bound(nodes.begin(), nodes.end(), a) - nodes.begin();
        int idx_b = lower_bound(nodes.begin(), nodes.end(), b) - nodes.begin();
        if (ds.find(idx_a) != ds.find(idx_b)) {
            ds.unite(idx_a, idx_b);
            components--;
        }
    }

    cout << (n - c_n) + components << '\n';
    return 0;
}
