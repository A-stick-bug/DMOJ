// https://dmoj.ca/problem/noi04p1
// Brute force (binary search), passes due to weak data
// check python code for proper solution

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int N, M;

int main() {
    cin >> N >> M;
    int left = 0;
    vector<int> wages;

    for (int i = 0; i < N; i++) {
        char cmd;
        int val;
        cin >> cmd >> val;

        if (cmd == 'I') {  // add new person
            if (val < M)  // left immediately
                continue;
            wages.insert(lower_bound(wages.begin(), wages.end(), val), val);
        }

        else if (cmd == 'F') {
            if (val > wages.size()) {  // not enough people
                cout << -1 << endl;
                continue;
            }
            cout << wages[wages.size() - val] << endl;
        }

        else if (cmd == 'A') {
            for (int &wage : wages)
                wage += val;
        }

        else {
            for (int &wage : wages)
                wage -= val;
            int old = wages.size();
            wages.erase(remove_if(wages.begin(), wages.end(),  [](int x){return (x < M);}), wages.end());
            left += old - wages.size();
        }
    }
    cout << left << endl;
    return 0;
}