// need fast input, direct translation of my python code that gets TLE

#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    cin >> n >> k;
    int nums[n];
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }

    long long total = (long long)n * (n + 1) / 2;  // total number of sub arrays

    unordered_map<int, int> freq;
    int left = 0;  // sliding window
    for (int right = 0; right < n; right++) {
        freq[nums[right]]++;

        while (freq.size() >= k) {
            int left_num = nums[left];
            freq[left_num]--;
            if (freq[left_num] == 0) {
                freq.erase(left_num);
            }
            left++;
        }

        total -= (right - left + 1);
    }

    cout << total << endl;
}
