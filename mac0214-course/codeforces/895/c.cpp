#include <bits/stdc++.h>

using namespace std;

int gcd(int a, int b)
{
    while (b != 0)
    {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main()
{

    int t;
    cin >> t;

    while (t--)
    {
        int l, r;
        cin >> l >> r;
        int a, b;
        bool found = false;

        for (int i = 1; i < r; i++)
        {
            if (found)
                break;
            for (int j = 1; j < r; j++)
            {
                int soma = i + j;
                if (l <= soma <= r)
                {
                    if (gcd(i, j) != 1)
                    {
                        found = true;
                        a = i, b = j;
                        break;
                    }
                }
            }
        }

        if (found)
            cout << a << " " << b << endl;
        else
            cout << -1 << endl;
    }

    return 0;
}