// https://dmoj.ca/problem/ioi11p4io
// Multi source dijkstra with second best option at each node
// States: [2nd best?][shortest path to end with 2nd best only]
//
// Reason of correctness:
// - Since there are many destinations, start from the ends and work backwards
// - Only pop a node from the queue once
//   - Once we pop it off the queue, it means that is currently has the smallest '2nd distance' (PQ property)
//   - (!!) This means it is currently optimal as no other path can reduce its distance

#include <bits/stdc++.h>
using namespace std;
#define int long long

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M, K;
    cin >> N >> M >> K;
    vector<vector<pair<int, int>>> graph(N);
    for (int i = 0; i < M; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].emplace_back(b, c);
        graph[b].emplace_back(a, c);
    }

    const int inf = 1LL << 60;
    vector<int> dist1(N + 1, inf), dist2(N + 1, inf);
    vector<bool> vis(N, false);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
    for (int i = 0; i < K; i++) {
        int e;
        cin >> e;
        dist1[e] = 0;
        dist2[e] = 0;
        pq.emplace(0, e);
    }
    while (!pq.empty()) {
        auto [d, u] = pq.top();
        pq.pop();
        if (vis[u])
            continue;
        vis[u] = true;
        for (auto [v, w] : graph[u]) {
            int nd = d + w;
            if (nd <= dist1[v]) {  // shortest found
                if (dist1[v] != inf) {  // old 1st becomes 2nd
                    dist2[v] = dist1[v];
                    pq.emplace(dist1[v], v);
                }
                dist1[v] = nd;
            } else if (nd == dist1[v] || nd < dist2[v]) {  // improve 2nd
                dist2[v] = nd;
                pq.emplace(nd, v);
            }
        }
    }
    cout << dist2[0] << "\n";
    return 0;
}
