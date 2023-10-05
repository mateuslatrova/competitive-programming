#include <bits/stdc++.h>

using namespace std;

int main() {

    int t; cin >> t;
    int n, last, curr;
    
    while (t--) {
        cin >> n;
    
        vector<int> a = {1, 4};

        for (int i = 2; i < n; i++) {
            last = a[i-1];
            curr = last + 1;

            while ((last + curr) % 3 == 0)
                curr++;

            a.push_back(curr);                                                            
        }

        for (int i = 0; i < n; i++) {
            cout << a[i];
            if (i == n-1)
                cout << endl;
            else
                cout << " ";
        }

    }

    return 0;
}