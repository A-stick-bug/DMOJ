// compared to the python one, this code simplified the math part

#include <bits/stdc++.h>
using namespace std;

int n;
vector<int> arr;
vector<int> cnt(4, 0);
double dp[301][301][301];

double solve(int i, int j, int k) {
    if(i == 0 and j == 0 and k == 0) return 0;
    if(dp[i][j][k] > 0) return dp[i][j][k];

    double ans = n;
    if(i > 0) ans += solve(i - 1, j, k) * i;
    if(j > 0) ans += solve(i + 1, j - 1, k) * j;
    if(k > 0) ans += solve(i, j + 1, k - 1) * k;
    ans /= (i + j + k);

    dp[i][j][k] = ans;
    return ans;
}

int main() {
    cin >> n;
    arr.resize(n);
    for(int i=0; i<n; i++) {
        cin >> arr[i];
        cnt[arr[i]]++;
    }
    memset(dp, 0, sizeof(dp));
    cout << fixed << setprecision(10) << solve(cnt[1], cnt[2], cnt[3]) << "\n";
    return 0;
}
