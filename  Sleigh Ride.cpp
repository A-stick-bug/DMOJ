/*
https://dmoj.ca/problem/sleigh

Q: Given a tree (0 is root), find the shortest path to visit all nodes (don't need to get back to start)

Because we don't need to get back to the start, we just find the furthest path down the tree
and minus that from (total length of all the path)*2
This works because we need to take each path exactly twice if we do need to get back to the start,
but since we don't, we can visit the furthest node last to save the most distance
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    long long total_cost = 0;
    vector<vector<pair<int, int>>> graph(n + 1);  // create graph from input
    for (int i = 0; i < n; ++i) {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].push_back({b, c});
        graph[b].push_back({a, c});
        total_cost += c;
    }

    long long highest = 0;  // dfs to find longest path from root
    vector<tuple<int, long long, int>> stack = {{0, 0, -1}};
    while (!stack.empty()) {
        auto [cur, dist, prev] = stack.back();
        stack.pop_back();
        highest = max(highest, dist);

        for (auto [adj, d] : graph[cur]) {
            if (adj == prev) continue;
            stack.push_back({adj, dist + d, cur});
        }
    }

    cout << total_cost * 2 - highest << "\n";

    return 0;
}