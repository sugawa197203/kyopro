#include <iostream>
#include <vector>
#include <queue>
#include <map>
using namespace std;

int H, W;
vector<vector<char>> Grid, ans;

vector<pair<int, int>> Directions = {
    {1, 0}, {0, 1}, {-1, 0}, {0, -1}
};

map<pair<int, int>, char> DirectionStr = {
    {{1, 0}, '^'},
    {{0, 1}, '<'},
    {{-1, 0}, 'v'},
    {{0, -1}, '>'}
};

char strByDir(pair<int, int> a, pair<int, int> b) {
    int dh = a.first - b.first;
    int dw = a.second - b.second;
    return DirectionStr[{dh, dw}];
}

vector<pair<int, int>> get_next(pair<int, int> pos, pair<int, int> from) {
    vector<pair<int, int>> retval;
    int h = pos.first, w = pos.second;

    for (auto [dh, dw] : Directions) {
        int nh = h + dh, nw = w + dw;
        if (nh < 0 || nh >= H || nw < 0 || nw >= W) continue;
        if (nh == from.first && nw == from.second) continue;
        if (Grid[nh][nw] != '#' && Grid[nh][nw] != 'E') {
            retval.emplace_back(nh, nw);
        }
    }
    return retval;
}

int main() {
    cin >> H >> W;
    Grid.resize(H, vector<char>(W));
    ans.resize(H, vector<char>(W));

    vector<pair<int, int>> start;

    for (int h = 0; h < H; ++h) {
        for (int w = 0; w < W; ++w) {
            cin >> Grid[h][w];
            ans[h][w] = Grid[h][w];
            if (Grid[h][w] == 'E') {
                start.emplace_back(h, w);
            }
        }
    }

    if (start.empty()) {
        for (int h = 0; h < H; ++h) {
            for (int w = 0; w < W; ++w) {
                cout << ans[h][w];
            }
            cout << '\n';
        }
        return 0;
    }

    queue<pair<pair<int, int>, pair<int, int>>> q;
    for (auto s : start) {
        q.push({s, s});
    }

    while (!q.empty()) {
        auto [pos, from] = q.front(); q.pop();
        for (auto nxt : get_next(pos, from)) {
            if (ans[nxt.first][nxt.second] == '.') {
                ans[nxt.first][nxt.second] = strByDir(nxt, pos);
                q.push({nxt, pos});
            }
        }
    }

    for (int h = 0; h < H; ++h) {
        for (int w = 0; w < W; ++w) {
            cout << ans[h][w];
        }
        cout << '\n';
    }

    return 0;
}
