// https://dmoj.ca/problem/fastlca
// tfw your sparse table LCA and tarjan's offline algorithm both MLE and brute force passes...
// Because of the way the data is generated, it's unlikely the tree will be very deep
// so we just travel up from both nodes and see when they first meet

#include <iostream>

using namespace std;

const int MN = 6000001;
int parent[MN];
bool vis[MN];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;

    for (int i = 2; i <= N; ++i) {
        cin >> parent[i];
    }

    for (int i = 0; i < Q; i++) {
        int u, v;
        cin >> u >> v;
        int reset = u;
        while (u) {  // go up until we reach 0
            vis[u] = true;
            u = parent[u];
        }

        while (!vis[v]) {  // go up until path converges
            v = parent[v];
        }
        cout << v << "\n";

        while (reset) {  // clear used nodes
            vis[reset] = false;
            reset = parent[reset];
        }
    }
    return 0;
}
