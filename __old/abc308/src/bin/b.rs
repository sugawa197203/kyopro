use proconio::{input, fastout};

#[fastout]
fn main() {
    input! {
        n: i32,
        ab: [(i32, i32); n],
    }

    

    let mut ans = vec![];

    let mut i = 0;
    for (a, b) in ab {
        ans.push((a / (a + b), i));
        i += 1;
    }

    // sort ans up
    ans.sort_by(|a, b| a.0.cmp(&b.0));

    for (_, i) in ans {
        print!("{} ", i);
    }
}
