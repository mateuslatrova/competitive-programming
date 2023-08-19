#include <bits/stdc++.h>
#include <iostream>

using namespace std;

int main()
{

    int t, n, cuts, a, b;
    cin >> t;

    while (t--)
    {
        cin >> n;
        cuts = 0;

        for (int i = 0; i < n; i++)
        {
            cin >> a >> b;
            if (b < a)
                cuts++;
        }

        cout << cuts << endl;
    }

    return 0;
}