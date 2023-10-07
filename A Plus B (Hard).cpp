/*
https://dmoj.ca/problem/aplusb2
First question I solved in c++ without help

Logic:
- add: fill in shorter number with zeros and add digits, carry if needed
- subtract: larger number minus smaller number, borrow if needed

- 2 positive: use add
- 2 negative: use add and print a negative sign
- 1 positive, 1 negative:
- same number: print 0
- positive > negative: positive - negative
- negative > positive: negative - positive, print a negative sign

*/

#include <bits/stdc++.h>

using namespace std;

int compare(const string &a, const string &b) {  // 0: a < b, 1: a > b, 2: a = b
    if (a.length() != b.length()) {  // take longer number
        return a.length() > b.length();
    }
    for (int i = 0; i < a.length(); i++) {  // same length, compare each digit
        if (a[i] != b[i]) {
            return a[i] > b[i];  // compare char is same as compare digit
        }
    }
    return 2;  // spacial case: same number
}

string add(string a, string b) {
    if (b.length() > a.length()) swap(a, b);
    string fill(a.length() - b.length(), '0');  // fill with leading zeros to make length equal
    b = fill + b;  // fill b with zeros on the left

    string res(a.length() + 1, '0');
    int cur;
    int carry = 0;

    for (int i = a.length() - 1; i >= 0; i--) {  // add digits
        cur = (a[i] - '0') + (b[i] - '0') + carry;
        carry = 0;
        if (cur > 9) {
            cur -= 10;
            carry = 1;
        }
        res[i + 1] = cur + '0';  // +1 because res is 1-indexed in case we need an extra digit on the left
    }
    if (carry) res[0] = '1';  // res has extra digit
    res.erase(0, res.find_first_not_of('0'));  // remove leading zeros
    if (res.empty()) res = "0";  // empty string is 0
    return res;
}

string subtract(string a, string b) {  // big - small
    if (compare(a, b) == 0) swap(a, b);
    string fill(a.length() - b.length(), '0');  // fill with leading zeros to make length equal
    b = fill + b;  // fill b with zeros on the left

    string res(a.length(), '0');
    int cur;
    int borrow = 0;
    for (int i = a.length() - 1; i >= 0; i--) {  // add digits
        cur = (a[i] - '0') - (b[i] - '0') - borrow;
        borrow = 0;
        if (cur < 0) {
            cur += 10;
            borrow = 1;
        }
        res[i] = cur + '0';  // int to char
    }
    res.erase(0, res.find_first_not_of('0'));  // remove leading zeros
    if (res.empty()) res = "0";  // empty string is 0
    return res;
}


int n;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n;
    for (int i = 0; i < n; i++) {
        string a, b;
        cin >> a >> b;

        // handle negative sign
        bool neg_a = a[0] == '-';
        bool neg_b = b[0] == '-';
        if (neg_a) a.erase(0, 1);
        if (neg_b) b.erase(0, 1);

        if (!neg_a && !neg_b) cout << add(a, b) << "\n";  // ++
        else if (neg_a && neg_b) cout << '-' << add(a, b) << "\n";  // --
        else {
            string abs_diff = subtract(a, b);
            int comp = compare(a, b);

            if (comp == 2) cout << "0" << "\n";
            else if (!neg_a && neg_b && comp == 1) cout << abs_diff << "\n";
            else if (!neg_a && neg_b && comp == 0) cout << '-' << abs_diff << "\n";
            else if (neg_a && !neg_b && comp == 0) cout << abs_diff << "\n";
            else cout << '-' << abs_diff << "\n";
        }
    }
    return 0;
}
