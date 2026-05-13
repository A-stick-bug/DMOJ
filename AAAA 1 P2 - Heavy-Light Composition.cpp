#include <bits/stdc++.h>
#define int long long
using namespace std;

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

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<pair<int,char>> lights(n);
    for (int i = 0; i < n; i++) {
        int pos;
        cin >> pos;
        lights[i] = {pos, 'l'};
    }


    vector<pair<int,char>> arr(m);
    for (int i = 0; i < m; i++) {
        int pos;
        cin >> pos;
        arr[i] = {pos, 'a'};
    }

    vector<pair<int,char>> pos;
    for (auto &p : lights) pos.push_back(p);
    for (auto &p : arr) pos.push_back(p);
    sort(pos.begin(), pos.end());

    DisjointSet ds(pos.size() + 3);
    for (int i = 0; i < pos.size(); i++) {
        if (pos[i].second == 'l') {
            ds.join(pos.size(), i);
        }
    }

    vector<pair<int,int>> edges;
    for (int i = 0; i < pos.size() - 1; i++)
        edges.emplace_back(i, i + 1);

    sort(edges.begin(), edges.end(), [&](const pair<int,int>& x, const pair<int,int>& y){
        int dx = pos[x.second].first - pos[x.first].first;
        int dy = pos[y.second].first - pos[y.first].first;
        return dx < dy;
    });

    int con = 0;
    int cost = 0;
    for (auto [a,b] : edges) {
        if (con == m) break;
        if (ds.find(a) != ds.find(b)) {
            ds.join(a, b);
            cost += pos[b].first - pos[a].first;
            con += 1;
        }
    }
    cout << cost << '\n';
    return 0;
}
