// https://dmoj.ca/problem/ccoprep1p3
// Store each group with a sorted structure, so we can efficiently get the k-th smallest element
// When joining groups, we use a disjoint set to keep track of each groups' root, also use
// union by size (merge smaller groups to larger ones) so fewer elements are moved (moving an element takes log(n))
//
// TC: O(N*log^2(N) + Qlog(N))

#include<bits/stdc++.h>
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;

vector<int> parent, sze;
vector<ordered_set> groups;

int find(int node) {
    if(parent[node] != node)
        parent[node] = find(parent[node]);
    return parent[node];
}

void union_sets(int a, int b) {
    int root_a = find(a);
    int root_b = find(b);
    if(root_a == root_b)
        return;
    if(sze[root_b] > sze[root_a])
        swap(root_a, root_b);
    parent[root_b] = root_a;
    sze[root_a] += sze[root_b];
    for(auto &it : groups[root_b])
        groups[root_a].insert(it);
    groups[root_b].clear();
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    cin >> N >> M;
    vector<int> rank(N+1), loc(N+1);
    parent.resize(N+1);
    sze.assign(N+1, 1);
    groups.resize(N+1);
    for(int i = 1; i <= N; i++) {
        parent[i] = i;
        cin >> rank[i];
        loc[rank[i]] = i;
        groups[i].insert(rank[i]);
    }
    for(int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        union_sets(a, b);
    }
    int Q;
    cin >> Q;
    while(Q--) {
        char type;
        cin >> type;
        if(type == 'B') {
            int x, y;
            cin >> x >> y;
            union_sets(x, y);
        } else {
            int x, k;
            cin >> x >> k;
            int root = find(x);
            if(groups[root].size() < k)
                cout << -1 << "\n";
            else
                cout << loc[*groups[root].find_by_order(k - 1)] << "\n";
        }
    }
    return 0;
}
