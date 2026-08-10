// https://dmoj.ca/problem/noi16p1
// 95/100, don't have full solution yet
//
// Basically brute force, optimized with hashing to compare substrings
// Try all split points between A and B, then try all lengths of A and B
//
// TC: O(n^2)

#include <bits/stdc++.h>
using namespace std;

template <size_t MAX_N = 200'005>
class SubstringHash {
public:
    static constexpr uint64_t MOD = (1ULL << 61) - 1;

private:
    static inline uint64_t mod61(unsigned __int128 x) {
        uint64_t val = (x >> 61) + (x & MOD);
        if (val >= MOD) val -= MOD;
        return val;
    }

    static inline uint64_t generate_base() {
        uint64_t seed = std::chrono::steady_clock::now().time_since_epoch().count();
        std::mt19937_64 rng(seed);
        std::uniform_int_distribution<uint64_t> dist(300, MOD - 2);
        return dist(rng) | 1;
    }

    static inline uint64_t init_powers(uint64_t* arr) {
        uint64_t base = generate_base();
        arr[0] = 1;
        for (size_t i = 1; i < MAX_N; ++i) {
            arr[i] = mod61((unsigned __int128)arr[i - 1] * base);
        }
        return base;
    }

    static inline uint64_t pows[MAX_N];
    static inline const uint64_t BASE = init_powers(pows);

    std::vector<uint64_t> psa;

public:
    explicit SubstringHash(std::string_view s) : psa(s.size() + 1, 0) {
        for (size_t i = 0; i < s.size(); ++i) {
            psa[i + 1] = mod61((unsigned __int128)psa[i] * BASE + static_cast<uint8_t>(s[i]));
        }
    }

    [[nodiscard]] inline uint64_t query(int l, int r) const {
        int len = r - l + 1;
        uint64_t p = pows[len];
        uint64_t sub = mod61((unsigned __int128)psa[l] * p);
        if (psa[r + 1] >= sub) {
            return psa[r + 1] - sub;
        } else {
            return psa[r + 1] + MOD - sub;
        }
    }
};

void solve() {
    string s;
    cin >> s;
    int n = s.size();

    SubstringHash sh(s);
    long long total = 0;
    for (int i = 2; i < n - 1; i++) {
        // i is the start of the first B
        int valid_l = 0, valid_r = 0;
        for (int l = i - 1, l2 = i - 2; l2 >= 0; l--, l2 -= 2) {
            if (sh.query(l2, l - 1) == sh.query(l, i - 1)) {
                valid_l++;
            }
        }
        for (int r = i, r2 = i + 1; r2 < n; r++, r2 += 2) {
            if (sh.query(i, r) == sh.query(r + 1, r2)) {
                valid_r++;
            }
        }

        total += valid_l * valid_r;
    }
    cout << total << endl;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
}
