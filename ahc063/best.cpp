#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")
#include <bits/stdc++.h>
using namespace std;

struct Timer {
    chrono::steady_clock::time_point st;
    Timer() : st(chrono::steady_clock::now()) {}
    double elapsed() const {
        return chrono::duration<double>(chrono::steady_clock::now() - st).count();
    }
};

struct XorShift {
    uint64_t x;
    explicit XorShift(uint64_t seed = 88172645463325252ULL) : x(seed) {}
    uint32_t next_u32() {
        x ^= x << 7;
        x ^= x >> 9;
        return static_cast<uint32_t>(x);
    }
};

constexpr int MAX_CELLS = 256;
constexpr int MAX_M = 256;
constexpr int MAX_HORIZON = 14;
constexpr int INF_DIST = 1'000'000;

constexpr int DR[4] = {-1, 1, 0, 0};
constexpr int DC[4] = {0, 0, -1, 1};
constexpr int DELTA[4] = {-16, 16, -1, 1};
constexpr char DCH[4] = {'U', 'D', 'L', 'R'};

int N, M, C;
uint8_t desired[MAX_M];
int ROW[MAX_CELLS];
int COL[MAX_CELLS];

inline int pack_cell(int r, int c) {
    return (r << 4) | c;
}

inline bool can_move(int cell, int dir) {
    const int r = ROW[cell];
    const int c = COL[cell];
    if (dir == 0) return r > 0;
    if (dir == 1) return r + 1 < N;
    if (dir == 2) return c > 0;
    return c + 1 < N;
}

inline int visit_index(int len, int cell) {
    return len * 256 + cell;
}

struct State {
    uint8_t food[MAX_CELLS]{};
    uint8_t body[MAX_CELLS]{};
    uint8_t color[MAX_M]{};
    uint16_t len = 0;
    uint16_t remaining = 0;
    uint16_t wrong = 0;
    uint16_t prefix = 0;

    inline int head() const {
        return body[0];
    }
};

struct StepInfo {
    bool ate = false;
    uint8_t eaten_color = 0;
    uint8_t cut_removed = 0;
};

struct Route {
    vector<int> dirs;
    State end;
    int gain = 0;
    long long eval = numeric_limits<long long>::min();
    bool found = false;
};

long long absolute_score(const State& s, int turns) {
    return static_cast<long long>(turns) + 10000LL * (s.wrong + 2LL * (M - s.len));
}

bool step(State& s, int dir, StepInfo* info = nullptr) {
    const int head = s.body[0];
    if (!can_move(head, dir)) return false;

    const int nh = head + DELTA[dir];
    if (s.len >= 2 && nh == s.body[1]) return false;

    if (info) *info = StepInfo{};

    const int len = s.len;
    const uint8_t fc = s.food[nh];

    if (fc != 0) {
        memmove(s.body + 1, s.body, len * sizeof(uint8_t));
        s.body[0] = static_cast<uint8_t>(nh);
        s.color[len] = fc;
        s.len = static_cast<uint16_t>(len + 1);
        s.food[nh] = 0;
        --s.remaining;

        if (fc != desired[len]) ++s.wrong;
        if (s.prefix == len && fc == desired[len]) ++s.prefix;

        if (info) {
            info->ate = true;
            info->eaten_color = fc;
        }
        return true;
    }

    memmove(s.body + 1, s.body, (len - 1) * sizeof(uint8_t));
    s.body[0] = static_cast<uint8_t>(nh);

    int new_len = len;
    for (int i = 1; i <= len - 2; ++i) {
        if (s.body[i] == nh) {
            new_len = i + 1;
            break;
        }
    }

    if (new_len < len) {
        for (int p = new_len; p < len; ++p) {
            const int cell = s.body[p];
            s.food[cell] = s.color[p];
            ++s.remaining;
            if (s.color[p] != desired[p]) --s.wrong;
        }
        s.len = static_cast<uint16_t>(new_len);
        if (s.prefix > new_len) s.prefix = static_cast<uint16_t>(new_len);
        if (info) info->cut_removed = static_cast<uint8_t>(len - new_len);
    }

    return true;
}

