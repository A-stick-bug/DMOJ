/*
 https://dmoj.ca/problem/ioi13p1io
 given a forest, turn it into a tree by adding edges while minimizing the diameter
 some similarities with https://dmoj.ca/problem/tle16c4p4

 Key observations:
 - when joining 2 components together, always join by their center (point that minimizes max distance)
   note: radius is farthest distance from a component's center
 - edge case: it is possible that a single component's diameter exceeds the joined radius of 2 components + joining cost
 - when joining many components together, we join all their centers to the center of the component with the
   largest radius, lets call this the center component
   - when doing this, the radius of every component except the center component's will increase by L
     this is we choose the center component to always be the one with the largest radius
   - instead of increasing every component by L, we actually only worry about the next 2 largest radii since they
     together will possibly yield the largest sum
 */

#include <bits/stdc++.h>

using namespace std;

int N, M, L;
vector<vector<pair<int, int>>> graph;
vector<bool> vis;
vector<int> diameters;

unordered_map<int, int> dfs(int start) {  // get the distance to every reachable node from start
    unordered_map<int, int> dist;
    dist[start] = 0;
    stack<int> st;
    st.push(start);

    while (!st.empty()) {
        int cur = st.top();
        st.pop();
        for (auto [adj, adj_d]: graph[cur]) {
            if (dist.find(adj) == dist.end()) {
                dist[adj] = dist[cur] + adj_d;
                st.push(adj);
            }
        }
    }
    return dist;
}

int get_radius(int start){  // find most even split of tree, also store the component's diameter
    unordered_map<int, int> dist = dfs(start);
    int end1 = start;
    for (auto [k, v]:dist)  // get diameter endpoints
        if (v > dist[end1])
            end1 = k;
    unordered_map<int, int> dist1 = dfs(end1);
    int end2 = start;
    for (auto [k, v]:dist1)
        if (v > dist1[end2])
            end2 = k;
    unordered_map<int, int> dist2 = dfs(end2);

    // find most even split which is guaranteed to be on the diameter
    int best = INT32_MAX;
    int d = 0;
    for (auto [k, v]: dist1){
        best = min(best, max(dist1[k], dist2[k]));
        d = max(d, v);
        vis[k] = true;
    }
    diameters.push_back(d);  // store diameter for later
    return best;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M >> L;

    graph.resize(N);  // create graph from input
    vis.resize(N);
    int a, b, t;
    for (int i = 0; i < M; i++) {
        cin >> a >> b >> t;
        graph[a].emplace_back(b, t);
        graph[b].emplace_back(a, t);
    }

    vector<int> radii;  // get radius/diameter for every component
    for (int i = 0; i < N; i++){
        if (!vis[i])
            radii.push_back(get_radius(i));
    }
    sort(radii.begin(), radii.end(), greater<int>());
    int max_diameter = *max_element(diameters.begin(), diameters.end());  // max diameter of a single component

    if (radii.size() == 1)  // only 1 component, print its own diameter
        cout << diameters[0] << "\n";
    else if (radii.size() == 2)  // max(sum of both component's radii + joining cost, max diameter of single component)
        cout << max(radii[0] + radii[1] + L, max_diameter) << "\n";
    else{  // we extend the logic for 2 components using the observation stated at the top of the code
        radii[1] += L;
        radii[2] += L;
        sort(radii.begin(), radii.end(), greater<int>());
        cout << max(radii[0] + radii[1], max_diameter) << "\n";
    }
    return 0;
}
