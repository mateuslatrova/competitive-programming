#include <bits/stdc++.h>

using namespace std;

int main() {

    int t; cin >> t;
    
    int n, k, x, min_sum, max_sum;
    
    while (t--) {
        cin >> n >> k >> x;
        min_sum = x * (x+1) / 2;
        max_sum =  (n * (n+1) - (n-x) * (n-x+1)) / 2;
        if (k >= min_sum && k <= max_sum)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }

    return 0;
}