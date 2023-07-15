use proconio::{fastout, input};

#[allow(non_snake_case)]
#[fastout]
fn main() {
    input! {
        N: usize,
        M: usize,
        AB: [(i32, i32); M],
    }

    let mut result = vec![vec!["-"; N]; N];

    for (a, b) in AB.iter() {
        result[(a - 1) as usize][(b - 1) as usize] = "o";
        result[(b - 1) as usize][(a - 1) as usize] = "x";
    }

    for line in result {
        println!("{}", line.join(" "));
    }
}
