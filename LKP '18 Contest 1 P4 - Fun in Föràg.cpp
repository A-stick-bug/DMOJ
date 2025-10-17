// https://dmoj.ca/problem/lkp18c1p4
// binary search the answer, then it's just running dijkstra's algorithm to check if the current answer works
// first time writing dijkstra's algorithm in C++

#include <bits/stdc++.h>
#define ll long long

using namespace std;

vector<vector<tuple<int, int, int>>> graph;
int START, END, TIME, N, M;;

bool works(int m) {
    priority_queue<tuple<ll, int>, vector<tuple<ll, int>>, greater<>> pq;
    vector<ll> vis(N+1, LLONG_MAX);
    vis[START] = 0;
    pq.emplace(0, START);
    while (!pq.empty()) {
        auto [d, cur] = pq.top();
        pq.pop();

        if (d > vis[cur])  // KEY OPTIMIZATION
            continue;

        if (cur == END) {
            return d < TIME;
        }
        for (auto [adj, adj_d, clearance]: graph[cur]) {
            if (clearance > m)  // not allowed here
                continue;
            ll new_d = adj_d + d;
            if (vis[adj] > new_d) {
                vis[adj] = new_d;
                pq.emplace(new_d, adj);
            }
        }
    }
    return false;
}


signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;
    graph.resize(N + 1);

    int a, b, c;
    for (int m = 1; m <= M; m++) {  // create graph from input
        cin >> a >> b >> c;
        graph[a].emplace_back(b, c, m);
        graph[b].emplace_back(a, c, m);
    }
    cin >> START >> END >> TIME;

    int low = 1, high = M, mid;
    while (low <= high) {
        mid = (high + low) / 2;
        if (works(mid))
            high = mid - 1;
        else
            low = mid + 1;
    }

    if (low <= M)
        cout << low << "\n";
    else
        cout << -1 << "\n";

    return 0;
}

/*
4 4
1 2 3
3 4 2
2 3 1
1 4 99
1 4 9

Output: 3
*/
