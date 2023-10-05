#include <bits/stdc++.h>

using namespace std;
using ll = long long;
 
#define N 200003
#define bits 30

int prefix[N][bits];
int a[N];

void build_prefix(int n){
    for(int i = 0; i < n; i++) {
        
        for(int j = 0; j < 30; j++){
            if (a[i] & (1<<j)) {
                prefix[i+1][j] = prefix[i][j] + 1;
            }
            else{
                prefix[i+1][j] = prefix[i][j];
            }
        }
    
    }
}

int main() {
    int t, q, l, k, low ,high, res; 
    cin >> t;
    
    while(t--) {
        int n; cin >> n;
        
        for(int i = 0; i < n; i++){
            cin >> a[i];
        }
        
        build_prefix(n);
        
        cin >> q;
        
        for (int i = 0; i < q; i++) {
            
            cin >> l >> k;
            
            if (a[l-1] < k) {
                cout << -1 << endl;
                continue;
            }

            low = l;
            high = n;
            res = l;
            
            while (low <= high) {
                int s = (low + high) / 2;
                int andy = 0;
                
                for (int j = 0; j < bits; j++) {
                    if (prefix[s][j] - prefix[l-1][j] == s-l+1){
                        andy += (1<<j);
                    }
                }

                if (andy >= k) {
                    low = s + 1;
                    res = max(res, s);
                } else 
                    high = s - 1;
            }
            
            cout << res << endl;
        }
    }

    return 0;
}
