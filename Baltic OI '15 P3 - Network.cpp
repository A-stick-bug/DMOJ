/*
 https://dmoj.ca/problem/btoi15p3
 same logic as https://dmoj.ca/problem/cco07p6 except we don't need to compress the biconnected components
 Strategy:
 - connect all leaf nodes in pairs
 - if we have an odd number of leaf nodes, just connect the single one to any other leaf
*/

#include <iostream>
#include <vector>

using namespace std;

vector<int> graph[500005];
vector<int> order;

void traversal(int cur, int prev) {
    if (graph[cur].size() == 1) {
        order.push_back(cur);
    }
    for (int adj : graph[cur]) {
        if (adj == prev) {
            continue;
        }
        traversal(adj, cur);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    for (int i = 0; i < n - 1; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    traversal(1, -1);
    int cnt = order.size();
    cout << (cnt + 1) / 2 << "\n";  // number of pairs

    if (cnt % 2 == 1) {  // odd case, pair with any other leaf
        cout << order[0] << " " << order[cnt - 1] << "\n";
        cnt -= 1;
        order.pop_back();
    }

    int offset = cnt / 2;  // match first half with second half
    for (int i = 0; i < cnt / 2; i++) {
        cout << order[i] << " " << order[i + offset] << "\n";
    }

    return 0;
}
