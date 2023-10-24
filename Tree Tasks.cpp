/*
https://dmoj.ca/problem/treepractice1

Use DFS to find the diameter of the tree
- run dfs from any node (in this case, node 1 for simplicity) and find the farthest node
- run dfs from that furthest node to find the other end of the tree which keeping track of the path

Trace back the path and check the minimum distance of max(dist to 2 ends of diameter)
*/

#include <bits/stdc++.h>

using namespace std;

const int NM = 500001;
int N;
vector<pair<int, int>> graph[NM];

pair<int, int>
get_farthest(int start, bool operation) {  // operation = true: finds farthest node, false: find diameter and radius
    stack<int> st;
    st.push(start);
    int dist[N + 1];
    int prev[N + 1];
    memset(dist, -1, sizeof(dist));  // fill in with default values
    memset(prev, 0, sizeof(prev));
    dist[start] = 0;

    int cur;
    while (!st.empty()) {
        cur = st.top();
        st.pop();
        for (auto [adj, d]: graph[cur]) {
            if (dist[adj] != -1)
                continue;
            dist[adj] = dist[cur] + d;
            prev[adj] = cur;  // keep track of previous to trace path
            st.push(adj);
        }
    }
    int farthest = 1;
    for (int i = 2; i <= N; i++) {  // find farthest node
        if (dist[i] > dist[farthest])
            farthest = i;
    }

    if (operation)  // first use of the function: return farthest node
        return {farthest, 0};

    // second use: get radius and diameter
    int diameter = dist[farthest];
    int radius = 1e9;
    while (farthest != 0){  // check distance to either end for each node in the diameter
        radius = min(radius, max(dist[farthest], diameter - dist[farthest]));
        farthest = prev[farthest];
    }
    return {diameter, radius};
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;
    for (int i, a, b, w = 0; i < N - 1; i++) {  // create tree from input
        cin >> a >> b >> w;
        graph[a].emplace_back(b, w);
        graph[b].emplace_back(a, w);
    }

    int farthest = get_farthest(1, true).first;  // get farthest node from 1
    auto [diam, rad] = get_farthest(farthest, false);  // get diameter and radius

    cout << diam << "\n" << rad << "\n";
    return 0;
}
