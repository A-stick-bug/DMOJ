// https://dmoj.ca/problem/graph2p2
// graph may not be connected, so we run multiple DFS

#include <bits/stdc++.h>

using namespace std;

const int MN = 1000;
bool graph[MN][MN], vis[MN], path[MN];

bool dfs(int cur) {  // (DFS) returns whether there exists a cycle in the graph
    if (vis[cur]) {
        return path[cur];  // if the visited node is in the current path, we have a cycle
    }
    vis[cur] = true;
    path[cur] = true;
    bool c = false;
    for (int i = 0; i < MN; i++) {
        if (graph[cur][i]) {
            c |= dfs(i);
        }
    }
    path[cur] = false;
    return c;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    for (int i = 0; i < N; i++) {  // create graph from input
        for (int j = 0; j < N; j++) {
            cin >> graph[i][j];
        }
    }

    // run dfs starting from all nodes, skip nodes that were processed in previous dfs
    for (int node = 0; node < N; node++) {
        if (!vis[node]) {
            if (dfs(node)) {
                cout << "NO" << "\n";
                return 0;
            }
        }
    }

    cout << "YES" << "\n";
    return 0;
}
