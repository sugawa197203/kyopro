#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
	int N;
	vector<unsigned int> A(2 * N - 1);

	vector<unsigned int> B(N);

	cin >> N;
	int n = 2 * N;

	for (int i = 0; i < n; i++)
	{
		cin >> A.at(i);
	}

	for (int i = 0, j = 0; i < N; i++, j += 2)
	{
		B[i] = A[j] ^ A[j + 1];
	}

	sort(B.begin(), B.end());
}