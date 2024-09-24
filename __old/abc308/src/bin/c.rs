use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        n: i32,
        ab: [(f64, f64); n],
    }

    let mut ans = vec![];

    let mut i = 0;
    for (a, b) in ab {
        ans.push((a / (a + b), i));
        i += 1;
    }

    // sort ans up by 1
    //ans.sort_by(|a, b| a.1.cmp(&b.0));

    for (a, i) in ans {
        print!("{} {}\n", a, i);
    }
}
