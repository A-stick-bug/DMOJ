#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<pair<int, int>> hw(n);
    for (int i = 0; i < n; ++i) {
        cin >> hw[i].first >> hw[i].second;
    }

    sort(hw.begin(), hw.end(), greater<pair<int, int>>());

    priority_queue<int> pq;
    vector<int> days(hw[0].first + 1, 0);
    int j = 0;

    for (int time = hw[0].first; time >= 1; --time) {
        while (j < n && hw[j].first >= time) {
            pq.push(hw[j].second);
            ++j;
        }
        if (!pq.empty()) {
            days[time] = pq.top();
            pq.pop();
        }
    }

    cout << accumulate(days.begin(), days.end(), 0) << endl;

    return 0;
}
