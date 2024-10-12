// https://dmoj.ca/problem/coci06c5p6
// - Binary search and hashing
// - Note: we need to double hash to prevent collisions
// - Required optimization: .reserve() on unordered_set will ensure
//   no time is wasted on allocating extra space and rehashing

#include <bits/stdc++.h>
#define ll long long

using namespace std;

const ll MOD = 2147483647;  // 2^31 - 1
const ll MOD2 = 2147483629;  // double hashing
const int P = 29;  // prime base for hashing

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    string str1;
    cin >> str1;

    vector<int> str(N);  // a=0, b=1, ..., z=25
    for (int i = 0; i < N; ++i) {
        str[i] = str1[i] - 'a';
    }

    // precompute powers of P with MOD and MOD2
    vector<ll> power(N), power2(N);
    power[0] = power2[0] = 1;
    for (int i = 1; i < N; ++i) {
        power[i] = (power[i - 1] * P) % MOD;
        power2[i] = (power2[i - 1] * P) % MOD2;
    }

    // precompute hashes for O(1) get substring hash
    vector<ll> hash1(N), hash2(N), psa1(N + 1), psa2(N + 1);
    for (int i = 0; i < N; ++i) {
        hash1[i] = (str[i] * power[N - i - 1]) % MOD;
        hash2[i] = (str[i] * power2[N - i - 1]) % MOD2;
    }
    // psa for range hash query
    psa1[0] = psa2[0] = 0;
    for (int i = 1; i <= N; ++i) {
        psa1[i] = (psa1[i - 1] + hash1[i - 1]) % MOD;
        psa2[i] = (psa2[i - 1] + hash2[i - 1]) % MOD2;
    }

    // check if a substring of length `le` is repeated
    auto works = [&](int le) -> bool {
        unordered_set<ll> seen;
        seen.reserve(200000);  // required optimization
        for (int i = 0; i <= N - le; ++i) {
            // get double hashes
            ll hash_single = (psa1[i + le] - psa1[i] + MOD) % MOD;
            hash_single = (hash_single * power[i]) % MOD;

            ll hash_double = (psa2[i + le] - psa2[i] + MOD2) % MOD2;
            hash_double = (hash_double * power2[i]) % MOD2;

            ll p = (hash_single << 32) | hash_double; // combine hashes, equivalent to {hash1, hash2}

            if (seen.find(p) != seen.end())  // found repeat
                return true;
            seen.insert(p);
        }
        return false;
    };

    int low = 0, high = N;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (works(mid)) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    cout << low - 1 << "\n";
    return 0;
}
