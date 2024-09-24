#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>

using namespace std;

int main() {
	int N;
	long double a, b;
	vector<tuple<int, long double>> p;
	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> a >> b;
		p.push_back(make_tuple(i, a / (a + b)));
	}

	sort(p.begin(), p.end(), [](tuple<int, long double> a, tuple<int, long double> b) {
		return get<1>(a) > get<1>(b);
	});

	for (int i = 0; i < N; i++) {
		cout << get<0>(p[i]) + 1 << " ";
	}
}