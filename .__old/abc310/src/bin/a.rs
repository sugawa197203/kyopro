use proconio::{fastout, input};

#[allow(non_snake_case)]
#[fastout]
fn main() {
    input! {
        N: usize,
        P: i32,
        Q: i32,
        D: [i32; N],
    }

    let m = D.iter().min().unwrap();

    if P <= *m + Q {
        println!("{}", P);
        return;
    }
    println!("{}", Q + m);
}