void record_visit(const State& s, vector<int>& visit_count) {
    const int len = min<int>(s.len, M);
    const int idx = visit_index(len, s.head());
    if (visit_count[idx] < 1'000'000) ++visit_count[idx];
}

void record_best(const State& s, const vector<char>& ans, long long& best_score, int& best_len) {
    const long long sc = absolute_score(s, static_cast<int>(ans.size()));
    if (sc < best_score) {
        best_score = sc;
        best_len = static_cast<int>(ans.size());
    }
}

void build_free_time(const State& s, int free_time[MAX_CELLS]) {
    fill(free_time, free_time + MAX_CELLS, 0);
    for (int i = 0; i < s.len; ++i) {
        const int cell = s.body[i];
        free_time[cell] = max(free_time[cell], static_cast<int>(s.len) - i);
    }
}

int nearest_md_color(const State& s, int cell, int target_color, bool exclude_same_cell = false) {
    int best = INF_DIST;
    const int sr = ROW[cell];
    const int sc = COL[cell];
    for (int r = 0; r < N; ++r) {
        for (int c = 0; c < N; ++c) {
            const int idx = pack_cell(r, c);
            if (s.food[idx] != target_color) continue;
            if (exclude_same_cell && idx == cell) continue;
            best = min(best, abs(sr - r) + abs(sc - c));
        }
    }
    return best == INF_DIST ? 2 * N * N : best;
}

int reachable_area(const State& s) {
    static bool blocked[MAX_CELLS];
    static bool vis[MAX_CELLS];
    fill(blocked, blocked + MAX_CELLS, false);
    fill(vis, vis + MAX_CELLS, false);
    for (int i = 1; i + 1 < s.len; ++i) blocked[s.body[i]] = true;

    queue<int> q;
    q.push(s.head());
    vis[s.head()] = true;
    int cnt = 0;

    while (!q.empty()) {
        const int cur = q.front();
        q.pop();
        ++cnt;
        for (int dir = 0; dir < 4; ++dir) {
            if (!can_move(cur, dir)) continue;
            const int nxt = cur + DELTA[dir];
            if (blocked[nxt] || vis[nxt]) continue;
            vis[nxt] = true;
            q.push(nxt);
        }
    }

    return cnt;
}

int reachable_area_target(const State& s, int target_color) {
    static bool blocked[MAX_CELLS];
    static bool vis[MAX_CELLS];
    fill(blocked, blocked + MAX_CELLS, false);
    fill(vis, vis + MAX_CELLS, false);
    for (int i = 1; i < s.len; ++i) blocked[s.body[i]] = true;

    queue<int> q;
    q.push(s.head());
    vis[s.head()] = true;
    int cnt = 0;

    while (!q.empty()) {
        const int cur = q.front();
        q.pop();
        ++cnt;
        for (int dir = 0; dir < 4; ++dir) {
            if (!can_move(cur, dir)) continue;
            const int nxt = cur + DELTA[dir];
            if (blocked[nxt] || vis[nxt]) continue;
            if (s.food[nxt] != 0 && s.food[nxt] != target_color) continue;
            vis[nxt] = true;
            q.push(nxt);
        }
    }

    return cnt;
}

int static_goal_distance(const State& s, int target_color) {
    if (target_color <= 0) return 0;

    static bool blocked[MAX_CELLS];
    static int dist[MAX_CELLS];
    fill(blocked, blocked + MAX_CELLS, false);
    fill(dist, dist + MAX_CELLS, -1);
    for (int i = 1; i < s.len; ++i) blocked[s.body[i]] = true;

    queue<int> q;
    q.push(s.head());
    dist[s.head()] = 0;

    while (!q.empty()) {
        const int cur = q.front();
        q.pop();
        for (int dir = 0; dir < 4; ++dir) {
            if (!can_move(cur, dir)) continue;
            const int nxt = cur + DELTA[dir];
            if (blocked[nxt] || dist[nxt] != -1) continue;
            if (s.food[nxt] != 0 && s.food[nxt] != target_color) continue;
            dist[nxt] = dist[cur] + 1;
            if (s.food[nxt] == target_color) return dist[nxt];
            q.push(nxt);
        }
    }

    return INF_DIST;
}

