#include <bits/stdc++.h>
using namespace std;

vector<int> S(int n){
    if (n == 1) return {1};

    auto v = S(n - 1);
    auto retval = vector<int>(v);
    retval.push_back(n);
    retval.insert(retval.end(), v.begin(), v.end());
    return retval;
}

int main(void){
    int N;
    cin >> N;
    for (auto v : S(N)) {
        cout << v << " ";
    }
}