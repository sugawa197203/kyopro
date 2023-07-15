use proconio::{fastout, input};

#[allow(non_snake_case)]
#[fastout]
fn main() {
    input! {
        data:[i32; 3]
    }

    let max = data.iter().max().unwrap();
    let min = data.iter().min().unwrap();

    println!("{}", max - min);
}
