// https://dmoj.ca/problem/vmss7wc16c6p3
// Template problem for finding articulation points (cut vertices) in a graph (undirected)
// using Tarjan's algorithm

#include <bits/stdc++.h>
using namespace std;

vector<int> node_id, low_link;
vector<bool> cut_vertex;
vector<vector<int>> graph;
int t = 0;

void dfs(int cur, int prev) {
    node_id[cur] = low_link[cur] = t++;
    int c = 0;  // number of children
    for (int adj : graph[cur]) {
        if (adj == prev) continue;  // ignore loops between adjacent nodes
        if (node_id[adj] == -1) {  // not visited
            dfs(adj, cur);
            c++;
            low_link[cur] = min(low_link[cur], low_link[adj]);
            if (low_link[adj] >= node_id[cur] && prev != -1)
                cut_vertex[cur] = true;
        } else {
            low_link[cur] = min(low_link[cur], node_id[adj]);
        }
    }
    // Special handling for the root: cut vertex if it connects 2 components
    if (prev == -1 && c > 1)
        cut_vertex[cur] = true;
}

vector<int> get_cut_vertices() {
    int N = graph.size();
    node_id.assign(N, -1);
    low_link.assign(N, -1);
    cut_vertex.assign(N, false);

    for (int u = 0; u < N; ++u)
        if (node_id[u] == -1)
            dfs(u, -1);

    vector<int> cut;
    for (int u = 0; u < N; ++u)
        if (cut_vertex[u])
            cut.push_back(u);
    return cut;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N, M;
    cin >> N >> M;

    graph.resize(N + 1);
    for (int i = 0; i < M; ++i) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    vector<int> cut = get_cut_vertices();
    sort(cut.begin(), cut.end());

    cout << cut.size() << "\n";
    for (int v : cut)
        cout << v << "\n";
    return 0;
}