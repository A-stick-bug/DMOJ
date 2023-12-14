// https://dmoj.ca/problem/electricity
// Kruskal's algorithm with 'virtual node and edges'
// 1-indexing, 0-th index is for the virtual node
// basically connect all houses with electricity together, so a house won't be connected twice

#include <bits/stdc++.h>

using namespace std;

class UnionFind {
public:
    UnionFind(int sz) : root(sz), rank(sz) {
        for (int i = 0; i < sz; i++) {
            root[i] = i;
            rank[i] = 1;
        }
    }

    int find(int x) {
        if (x == root[x]) {
            return x;
        }
        return root[x] = find(root[x]);
    }

    void unionSet(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX != rootY) {
            if (rank[rootX] > rank[rootY]) {
                root[rootY] = rootX;
            } else if (rank[rootX] < rank[rootY]) {
                root[rootX] = rootY;
            } else {
                root[rootY] = rootX;
                rank[rootX] += 1;
            }
        }
    }

    bool connected(int x, int y) {
        return find(x) == find(y);
    }

private:
    vector<int> root;
    vector<int> rank;
};


bool edge_comp(const tuple<int, int, int>& a, const tuple<int, int, int>& b) {
    return get<2>(a) < get<2>(b);
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t, n;  // stuff used in each test case
    UnionFind uf(1);
    vector<int> arr;
    vector<int> power;
    vector<tuple<int, int, int>> edges;

    cin >> t;
    while (t--) {
        cin >> n;
        arr = vector<int>(n + 1);
        power = vector<int>(n + 1);
        edges = vector<tuple<int, int, int>>();  // a <--> b, distance of c

        for (int i = 1; i <= n; i++)
            cin >> arr[i] >> power[i];

        uf = UnionFind(n + 1);
        for (int i = 1; i < n; i++)  // create edges
            edges.emplace_back(i, i + 1, arr[i + 1] - arr[i]);

        for (int i = 1; i <= n; i++) {  // connect all houses with electricity to a virtual node
            if (power[i])
                uf.unionSet(0, i);
        }

        sort(edges.begin(), edges.end(), edge_comp);

        long long total = 0;
        for (auto [a,b,c]:edges){  // create mst
            if (!uf.connected(a,b)){
                uf.unionSet(a,b);
                total += c;
            }
        }
        cout << total << "\n";
    }
    return 0;
}
