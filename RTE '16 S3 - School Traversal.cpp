// https://dmoj.ca/problem/rte16s3
// Use O(n^2) precomputation with DFS to answer queries of distance between 2 nodes in O(1)
//
// things to note:
// - the 'graph' is actually a tree
// - the distance from a node to itself is 0
// - we must use unsigned ints to store the distance between 2 nodes to prevent overflow

#include <bits/stdc++.h>

using namespace std;

const int NM = 6000;
int N, Q;
vector<tuple<int, int>> graph[NM];
unsigned int dist[NM][NM];

void get_dists(int start) {  // DFS to get distance from one node to all other nodes, O(n)
    stack<tuple<int, unsigned int>> st;
    st.emplace(start, 0);

    while (!st.empty()) {
        auto [cur, d] = st.top();
        st.pop();

        for (auto [adj, n_dist]: graph[cur]) {
            if (dist[start][adj] == 0) {  // haven't reached this node yet
                dist[start][adj] = d + n_dist;  // update distance to this node
                st.emplace(adj, d + n_dist);
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    int a, b, w;
    for (int i = 0; i < N - 1; i++) {  // create graph
        cin >> a >> b >> w;
        graph[a].emplace_back(b, w);
        graph[b].emplace_back(a, w);
    }

    for (int i = 0; i < N; i++)  // precompute distances
        get_dists(i);

    cin >> Q;
    for (int i = 0; i < Q; i++) {  // answer queries
        cin >> a >> b;
        if (a == b) cout << 0 << "\n";  // distance to itself is always 0
        else cout << dist[b][a] << "\n";
    }

    return 0;
}

