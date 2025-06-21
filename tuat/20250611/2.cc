#include <bits/stdc++.h>
using namespace std;

int main(void)
{
    int N, K;
    cin >> N >> K;
    vector<int> R(N), ans(N, 1);
    for (int i = 0; i < N; i++)
    {
        cin >> R[i];
    }

    while (1)
    {
        // sum ans
        int sm = reduce(R.begin(), R.end());
        if (sm % K == 0)
        {
            for (auto a : ans)
            {
                cout << a << " ";
            }
        }

        for (int i = N - 1; i >= 0; i--)
        {
            ans[i]++;
            if (ans[i] <= R[i])
                break;

            ans[i] = 1;
        }

        if (sm == N)
        {
            cout << endl;
            return 0;
        }
    }
}