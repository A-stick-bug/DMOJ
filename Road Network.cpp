// template MST problem, I used Kruskal's algorithm (Prim's also works)
// note that I used c++ instead of python to have more accurate decimals (double) and to use setprecision(2)

#include <bits/stdc++.h>
using namespace std;

struct UnionFind {
    vector<int> parent, size;
    UnionFind(int n) : parent(n), size(n, 1) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int x) {
        if (x != parent[x]) parent[x] = find(parent[x]);
        return parent[x];
    }
    void unite(int x, int y) {
        x = find(x); y = find(y);
        if (size[y] > size[x]) swap(x, y);
        parent[y] = x;
        size[x] += size[y];
    }
};

double dist(pair<int, int> a, pair<int, int> b) {
    double dx = a.first - b.first;
    double dy = a.second - b.second;
    return sqrt(dx * dx + dy * dy);
}

int main() {
    int N, M;
    cin >> N >> M;
    vector<pair<int, int>> villages(N+1);
    for (int i = 1; i <= N; ++i)
        cin >> villages[i].first >> villages[i].second;

    UnionFind uf(N+1);
    for (int i = 0; i < M; ++i) {
        int a, b;
        cin >> a >> b;
        uf.unite(a, b);
    }

    vector<tuple<double, int, int>> edges;
    for (int i = 1; i <= N; ++i) {
        for (int j = i+1; j <= N; ++j) {
            edges.emplace_back(dist(villages[i], villages[j]), i, j);
        }
    }
    sort(edges.begin(), edges.end());

    double total = 0;
    for (auto [d, a, b] : edges) {
        if (uf.find(a) != uf.find(b)) {
            uf.unite(a, b);
            total += d;
        }
    }

    cout << fixed << setprecision(2) << total << endl;
    return 0;
}