long long future_eval(const State& s, int turns, const vector<int>& visit_count) {
    long long val = -absolute_score(s, turns) * 1024LL;
    val += 2'000'000LL * s.prefix;
    val -= 400'000LL * s.wrong;

    const int head = s.head();
    const int visit = visit_count[visit_index(min<int>(s.len, M), head)];
    val -= 50'000LL * visit;

    if (s.len < M) {
        const int target = desired[s.len];
        int goal = static_goal_distance(s, target);
        if (goal >= INF_DIST) goal = 2 * N * N;
        val -= 200'000LL * goal;
        val -= 20'000LL * nearest_md_color(s, head, target, false);
        val += 4'000LL * reachable_area_target(s, target);
    } else {
        val += 5'000'000'000LL;
    }

    return val;
}

vector<int> reconstruct_exact_route(
    int end_cell,
    int end_p,
    int dist,
    const int prev_cell[MAX_CELLS][MAX_HORIZON + 1],
    const int prev_p[MAX_CELLS][MAX_HORIZON + 1],
    const signed char prev_dir[MAX_CELLS][MAX_HORIZON + 1]
) {
    vector<int> route;
    route.reserve(dist);
    int cell = end_cell;
    int p = end_p;
    int d = dist;
    while (d > 0) {
        const int dir = prev_dir[cell][p];
        route.push_back(dir);
        const int pc = prev_cell[cell][p];
        const int pp = prev_p[cell][p];
        cell = pc;
        p = pp;
        --d;
    }
    reverse(route.begin(), route.end());
    return route;
}

bool validate_exact_route(const State& start, const vector<int>& route, State& end, int& gain) {
    end = start;
    gain = 0;
    for (int dir : route) {
        StepInfo info;
        if (!step(end, dir, &info)) return false;
        if (info.cut_removed > 0) return false;
        if (info.ate) {
            if (start.len + gain >= M) return false;
            if (info.eaten_color != desired[start.len + gain]) return false;
            ++gain;
        }
    }
    return gain > 0;
}

bool validate_empty_route(const State& start, const vector<int>& route, State& end) {
    end = start;
    for (int dir : route) {
        StepInfo info;
        if (!step(end, dir, &info)) return false;
        if (info.ate || info.cut_removed > 0) return false;
    }
    return true;
}

