use proconio::{fastout, input};
use std::collections::HashSet;

#[allow(non_snake_case)]
#[fastout]
fn main() {
    input! {
        N: usize,
        S: [String; N],
    }

    let mut ans = HashSet::new();

    for s in S {
        if ans.contains(&s) || ans.contains(&s.chars().rev().collect::<String>()) {
        } else {
            ans.insert(s);
        }
    }

    println!("{}", ans.len());
}
