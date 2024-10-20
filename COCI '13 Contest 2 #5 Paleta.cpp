/*
https://dmoj.ca/problem/coci13c2p5
Graph theory observations and combinatorics

- find number of possible colorings in a functional/successor graph (at most 1 cycle per component)
- solve for each component separately and multiply the answers
- if we fix the colors in the cycle, each node not in the cycle can be one of (K-1) colors
- find the number of colorings using this https://en.wikipedia.org/wiki/Chromatic_polynomial
- note: if there is no cycle, it's the same as having a cycle of length 1
*/


#include <bits/stdc++.h>

using namespace std;

const int MOD = 1e9 + 7;
int N, K;
const int MN = 1e6 + 1;
int arr[MN];
bool vis[MN];
vector<int> graph[MN];
int cycle_length = 0, component_size = 0;

// get the component details (cycle length and component size)
pair<int, int> get_comp(int cur, int prev, int depth) {
    vis[cur] = true;
    component_size++;
    int c_depth = -1, c_node = -1;

    for (int adj: graph[cur]) {
        if (adj == prev) continue;
        if (vis[adj]) { // cycle found
            c_depth = depth;
            c_node = adj;
            continue;
        }

        auto [temp_depth, temp_node] = get_comp(adj, cur, depth + 1);

        if (c_node == -1) {
            c_depth = temp_depth;
            c_node = temp_node;
        }
        if (c_node == cur) {
            cycle_length = c_depth - depth;
        }
    }
    return {c_depth, c_node};
}

// calculate the number of ways to color the cycle
long long color_cycle(int nodes) {
    if (nodes == 1)  // edge case where formula doesn't work
        return K;

    long long ways = 1;
    for (int i = 0; i < nodes; i++)
        ways = (ways * (K - 1)) % MOD;

    if (nodes % 2 == 0)
        ways = (ways + (K - 1)) % MOD;
    else
        ways = (ways - (K - 1)) % MOD;
    return ways;
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> K;
    for (int i = 1; i <= N; i++)
        cin >> arr[i];

    // build graph
    for (int i = 1; i <= N; i++) {
        if (i != arr[i]) {
            graph[i].push_back(arr[i]);
            graph[arr[i]].push_back(i);
        }
    }

    // process each component separately
    long long ways = 1;
    for (int i = 1; i <= N; i++) {
        if (vis[i]) continue;

        cycle_length = component_size = 0;
        get_comp(i, -1, 0);
        cycle_length++;  // account for root node

        int in_cycle = cycle_length;
        int not_in_cycle = component_size - cycle_length;

        // ways to color the cycle
        ways = (ways * color_cycle(in_cycle)) % MOD;
        // ways to color the rest of the tree/graph
        for (int j = 0; j < not_in_cycle; j++)
            ways = (ways * (K - 1)) % MOD;
    }

    cout << ways << "\n";
    return 0;
}