Route plan_exact(const State& s, int turn_base, const vector<int>& visit_count, XorShift& rng, int horizon) {
    Route best;
    if (s.remaining == 0 || s.len >= M) return best;

    horizon = min(horizon, MAX_HORIZON);
    horizon = min(horizon, M - static_cast<int>(s.len));
    if (horizon <= 0) return best;

    int free_time[MAX_CELLS];
    build_free_time(s, free_time);

    static int dist[MAX_CELLS][MAX_HORIZON + 1];
    static int prev_cell[MAX_CELLS][MAX_HORIZON + 1];
    static int prev_p[MAX_CELLS][MAX_HORIZON + 1];
    static signed char prev_dir[MAX_CELLS][MAX_HORIZON + 1];

    for (int cell = 0; cell < MAX_CELLS; ++cell) {
        for (int p = 0; p <= horizon; ++p) {
            dist[cell][p] = -1;
            prev_cell[cell][p] = -1;
            prev_p[cell][p] = -1;
            prev_dir[cell][p] = -1;
        }
    }

    struct Node {
        uint8_t cell;
        uint8_t p;
    };
    static Node que[MAX_CELLS * (MAX_HORIZON + 1)];
    int qh = 0;
    int qt = 0;

    dist[s.head()][0] = 0;
    que[qt++] = Node{static_cast<uint8_t>(s.head()), 0};

    const int max_dist = min(8 * N + 4 * horizon, 96);

    while (qh < qt) {
        const Node cur = que[qh++];
        const int cell = cur.cell;
        const int p = cur.p;
        const int cd = dist[cell][p];
        if (cd >= max_dist) continue;

        for (int dir = 0; dir < 4; ++dir) {
            if (!can_move(cell, dir)) continue;
            const int nxt = cell + DELTA[dir];
            const int nd = cd + 1;
            if (nd < free_time[nxt] + p) continue;

            int np = p;
            const int fc = s.food[nxt];
            if (fc != 0) {
                if (p >= horizon) continue;
                if (fc != desired[s.len + p]) continue;
                np = p + 1;
            }

            if (dist[nxt][np] != -1) continue;
            dist[nxt][np] = nd;
            prev_cell[nxt][np] = cell;
            prev_p[nxt][np] = p;
            prev_dir[nxt][np] = static_cast<signed char>(dir);
            que[qt++] = Node{static_cast<uint8_t>(nxt), static_cast<uint8_t>(np)};
        }
    }

    struct Candidate {
        uint8_t cell;
        uint8_t p;
        uint8_t d;
        long long key;
    };

    vector<Candidate> cands;
    cands.reserve(MAX_CELLS * horizon);

    for (int r = 0; r < N; ++r) {
        for (int c = 0; c < N; ++c) {
            const int cell = pack_cell(r, c);
            for (int p = 1; p <= horizon; ++p) {
                if (dist[cell][p] == -1) continue;
                const int next_md =
                    (s.len + p < M) ? nearest_md_color(s, cell, desired[s.len + p], false) : 0;
                const int visit = visit_count[visit_index(min<int>(s.len + p, M), cell)];
                long long key = 1'000'000'000'000LL * p;
                key -= 15'000'000LL * dist[cell][p];
                key -= 1'500'000LL * next_md;
                key -= 250'000LL * visit;
                key += static_cast<int>(rng.next_u32() & 1023U);
                cands.push_back(Candidate{
                    static_cast<uint8_t>(cell),
                    static_cast<uint8_t>(p),
                    static_cast<uint8_t>(dist[cell][p]),
                    key
                });
            }
        }
    }

    sort(cands.begin(), cands.end(), [](const Candidate& a, const Candidate& b) {
        return a.key > b.key;
    });

    const int check_limit = min<int>(48, cands.size());
    for (int i = 0; i < check_limit; ++i) {
        const auto& cand = cands[i];
        vector<int> route = reconstruct_exact_route(
            cand.cell, cand.p, cand.d, prev_cell, prev_p, prev_dir
        );
        State end;
        int gain = 0;
        if (!validate_exact_route(s, route, end, gain)) continue;

        long long eval = future_eval(end, turn_base + static_cast<int>(route.size()), visit_count);
        eval += 50'000'000LL * gain;
        eval -= 2'000LL * static_cast<int>(route.size());

        if (eval > best.eval) {
            best.found = true;
            best.dirs = move(route);
            best.end = end;
            best.gain = gain;
            best.eval = eval;
        }
    }

    return best;
}

