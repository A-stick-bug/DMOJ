// https://dmoj.ca/problem/mccc2s3
// brute force with disjoint sets
// TC: O(128M), where 128 is the maximum possible cost

#include <bits/stdc++.h>
using namespace std;

const int MM = 128;

class DisjointSet {
    public:
    vector<int> parent;
    vector<int> sz;
    DisjointSet(int n) {
        parent.resize(n);
        sz.resize(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            sz[i] = 1;
        }
    }
    int find(int node) { // with path compression
        if (parent[node] == node) // root
            return node;
        return parent[node] = find(parent[node]);
    }
    void join(int a, int b) { // with union by size
        int root_a = find(a);
        int root_b = find(b);
        if (root_a == root_b)
            return;
        // join the smaller to the larger
        if (sz[root_b] > sz[root_a])
            swap(root_a, root_b);
        parent[root_b] = root_a;
        sz[root_a] += sz[root_b];
    }
    bool connected(int x, int y) {
        return find(x) == find(y);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N, M, Q;
    cin >> N >> M >> Q;

    vector<array<int, 3>> edges;
    for (int i = 0, a, b, c; i < M; i++){
        cin >> a >> b >> c;
        edges.push_back({a, b, c});
    }

    // make MSTs, where the i-th MST has a maximum cost of i between nodes
    // note that OR is idempotent so if 2 nodes are connected in the i-th MST
    // the minimum OR cost between them will be i
    vector<DisjointSet> msts(MM, DisjointSet(N + 1));
    for (int i = 0; i < MM; i++){
        for (auto [a, b, c]: edges){
            if ((i|c) == i)  // only use edges that won't increase the cost to over i
                msts[i].join(a, b);
        }
    }

    int a, b;
    while (Q--){
        cin >> a >> b;  // find the first MST that they are connected in
        for (int i = 0; i < MM; i++){
            if (msts[i].connected(a, b)){
                cout << i << "\n";
                break;
            }
        }
    }
    return 0;
}
