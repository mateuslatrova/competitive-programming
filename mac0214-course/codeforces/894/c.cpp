#include <bits/stdc++.h>

using namespace std;

int main() {

    int t = 0; cin >> t;

    while (t--) {

        int n; cin >> n;

        vector<int> hs;
        for (int i = 0; i < n; i++) {
            int h; cin >> h;
            hs.push_back(h);
        }

        vector<int> new_hs;

        for (int i = n; i >= 1; i--) {
            while (new_hs.size() < hs[i]) {
                new_hs.push_back(i);
            }
        }

        bool symm = true;

        for (int i = 1; i <= n; i++) {
            if (hs[i] != new_hs[i - 1]) {
                symm = false;
                break;
            }
        }

        if (symm)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }

    return 0;
}