Route plan_stage_and_exact(
    const State& s,
    int turn_base,
    const vector<int>& visit_count,
    XorShift& rng,
    int exact_horizon
) {
    Route best;
    if (s.len >= M) return best;

    const int target = desired[s.len];
    const int base_goal = static_goal_distance(s, target);
    int free_time[MAX_CELLS];
    build_free_time(s, free_time);

    static int dist[MAX_CELLS];
    static int prev_cell[MAX_CELLS];
    static signed char prev_dir[MAX_CELLS];
    fill(dist, dist + MAX_CELLS, -1);
    fill(prev_cell, prev_cell + MAX_CELLS, -1);
    fill(prev_dir, prev_dir + MAX_CELLS, -1);

    queue<int> q;
    dist[s.head()] = 0;
    q.push(s.head());

    const int max_dist = min(6 * N, 80);
    while (!q.empty()) {
        const int cur = q.front();
        q.pop();
        const int cd = dist[cur];
        if (cd >= max_dist) continue;

        for (int dir = 0; dir < 4; ++dir) {
            if (!can_move(cur, dir)) continue;
            const int nxt = cur + DELTA[dir];
            const int nd = cd + 1;
            if (dist[nxt] != -1) continue;
            if (nd < free_time[nxt]) continue;
            if (s.food[nxt] != 0) continue;
            dist[nxt] = nd;
            prev_cell[nxt] = cur;
            prev_dir[nxt] = static_cast<signed char>(dir);
            q.push(nxt);
        }
    }

    struct Candidate {
        uint8_t cell;
        uint8_t d;
        long long key;
    };
    vector<Candidate> cands;
    for (int r = 0; r < N; ++r) {
        for (int c = 0; c < N; ++c) {
            const int cell = pack_cell(r, c);
            if (dist[cell] <= 0) continue;
            const int md = nearest_md_color(s, cell, target, false);
            const int visit = visit_count[visit_index(min<int>(s.len, M), cell)];
            long long key = -2'000'000LL * md;
            key -= 500'000LL * dist[cell];
            key -= 100'000LL * visit;
            key += static_cast<int>(rng.next_u32() & 1023U);
            cands.push_back(Candidate{
                static_cast<uint8_t>(cell),
                static_cast<uint8_t>(dist[cell]),
                key
            });
        }
    }

    sort(cands.begin(), cands.end(), [](const Candidate& a, const Candidate& b) {
        return a.key > b.key;
    });

    const int check_limit = min<int>(24, cands.size());
    for (int i = 0; i < check_limit; ++i) {
        const auto& cand = cands[i];
        vector<int> route;
        route.reserve(cand.d);
        int cell = cand.cell;
        int d = cand.d;
        while (d > 0) {
            route.push_back(prev_dir[cell]);
            cell = prev_cell[cell];
            --d;
        }
        reverse(route.begin(), route.end());

        State mid;
        if (!validate_empty_route(s, route, mid)) continue;

        Route exact = plan_exact(
            mid, turn_base + static_cast<int>(route.size()), visit_count, rng, exact_horizon
        );

        if (exact.found) {
            Route cand_route;
            cand_route.found = true;
            cand_route.dirs = route;
            cand_route.dirs.insert(
                cand_route.dirs.end(), exact.dirs.begin(), exact.dirs.end()
            );
            cand_route.end = exact.end;
            cand_route.gain = exact.gain;
            cand_route.eval = future_eval(
                cand_route.end, turn_base + static_cast<int>(cand_route.dirs.size()), visit_count
            );
            cand_route.eval += 40'000'000LL * exact.gain;
            cand_route.eval -= 2'000LL * static_cast<int>(route.size());
            if (cand_route.eval > best.eval) best = move(cand_route);
            continue;
        }

        const int new_goal = static_goal_distance(mid, target);
        if (new_goal + 2 >= base_goal) continue;

        Route cand_route;
        cand_route.found = true;
        cand_route.dirs = move(route);
        cand_route.end = mid;
        cand_route.gain = 0;
        cand_route.eval =
            future_eval(mid, turn_base + static_cast<int>(cand_route.dirs.size()), visit_count);
        cand_route.eval += 5'000'000LL * (base_goal - new_goal);
        if (cand_route.eval > best.eval) best = move(cand_route);
    }

    return best;
}

vector<int> reconstruct_beam_path(const vector<struct BeamNode>& pool, int idx);

struct BeamNode {
    State st;
    int parent = -1;
    uint8_t move = 255;
    uint8_t depth = 0;
    long long key = numeric_limits<long long>::min();
};

vector<int> reconstruct_beam_path(const vector<BeamNode>& pool, int idx) {
    vector<int> route;
    while (pool[idx].parent != -1) {
        route.push_back(pool[idx].move);
        idx = pool[idx].parent;
    }
    reverse(route.begin(), route.end());
    return route;
}

