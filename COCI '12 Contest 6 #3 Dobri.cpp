#include <iostream>
#include <vector>

#define OFFSET 200001

int main() {
    int n;
    std::cin >> n;

    std::vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }

    std::vector<bool> exists(OFFSET * 2, false);
    int total = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {  // 3-sum with numbers before current index
            if (exists[OFFSET + arr[i] - arr[j]]) {  // matched pair
                total += 1;
                break;
            }
        }
        for (int j = 0; j <= i; j++) {  // current number can now be match with other numbers before it
            exists[OFFSET + arr[i] + arr[j]] = true;
        }
    }

    std::cout << total << std::endl;
    return 0;
}
