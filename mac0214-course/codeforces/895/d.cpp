#include <bits/stdc++.h>

using namespace std;
#define ll long long

ll gcd(ll a, ll b) {
    while (b != 0) {
        ll temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

ll lcm(ll a, ll b) {
    return (a * b) / gcd(a, b);
}

int main()
{

    ll t;
    cin >> t;

    while (t--)
    {
        ll n, x, y;
        cin >> n >> x >> y;

        ll score = 0;

        ll nums_in_left = n/x;
        ll nums_in_right = n/y;

        ll l = lcm(x, y);

        ll num_of_positions_in_left_and_right = n/l;

        ll start = n-nums_in_left+num_of_positions_in_left_and_right+1;
        ll end = n;
        ll soma = ( (1+end) * (end/2) ) - ( (start) * ((start-1)/2) );
        score += soma;

        // for (ll i = n; i > (n-nums_in_left+num_of_positions_in_left_and_right); i--)
        //     score += i;
        
        start = 1;
        end = nums_in_right-num_of_positions_in_left_and_right;
        ll sub = ( (1+end) * (end/2) ) - ( (start) * ((start-1)/2) );
        score -= sub;

        // for (ll i = 1; i <= nums_in_right-num_of_positions_in_left_and_right; i++)
        //     score -= i;
        
        cout << score << endl;
    }   

    return 0;
}