Route plan_local_beam(
    const State& s,
    int turn_base,
    const vector<int>& visit_count,
    XorShift& rng,
    int depth_limit,
    int beam_width,
    int exact_horizon
) {
    Route best;

    vector<BeamNode> pool;
    pool.reserve(1 + depth_limit * beam_width * 4);
    pool.push_back(BeamNode{s, -1, 255, 0, 0});

    vector<int> cur{0};
    for (int depth = 1; depth <= depth_limit; ++depth) {
        vector<int> next;
        next.reserve(cur.size() * 4);

        for (int idx : cur) {
            const State& base = pool[idx].st;
            for (int dir = 0; dir < 4; ++dir) {
                BeamNode node;
                node.st = base;
                StepInfo info;
                if (!step(node.st, dir, &info)) continue;

                node.parent = idx;
                node.move = static_cast<uint8_t>(dir);
                node.depth = static_cast<uint8_t>(depth);

                const int head = node.st.head();
                const int visit = visit_count[visit_index(min<int>(node.st.len, M), head)];
                long long key = -absolute_score(node.st, turn_base + depth) * 64LL;
                key += 5'000'000LL * node.st.prefix;
                key -= 500'000LL * node.st.wrong;
                key -= 60'000LL * visit;
                if (node.st.len < M) {
                    key -= 120'000LL *
                           nearest_md_color(node.st, head, desired[node.st.len], false);
                }
                if (info.cut_removed > 0) {
                    key += 1'200'000LL * info.cut_removed;
                }
                if (info.ate && node.st.len <= M && info.eaten_color == desired[node.st.len - 1]) {
                    key += 30'000'000LL;
                }
                key += static_cast<int>(rng.next_u32() & 2047U);
                node.key = key;

                pool.push_back(node);
                next.push_back(static_cast<int>(pool.size()) - 1);
            }
        }

        if (next.empty()) break;

        sort(next.begin(), next.end(), [&](int a, int b) {
            return pool[a].key > pool[b].key;
        });
        if (static_cast<int>(next.size()) > beam_width) next.resize(beam_width);
        cur = next;

        const int eval_count = min<int>(12, cur.size());
        for (int i = 0; i < eval_count; ++i) {
            const int idx = cur[i];
            vector<int> outer = reconstruct_beam_path(pool, idx);
            const State& mid = pool[idx].st;

            Route exact = plan_exact(
                mid, turn_base + static_cast<int>(outer.size()), visit_count, rng, exact_horizon
            );

            Route cand;
            cand.found = true;
            cand.dirs = move(outer);
            cand.end = mid;
            cand.gain = 0;
            if (exact.found) {
                cand.dirs.insert(cand.dirs.end(), exact.dirs.begin(), exact.dirs.end());
                cand.end = exact.end;
                cand.gain = exact.gain;
            }

            cand.eval = future_eval(
                cand.end, turn_base + static_cast<int>(cand.dirs.size()), visit_count
            );
            cand.eval += 40'000'000LL * cand.gain;
            cand.eval -= 1'000LL * static_cast<int>(cand.dirs.size());
            if (cand.eval > best.eval) best = move(cand);
        }
    }

    return best;
}

Route plan_single_step(
    const State& s,
    int turn_base,
    const vector<int>& visit_count,
    XorShift& rng,
    int exact_horizon
) {
    Route best;

    array<int, 4> dirs = {0, 1, 2, 3};
    rotate(dirs.begin(), dirs.begin() + (rng.next_u32() & 3U), dirs.end());

    for (int dir : dirs) {
        State mid = s;
        StepInfo info;
        if (!step(mid, dir, &info)) continue;

        Route exact = plan_exact(mid, turn_base + 1, visit_count, rng, exact_horizon);

        Route cand;
        cand.found = true;
        cand.dirs = {dir};
        cand.end = mid;
        cand.gain = 0;
        if (exact.found) {
            cand.dirs.insert(cand.dirs.end(), exact.dirs.begin(), exact.dirs.end());
            cand.end = exact.end;
            cand.gain = exact.gain;
        }

        cand.eval = future_eval(
            cand.end, turn_base + static_cast<int>(cand.dirs.size()), visit_count
        );
        cand.eval += 35'000'000LL * cand.gain;
        if (info.cut_removed > 0) cand.eval += 5'000'000LL * info.cut_removed;
        if (info.ate && cand.gain == 0) {
            cand.eval -= (info.eaten_color == desired[s.len]) ? 0LL : 20'000'000LL;
        }

        if (cand.eval > best.eval) best = move(cand);
    }

    return best;
}

