// python code has explanations and stuff

#include <bits/stdc++.h>

using namespace std;

int N;
vector<set<int>> graph;
vector<int> _size;

void precompute_size(int cur, int prev) {
    _size[cur] = 1;
    for (int adj : graph[cur]) {
        if (adj == prev)
            continue;
        precompute_size(adj, cur);
        _size[cur] += _size[adj];
    }
}

int get_centroid(int cur, int prev, int comp_size) {
    for (int adj : graph[cur]) {
        if (adj != prev && _size[adj] > comp_size / 2)
            return get_centroid(adj, cur, comp_size);
    }
    return cur;
}

int main() {
    cin >> N;
    graph.resize(N + 1);
    _size.resize(N + 1, 0);
    for (int i = 0; i < N - 1; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].insert(b);
        graph[b].insert(a);
    }

    int root = 1;
    while (true) {
        precompute_size(root, -1);
        int centroid = get_centroid(root, -1, _size[root]);
        cout << centroid << endl;
        int closer;
        cin >> closer;

        if (closer == 0)
            break;

        for (int adj : graph[centroid])
            graph[adj].erase(centroid);

        root = closer;
    }
    return 0;
}
