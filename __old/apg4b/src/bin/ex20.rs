use proconio::{fastout, input};

#[allow(non_snake_case)]
#[fastout]
fn main() {
    input! {
        N:usize,
        P:[usize; N-1],
    }

    let mut cnt = vec![1; N];
    for i in (0..N - 1).rev() {
        cnt[P[i]] += cnt[i + 1];
    }
    for i in cnt {
        println!("{}", i);
    }
}
