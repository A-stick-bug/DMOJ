#include <bits/stdc++.h>
#define int long long

using namespace std;

const int inf = 1LL << 60;

signed main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, H;
    cin >> N >> H;
    vector<int> prev1(H + 1, -inf);  // did not take previous set
    vector<int> prev2(H + 1, -inf);

    prev1[0] = prev2[0] = 0;

    // (val, cost), (val, cost)
    for (int i = 0; i < N; i++) {
        int v1, c1, v2, c2;
        cin >> v1 >> c1 >> v2 >> c2;

        // 0/1 first for going to the NPCs
        vector<int> dp2(H + 1, -inf);
        vector<int> dp1(H + 1);
        for (int j = 0; j <= H; j++) {
            dp1[j] = max(prev1[j], prev2[j]);  // not taking from this set
        }

        for (int v = H; v >= c1; v--) {
            dp2[v] = dp1[v - c1] + v1;
        }

        // unbounded for doing amounts of quests
        for (int v = c2; v <= H; v++) {
            dp2[v] = max(dp2[v], dp2[v - c2] + v2);
        }

        prev1 = dp1;
        prev2 = dp2;
    }

    cout << max(*max_element(prev1.begin(), prev1.end()), *max_element(prev2.begin(), prev2.end())) << "\n";

    return 0;
}
