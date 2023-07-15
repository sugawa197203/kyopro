#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main()
{
	int n;
	cin >> n;
	string b;
	vector<string> a;
	vector<string> _a;

	for (int i = 0; i < n; i++)
	{
		cin >> b;
		a.push_back(b);
	}

	int _nn = n - 1;
	copy(a.begin(), a.end(), _a.begin());

	for (int i = 0; i < _nn; i++)
	{
		_a[0][i + 1] = a[0][i];
	}

	for (int i = 0; i < _nn; i++)
	{
		_a[i + 1][0] = a[i][0];
	}

	for (int i = 0; i < _nn; i++)
	{
		_a[n][i] = a[n][i + 1];
	}

	for (int i = 0; i < _nn; i++)
	{
		_a[i][0] = a[i + 1][0];
	}

	for (int i = 0; i < n; i++)
	{
		cout << _a[i] << endl;
	}
}