use proconio::{fastout, input};

#[allow(non_snake_case)]
#[fastout]
fn main() {
    input! {
        A: [i32; 5]
    }

    for i in 0..4 {
        if A[i] == A[i + 1] {
            println!("YES");
            return;
        }
    }

    println!("NO");
}
