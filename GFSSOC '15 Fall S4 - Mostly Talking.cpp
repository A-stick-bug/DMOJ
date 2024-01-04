#include <bits/stdc++.h>
using namespace std;

const long long INF = 1LL << 50;
typedef pair<long long, pair<int, bool>> plib;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    cin >> N >> M;

    vector<vector<pair<int, pair<long long, bool>>>> graph(N + 1);  // (destination, distance, special)
    for(int i = 0; i < M; i++) {
        int a, b;
        long long d;
        cin >> a >> b >> d;
        graph[a].push_back({b, {d, false}});
    }

    int S;
    cin >> S;
    for(int i = 0; i < S; i++) {
        int a, b;
        long long d;
        cin >> a >> b >> d;
        graph[a].push_back({b, {d, true}});
    }

    vector<vector<long long>> dist(N + 1, vector<long long>(2, INF));
    dist[1][0] = 0;

    priority_queue<plib, vector<plib>, greater<plib>> pq;
    pq.push({0, {1, false}});

    while(!pq.empty()) {
        long long d = pq.top().first;
        int cur = pq.top().second.first;
        bool special = pq.top().second.second;
        pq.pop();

        if(cur == N) {
            cout << d << "\n";
            return 0;
        }

        for(auto &edge : graph[cur]) {
            int adj = edge.first;
            long long adj_dist = edge.second.first;
            bool adj_special = edge.second.second;

            long long new_dist = adj_dist + d;
            int new_special = special + adj_special;

            if(new_special > 1)  // can't take more than 1 special path
                continue;

            if(dist[adj][new_special] > new_dist) {
                dist[adj][new_special] = new_dist;
                pq.push({new_dist, {adj, new_special}});
            }
        }
    }

    cout << -1 << "\n";
    return 0;
}
