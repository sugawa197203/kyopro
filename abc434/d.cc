#include <iostream>
#include <vector>

using namespace std;

const int SIZE = 2000;

struct Cloud {
    int u, d, l, r;
};

int main() {

    int N;
    cin >> N;

    vector<Cloud> clouds(N);
    for (int i = 0; i < N; ++i) {
        cin >> clouds[i].u >> clouds[i].d >> clouds[i].l >> clouds[i].r;
        clouds[i].u--;
        clouds[i].l--;
    }

    vector<int> single_contribution(N, 0);
    
    long long sum_cloud = 0;

    vector<int> count_diff(SIZE + 1);
    vector<int> id_diff(SIZE + 1);

    for (int row = 0; row < SIZE; ++row) {
        fill(count_diff.begin(), count_diff.end(), 0);
        fill(id_diff.begin(), id_diff.end(), 0);

        for (int i = 0; i < N; ++i) {
            if (clouds[i].u <= row && row < clouds[i].d) {
                count_diff[clouds[i].l]++;
                count_diff[clouds[i].r]--;
                
                id_diff[clouds[i].l] += i;
                id_diff[clouds[i].r] -= i;
            }
        }

        int current_overlap = 0;
        int current_id_sum = 0;

        for (int col = 0; col < SIZE; ++col) {
            current_overlap += count_diff[col];
            current_id_sum += id_diff[col];

            if (current_overlap > 0) {
                sum_cloud++;
                
                if (current_overlap == 1) {
                    single_contribution[current_id_sum]++;
                }
            }
        }
    }

    long long total_grid_area = (long long)SIZE * SIZE;
    for (int i = 0; i < N; ++i) {
        cout << total_grid_area - (sum_cloud - single_contribution[i]) << endl;
    }

    return 0;
}