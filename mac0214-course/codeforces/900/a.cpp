#include <bits/stdc++.h>

using namespace std;

int main() {

    int t; cin >> t;
    int n, k, a_i;
    set<int> a;
    
    while (t--) {
        a = {};
        cin >> n >> k;
        for (int i = 0; i < n; i++) {
            cin >> a_i;
            a.insert(a_i);
        }

        if (a.count(k) > 0)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }

    return 0;
}