void execute_route(
    State& s,
    vector<char>& ans,
    const vector<int>& route,
    vector<int>& visit_count,
    long long& best_score,
    int& best_len,
    int& stagnation,
    const Timer& timer,
    double deadline
) {
    for (int dir : route) {
        if (static_cast<int>(ans.size()) >= 100000) break;
        if ((ans.size() & 63U) == 0 && timer.elapsed() > deadline) break;

        StepInfo info;
        if (!step(s, dir, &info)) break;
        ans.push_back(DCH[dir]);
        if (info.ate) stagnation = 0;
        else ++stagnation;
        record_visit(s, visit_count);
        record_best(s, ans, best_score, best_len);
    }
}

vector<char> solve(const State& initial) {
    State s = initial;
    vector<char> ans;
    ans.reserve(100000);

    vector<int> visit_count((M + 1) * 256, 0);
    record_visit(s, visit_count);

    long long best_score = absolute_score(s, 0);
    int best_len = 0;
    int stagnation = 0;

    Timer timer;
    constexpr double DEADLINE = 1.82;
    XorShift rng(123456789ULL + 10007ULL * N + 1000003ULL * M + 1000000007ULL * C);

    while (static_cast<int>(ans.size()) < 100000 && timer.elapsed() < DEADLINE) {
        Route best_route;

        int exact_horizon = 12;
        if (timer.elapsed() > DEADLINE - 0.45) exact_horizon = 10;
        if (timer.elapsed() > DEADLINE - 0.20) exact_horizon = 8;

        Route exact = plan_exact(s, static_cast<int>(ans.size()), visit_count, rng, exact_horizon);
        if (exact.found) best_route = exact;

        if (s.len < M && timer.elapsed() < DEADLINE - 0.08) {
            Route stage = plan_stage_and_exact(
                s, static_cast<int>(ans.size()), visit_count, rng, min(exact_horizon, 8)
            );
            if (stage.found && stage.eval > best_route.eval) best_route = move(stage);
        }

        if ((!best_route.found || best_route.gain <= 1 || stagnation >= 2 * N) &&
            timer.elapsed() < DEADLINE - 0.12) {
            Route beam = plan_local_beam(
                s, static_cast<int>(ans.size()), visit_count, rng,
                (timer.elapsed() < DEADLINE - 0.30) ? 7 : 6,
                (timer.elapsed() < DEADLINE - 0.30) ? 48 : 32,
                min(exact_horizon, 7)
            );
            if (beam.found && beam.eval > best_route.eval) best_route = move(beam);
        }

        Route one = plan_single_step(
            s, static_cast<int>(ans.size()), visit_count, rng, min(exact_horizon, 6)
        );
        if (one.found && one.eval > best_route.eval) best_route = move(one);

        if (!best_route.found || best_route.dirs.empty()) break;
        execute_route(
            s, ans, best_route.dirs, visit_count, best_score, best_len,
            stagnation, timer, DEADLINE
        );
    }

    ans.resize(best_len);
    return ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    for (int cell = 0; cell < MAX_CELLS; ++cell) {
        ROW[cell] = cell >> 4;
        COL[cell] = cell & 15;
    }

    cin >> N >> M >> C;
    for (int i = 0; i < M; ++i) {
        int x;
        cin >> x;
        desired[i] = static_cast<uint8_t>(x);
    }

    State initial;
    initial.len = 5;
    initial.prefix = 5;
    initial.wrong = 0;
    for (int i = 0; i < 5; ++i) initial.color[i] = 1;
    initial.body[0] = static_cast<uint8_t>(pack_cell(4, 0));
    initial.body[1] = static_cast<uint8_t>(pack_cell(3, 0));
    initial.body[2] = static_cast<uint8_t>(pack_cell(2, 0));
    initial.body[3] = static_cast<uint8_t>(pack_cell(1, 0));
    initial.body[4] = static_cast<uint8_t>(pack_cell(0, 0));

    for (int r = 0; r < N; ++r) {
        for (int c = 0; c < N; ++c) {
            int x;
            cin >> x;
            initial.food[pack_cell(r, c)] = static_cast<uint8_t>(x);
            if (x != 0) ++initial.remaining;
        }
    }

    vector<char> ans = solve(initial);
    for (char ch : ans) cout << ch << '\n';
    return 0;
}
