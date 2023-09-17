#include <bits/stdc++.h>

using namespace std;

int main() {

    int t; cin >> t;

    while (t--) {
        int a, b, c;
        cin >> a >> b >> c;

        int moves = 0;

        int goal = (a+b)/2;

        int biggest = max(a,b); 

        float diff = biggest - goal; 
        
        int ans = (int) ceil(diff/c);
        
        cout << ans << endl;
    }

    return 0;
}